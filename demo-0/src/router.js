import {createRouter, createWebHashHistory} from "vue-router"
import Map from './components/Map.vue'
import Login from './components/Login.vue'

const router=createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:"/Map",
            component: Map
        },
        {
            path:"/Login",
            component: Login
        }
    ]
});

export default router;