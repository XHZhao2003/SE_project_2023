<script setup>
import { Avatar, ElementPlus, Lock } from "@element-plus/icons-vue";
import { ref } from "vue";

defineEmits(["no-account-register"]);
</script>

<template>
  <div class="loginBox">
    <div style="width: 100%; height: 40%; text-align: center; overflow: hidden">
      <img src="../assets/ERoad-logo.png" style="width: 100%; height: 100%" />
    </div>
    <div
      style="
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 60%;
        flex-grow: 0;
      "
    >
      <el-form :model="user" style="width: 80%" :rules="rules" ref="loginRef">
        <div
          style="
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
          "
        >
          欢迎登录
        </div>
        <el-form-item prop="username">
          <el-input
            prefix-icon="Avatar"
            size="medium"
            v-model="user.username"
            placeholder="请输入用户名/邮箱"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            prefix-icon="Lock"
            size="medium"
            show-password
            v-model="user.password"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" style="width: 100%" @click="EventLogin">
            登录
          </el-button>
        </el-form-item>
        <div style="display: flex">
          <div style="flex: 1; text-align: left">
            还没有账号？请
            <span
              style="color: rgb(92, 214, 92); cursor: pointer"
              @click="$emit('no-account-register')"
              >注册
            </span>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import JSEncrypt from 'jsencrypt'
export default {
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  methods: {
    $getRsaCode (str){ // 注册方法
      let pubKey = `-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwYP+FjArOo0msH6lEcl9
        jr82dTvBkzMPgtuLnFKECL+86y7YQnWNADFA+avkLVaTJKxf5vkVwvmTv0Vfps2g
        ZG8ByaEq/JV4y0mevPSe/Jpt8XF/1tL6SfE3ft/0UUfaC7keJp5LLPG9iC7EIlRm
        H2N2opSVD03yt8lCAAMoSrARk4meCrCU1gydlCb2KNMPNbPa9YkG2vDQEZxHSjoY
        h5/01FzKEDUtueG6R1CXSb29fJfRVlpy826jiAo8Ljb4rcobUEsOrmv01Wxk8/OF
        TI8fnNmwDRAqv06uiXgeAB0qVMtvktBm0gl0aTQy+jPetrlbjRf/vwizgEy2/oF8
        bQIDAQAB-----END PUBLIC KEY-----`;// ES6 模板字符串 引用 rsa 公钥
      let encryptStr = new JSEncrypt();
      encryptStr.setPublicKey(pubKey); // 设置 加密公钥
      let data = encryptStr.encrypt(str.toString());  // 进行加密
      return data;
    },
    EventLogin() {
      const that = this;
      this.$refs.loginRef.validate((valid) => {
        // 表单自身rules的规则检查
        if(valid) {
          let senddata = {
            action:"login",
            username: this.user.username,
            password: this.$getRsaCode(this.user.password)
          }
          axios
            .post("http://127.0.0.1:8000/api/AppUser/", senddata)
            .then((res) => {
              if(res.data.status==200){
                localStorage.setItem("loginFlag", "true");
                localStorage.setItem("username", this.user.username)
                this.$router.push("/Map");
              }
              else{
                alert("用户名或密码错误");
              }
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },
  },
};
</script>

<style>
.loginBox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-color: white;
  width: 30%;
  height: 60%;
  border-radius: 5px;
  overflow: hidden;
}
</style>