/*
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-09-22
 * @FilePath: /PyramidCoder-demo/src/store/store.js
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
 */

import { createStore } from 'vuex'

const store = createStore({
  state: {
    username: null
  },
  mutations: {
    setUsername(state, username) {
      state.username = username
    }
  }
})

export default store
