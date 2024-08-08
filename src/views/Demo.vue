<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-08-08
 * @FilePath: /PyramidCoder-demo/src/views/Demo.vue
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
-->

<template>
<main class="card_view">
    <el-row :gutter="0">
      <el-col :span="6">

        <el-card :body-style="{ padding: '0px' }">
      <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
      <div style="padding: 14px;">
        <el-button type="text" class="button"><span>好吃的汉堡</span></el-button>
      </div>
    </el-card>

      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card1.png" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_letter.png" />
          <span style="margin-top: 10em;">Whisper</span>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card2.png" />
        </el-card>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card3.png" />
        </el-card>
      </el-col>

      <el-col :span="6">
  <el-card shadow="hover" class="card_link" >
    <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_lock.png" />
    <span style="text-align: center;">Secret World</span>
  </el-card>
</el-col>


    <el-col :span="6">
      <el-card shadow="hover" :body-style="{ padding: '0px' }">
        <img class="card_img" src="../assets/imgs/home_card/card5.png" />
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_diamond.png" />
          <span style="margin-top: 10em;">Wish List</span>
        </el-card>
    </el-col>
  </el-row>
  
  </main> 

</template>

<style scoped>

</style>