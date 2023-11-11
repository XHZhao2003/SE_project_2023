import {createRouter, createWebHashHistory} from "vue-router"
import Map from './components/Map.vue'
import Home from './components/Home.vue'
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
        }
    ]
});

export default router;