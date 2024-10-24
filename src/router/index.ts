/*
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2024-08-20
 * @FilePath: /PyramidCoder-demo/src/router/index.ts
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
 */
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root',
      component: HomeView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/demo',
      name: 'demo',
      component: () => import('../views/Demo.vue')
    }
  ]
})

export default router
