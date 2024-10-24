/*
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-09-22
 * @FilePath: /PyramidCoder-demo/src/main.ts
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
 */

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store.js'


import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import ActivityCalendar from "vue-activity-calendar";
import "vue-activity-calendar/style.css"; 
 

import './assets/main.css'
import './assets/global.css'


const app = createApp(App)

app.use(router)
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.use(ActivityCalendar)
app.use(store)

app.mount('#app')
