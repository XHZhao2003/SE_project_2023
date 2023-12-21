import './assets/main.css'
import router from './router.js'
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/theme-chalk/index.css' 
import axios from 'axios'

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
app.config.globalProperties.SERVER = "http://8.140.199.201:10001"


// axios.defaults.xsrfCookieName = 'csrfmiddlewaretoken'
// axios.defaults.xsrfHeaderName = 'X-XSRF-TOKEN'
// axios.defaults.withCredentials = true
// axios.get('api/AppUser',{withCredentials: true})
//         .then((response) => {
//           axios.defaults.headers['X-CSRFToken'] = getCsfrKey()
//           console.log(axios.defaults.headers['X-CSRFToken'])
//         })


// 注册element-plus图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

