import {createRouter, createWebHashHistory} from "vue-router"
import Map from './components/Map.vue'

const router=createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:"/Map",
            component: Map
        }
    ]
});

export default router;