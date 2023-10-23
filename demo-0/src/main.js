import './assets/main.css'
import router from './router.js'
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/theme-chalk/index.css' 


const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')

// 注册element-plus图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
