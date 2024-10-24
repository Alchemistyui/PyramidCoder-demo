<!-- <script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script> -->

<template>
  <el-container>
    <el-header>
      <el-menu mode="horizontal" active-text-color="#ee827c">

        <el-menu-item index="0" class="logo_router">
          <RouterLink class="router_link" :to="{path:'/', query: {isJan: isJan.toString()}}">
            <img alt="logo" class="logo"
              src="@/assets/imgs/home/pyramidcoder_logo.png" width="260" height="50"
              style="display: flex; align-items: center;" />
          </RouterLink>
        </el-menu-item>

        <!-- <el-menu-item index="1">
          <RouterLink class="router_link" to="/home">Home</RouterLink>
        </el-menu-item> -->
        <el-menu-item index="1">
          <RouterLink class="router_link" to="/demo" :isJan="isJan">Examples</RouterLink>
        </el-menu-item>

        <el-menu-item index="2" >
          <el-button-group class="lang_button">
            <el-button type="primary" @click="setIsJan(false)">Eng</el-button>
            <el-button type="primary" @click="setIsJan(true)">日</el-button>
          </el-button-group>
        </el-menu-item>
      </el-menu>
    </el-header>


    <el-main>
      <RouterView />
    </el-main>


    <el-footer>
      <!-- <el-footer> -->
      <el-divider>
        ˗ˋˏ꒰ঌ ♡ ໒꒱ྀིˎˊ˗
      </el-divider>
      <!-- <el-divider>
       <p style="background-color: #FFFFFB;">asss</p>
      </el-divider> -->
      <p style="font-family: cursive;">
        ❤ Copyright © 2024 Alchemist. All rights reserved. ❤
      </p>
    </el-footer>
  </el-container>
</template>

<script >
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
export default {
  data() {
    return {
      isJan: true
    };
  },
  methods: {
    setIsJan(value) {
      this.isJan = value;
      this.$router.push({ path: '/', query: { isJan: value.toString() } });
    }
  },
  watch: {
    isJan(newVal) {
      this.$router.push({ path: '/', query: { isJan: newVal.toString() } });
    }
  }
}
</script>

<style scoped>
@media (min-width: 1024px) {

  .el-menu {
    background-color: #FFFFFB;
    /* text-align: left; */
    /* font-family: 'Bad Script', cursive; */
    font-size: 1rem;
    margin-top: 1rem;
    width: 100%;
  }

  .el-main {
    /* text-align: left; */
    font-size: 1.2rem;
    margin-top: 1rem;
    /* max-width: 500px; */
    width: 100%;
  }

  .el-container {
    background-color: #FFFFFB;
    /* background-color: #fffffc; */
  }

  .el-footer {
    margin: 2rem auto;
  }

  .el-menu a.router-link-exact-active {
    font-weight: bold;
  }

  .el-menu a.router-link-exact-active:hover {
    background-color: transparent;
    /* background-color: red; */
  }

  .el-menu a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
    /* border-left-color: red; */
    /* #fefefe; */
  }

  .el-menu a:first-of-type {
    border: 0;
  }

  .router_link {
    font-size: 1.5rem;
  }

  .router_link:hover {
    background-color: transparent;
    font-size: 1.5rem;
    /* background-color: red;  */
    /* padding: 5px 20px; */
  }

  .el-menu-item:hover {
    /* outline: 0 !important;   */
    color: #f0908d !important;
    background-color: transparent !important;

  }

  .el-menu--horizontal>.logo_router.is-active {
    border-bottom: 1px solid #FFFFFB;
  }
  .lang_button {
    position: fixed;
    top: 2rem;
    right: 5rem;
    /* padding-top: 1rem;
    padding-left: 63rem; */
  }
}
</style>
