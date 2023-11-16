<script setup>
import { Avatar, ElementPlus, Lock } from "@element-plus/icons-vue";
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
          欢迎注册
        </div>
        <el-form-item prop="username">
          <el-input
            prefix-icon="Avatar"
            size="medium"
            v-model="user.username"
            placeholder="请输入账号"
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
            注册
          </el-button>
        </el-form-item>
        <div style="display: flex">
          <div style="flex: 1; text-align: left">
            已经有账号：请
            <span
              style="color: red; cursor: pointer"
              @click="$emit('have-account-login')"
              >登录</span
            >
          </div>
          <div style="flex: 1; text-align: right">忘记密码</div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
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
    EventLogin() {
      let senddata = {
        username: this.user.username,
        password: this.user.password,
      };
      console.log(senddata);
      this.$refs.loginRef.validate((valid) => {
        // 表单自身rules的规则检查
        if (valid) {
          axios
            .post("http://127.0.0.1:8000/api/AppUser/register/", senddata)
            .then((res) => {
              console.log(res);
              this.$router.push("/HellowWorld");
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