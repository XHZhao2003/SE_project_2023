<template>
  <div>
    <el-dropdown>
      <el-avatar size="large" style="font-size: 30px;"> {{nameInAvatar}} </el-avatar>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="ExitLogin">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
</template>

<script>
import { ElMessage, ElMessageBox } from "element-plus";

export default {
  data() {
    return {
      username: "",
      nameInAvatar: "User"
    };
  },
  methods: {
    ExitLogin() {
      ElMessageBox.confirm("确认离开当前页面", "退出登录", {
        confirmButtonText: "OK",
        cancelButtonText: "Cancel",
        type: "warning",
        size: 500,
      })
        .then(() => {
          ElMessage({
            type: "success",
            message: "退出登录",
          });
          this.$router.push("/Home");
        })
        .catch(() => {});
    },
  },
  mounted: function(){
    this.username = localStorage.getItem("username")
    if(this.username[0] >= 'a' && this.username[0] <= 'z'){
      this.nameInAvatar = this.username[0].toUpperCase()
    }
    else if(this.username[0] >= 'A' && this.username[0] <= 'Z'){
      this.nameInAvatar = this.username[0]
    }
  }
};
</script>




