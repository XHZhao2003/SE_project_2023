import {createRouter, createWebHashHistory} from "vue-router"
import Map from './components/Map.vue'
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue'

const router=createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:"/Map",
            component: Map,
            meta:{
                loginFlag: "true"
            }
        },
        {
            path:"/Home",
            component: Home
        },
        {
            path:"/",
            component: Home
        },
        {
            path:"/HelloWorld",
            component: HelloWorld,
            meta:{
                loginFlag:"true"
            }
        }
    ]
});

router.beforeEach((to, from, next)=>{
    if(to.meta.loginFlag == "true"){
        // 需要登录状态的页面
        if(localStorage.getItem("loginFlag") == "true"){
            next()
        }
        else{
            alert("请登录以使用服务")
            next('/')
        }
    }
    else{
        var loginFlag = localStorage.getItem("loginFlag")
        if(loginFlag == "true"){
            if(from.path == '/Map'){
                localStorage.setItem("loginFlag", "false")
                localStorage.setItem("userName", "")
                next()
            }
            else{
                console.log("登录状态下自动跳转")
                next('/Map')
            }
        }
        else{
            next()
        }
    }
})

export default router;