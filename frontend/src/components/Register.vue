<script setup>
import {
  Avatar,
  ElementPlus,
  Lock,
  Message,
  CircleCheck,
} from "@element-plus/icons-vue";
import { ref } from "vue";
defineEmits(["have-account-login"]);
</script>

<template>
  <div class="registerBox">
    <div style="width: 100%; height: 40%; text-align: center; overflow: hidden">
      <img src="../assets/ERoad-logo.png" style="width: 100%; height: 100%" />
    </div>
    <div
      style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 60%;
        flex-grow: 0;
      "
    >
      <div
        style="
          font-size: 20px;
          font-weight: bold;
          text-align: center;
          margin-bottom: 20px;
        "
      >
        欢迎注册
      </div>

      <el-scrollbar style="width: 80%; height: 70%">
        <el-form
          :model="user"
          style="width: 80% text-align:center"
          :rules="rules"
          ref="registerRef"
        >
          <el-form-item prop="username">
            <el-input
              prefix-icon="Avatar"
              size="medium"
              v-model="user.username"
              placeholder="请输入4-20位用户名"
            ></el-input>
          </el-form-item>

          <el-form-item prop="password">
            <el-input
              prefix-icon="Lock"
              size="medium"
              show-password
              v-model="user.password"
              placeholder="请输入4-20位密码，包含字母与数字"
            ></el-input>
          </el-form-item>

          <el-form-item prop="confirmpassword">
            <el-input
              prefix-icon="Lock"
              size="medium"
              show-password
              v-model="user.confirmpassword"
              placeholder="请确认密码"
            ></el-input>
          </el-form-item>

          <el-form-item prop="email">
            <el-input
              prefix-icon="Message"
              size="medium"
              v-model="user.email"
              placeholder="请输入邮箱"
            ></el-input>
          </el-form-item>

          <el-row>
            <el-col :span="16">
              <el-form-item prop="verifycode" :inline="true">
                <el-input
                  prefix-icon="CircleCheck"
                  size="medium"
                  v-model="user.verifycode"
                  placeholder="请输入验证码"
                ></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="8">
              <el-form-item>
                <el-button
                  plain
                  type="primary"
                  style="width: 100%"
                  @click="EventSendVerifyCode"
                  v-bind:disabled="DisableVerifycodeButton"
                >
                  {{ VerifycodeButtonText }}
                </el-button>
              </el-form-item>
            </el-col>
          </el-row>

          <el-form-item>
            <el-button
              type="primary"
              style="width: 100%"
              @click="EventRegister"
            >
              注册
            </el-button>
          </el-form-item>
          <div style="display: flex">
            <div style="flex: 1; text-align: left">
              已经有账号：请
              <span
                style="color: rgb(92, 214, 92); cursor: pointer"
                @click="$emit('have-account-login')"
                >登录</span
              >
            </div>
            <div style="flex: 1; text-align: right">忘记密码</div>
          </div>
        </el-form>
      </el-scrollbar>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { RESOLVE_COMPONENT } from "@vue/compiler-core";
import JSEncrypt from 'jsencrypt'
export default {
  data() {
    const confirmValidator = (rule, value, callback)=>{
        if(value == this.user.password){
          callback();
        }
        else{
          callback(new Error("两次输入密码不一致"));
        }
      }

    return {
      user: {
        username: "",
        password: "",
        confirmpassword: "",
        email: "",
        verifycode: "",
      },
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" },
                   { min: 4, max: 20, message:"长度应在4-20", trigger:["blur", "change"]}],
        password: [{ required: true, message: "请输入密码", trigger: "blur" },
                   { min: 4, max: 20, message:"长度应在4-20", trigger:["blur", "change"]},
                   { pattern: /.*[a-zA-z].*/, message:"密码应包含字母", trigger:["blur", "change"]},
                   { pattern: /.*[0-9].*/, message:"密码应包含数字", trigger:["blur", "change"]}], 
        confirmpassword: [{ required:true, message:"请再次输入密码", trigger:"blur"},
                          { validator:confirmValidator, 
                            message:"两次输入密码不一致", trigger:["blur", "change"]}],
        email:[{ required:true, message:"请输入PKU邮箱", trigger:"blur",},
               { pattern: /([0-9a-zA-Z]{1,50})+(@pku.edu.cn|@stu.pku.edu.cn)$/, 
                 message:"PKU邮箱格式错误", trigger:["blur", "change"]
}],
      },
      VerifycodeButtonText:"获取验证码",
      DisableVerifycodeButton:false,
      
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
    EventRegister() {
      let senddata = {
        action: "register",
        username: this.user.username,
        password: this.$getRsaCode(this.user.password),
        email:this.user.email,
        confirm:this.user.confirmpassword,
        verify_code:this.user.verifycode
      };
      console.log(senddata);
      this.$refs.registerRef.validate((valid) => {
        // 表单自身rules的规则检查
        if (valid) {
          axios
            .post("http://127.0.0.1:8000/api/AppUser/", senddata)
            .then((res) => {
              console.log(res);
              if(res.data.status==201){
                alert("注册成功")
                this.$emit('have-account-login');
              }
              else{
                alert("注册失败");
              }
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },
    EventSendVerifyCode(){
      let senddata = {
        action: "send_email",
        email: this.user.email
      }
      console.log(senddata);
      this.$refs.registerRef.validate((valid) => {
        // 表单自身rules的规则检查
        if (valid) {
          axios
            .post("http://127.0.0.1:8000/api/AppUser/", senddata)
            .then((res) => {
              console.log(res);
              alert("验证码发送成功")
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
.registerBox {
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