<template>
  <div>
    <el-dropdown>
      <el-avatar size="large"> User </el-avatar>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="ExitLogin">Action 1</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
</template>

<script>
import { ElMessage, ElMessageBox } from "element-plus";

export default {
  data() {
    return {};
  },
  methods: {
    ExitLogin() {
      ElMessageBox.confirm(
        "确认离开当前页面",
        "退出登录",
        {
          confirmButtonText: "OK",
          cancelButtonText: "Cancel",
          type: "warning",
          size: 500
        }
      )
        .then(() => {
          ElMessage({
            type: "success",
            message: "退出登录",
          });
          this.$router.push('/Home')
        })
        .catch(() => {});
    },
  },
};
</script>



