import {createRouter, createWebHashHistory} from "vue-router"
import Map from './components/Map.vue'
import HelloWorld from './components/HelloWorld.vue'
import Home from './components/Home.vue'
import Lifestyle from './components/Lifestyle.vue'
import Login from './components/Login.vue'

const router=createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:"/Map",
            component: Map
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
            path:"/HellowWorld",
            component: HelloWorld
        },
        {
            path:"/Lifestyle",
            component: Lifestyle
        },
    ]
});

export default router;