<script setup>
import { Avatar, Lock } from '@element-plus/icons-vue'
</script>

<template>
    <div class="loginPage">
        <div class="loginBox">
            <!-- <div style="flex: 1;">
                <img src='..\assets\start_page.jpg' style="width: 100%;height: 100%;">
            </div> -->
            <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
                <el-form :model="user" style="width: 80%;">
                    <div style="font-size: 20px; font-weight: bold; text-align: center;  margin-bottom: 20px;">
                        欢迎登录
                    </div>
                    <el-form-item prop="username">
                        <el-input prefix-icon="Avatar" size="medium" v-model="user.username" placeholder="请输入账号"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input prefix-icon="Lock" size="medium" show-password v-model="user.password" placeholder="请输入密码"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" style="width: 100%;">
                            登录
                        </el-button>
                    </el-form-item>
                    <div style="display: flex">
                        <div style="flex: 1; text-align: left;">还没有账号？请<span style="color: red; cursor: pointer;">注册</span></div>
                        <div style="flex: 1; text-align: right;">忘记密码</div>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                username: '',
                password: ''
            }
        }
    },
    // setup(){
    //     return{
    //         User, Lock
    //     }
    // },

    methods() {

    }


}
</script>

<style>
.loginPage {
    height: 100vh;
    overflow: hidden;

    display: flex;
    align-items: center;
    justify-content: center;

    background-color: aliceblue;
}

.loginBox {
    display: flex;
    background-color: white;
    width: 50%;
    height: 50%;
    border-radius: 5px;
    overflow: hidden;
}
</style>