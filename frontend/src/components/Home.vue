<template>
  <div style="width: 100%; height: auto;">
    <el-carousel :interval="3000" height="810px">
      <el-carousel-item v-for="item in imgList" :key="item.id" height="810px">
        <img :src="item.idView" style="width: 100%; height: 100%;">
      </el-carousel-item>
    </el-carousel>
  </div>

  <div id="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect" style="background-color: aliceblue; height: 100%;">
      <el-menu-item index="0" style="margin: 0px; padding: 0px;">
        <img style="height: 100%; object-fit: contain;" src="../assets/ERoad-logo.png">
      </el-menu-item>
      <div style="display: flex; flex-direction: row; flex-grow: 1; justify-content: flex-end;">
        <el-menu-item index="1" id="login_register" @click="switchToLogin">登录</el-menu-item>
        <el-menu-item index="2" id="login_register" @click="switchToRegister">注册</el-menu-item>
      </div>
    </el-menu>
  </div>

  <Login v-if="ShowLogin" id="login" @no-account-register="switchToRegister" />
  <Register v-else-if="ShowRegister" id="register" @have-account-login="switchToLogin" />

</template>

<script>
import { ref } from "vue";
import Login from "./Login.vue";
import Register from "./Register.vue";

export default {
  name: "index",
  data() {
    return {
      imgList: [
        { id: 0, idView: "/corousel1.jpg" },
        { id: 1, idView: "/corousel2.jpg" },
        { id: 2, idView: "/corousel3.jpg" },
        { id: 3, idView: "/corousel4.jpg" },
      ],
      ShowLogin: false,
      ShowRegister: false,
    };
  },
  methods: {
    switchToLogin() {
      this.ShowLogin = true;
      this.ShowRegister = false;
    },
    switchToRegister() {
      this.ShowLogin = false;
      this.ShowRegister = true;
    },
  },
  components: {
    Login,
    Register,
  },
};

const activeIndex = ref("1");
const handleSelect = (key, keyPath) => {
  console.log(key, keyPath);
};
</script>
<style>
#header {
  position: absolute;
  top: 0%;
  left: 5px;
  width: 100%;
  height: 100px;
  z-index: 1;
  margin: 0px;
  padding: 0px;
}
#login_register {
  height: 100%;
  width: 10%;
  font-size: 28px;
}
#login {
  position: absolute;
  left: 35%;
  top: 20%;
}
#register {
  position: absolute;
  left: 35%;
  top: 20%;
}
</style>
