<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-08-19
 * @FilePath: /PyramidCoder-demo/src/views/Demo.vue
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
-->

<template>
    <main class="card_view">
        <el-button type="text" @click="dialogVisible = true">{{dialogVisible}}</el-button>

<el-dialog
  title="提示"
  v-model="dialogVisible"
  width="30%"
  :before-close="handleClose">
  <span>这是一段信息</span>
  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
  </span>
</el-dialog>


        <el-row v-for="(page, index) of pages" :key="index">
            <el-col :span="4" v-for="(item, innerindex) of page" :key="item.projectId" :offset="innerindex > 0 ? 2 : 1">
                <el-card :body-style="{ padding: '0px' }">
                    <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                        class="image">
                    <div style="padding: 14px;">
                        <el-button type="text" @click="dialogVisible = true"><span>{{ item.message
                                }}</span></el-button>

                        <el-dialog title="收货地址" v-model="dialogVisible">
                            <span>这是一段信息</span>
                        </el-dialog>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        <!-- 
    <el-row :gutter="0">
      <el-col :span="6"> -->


        <!-- </el-col>
    </el-row>   -->
    </main>

</template>

<script>
export default {
    data() {
        return {
            allprojects: [{ message: 'Foo' }, { message: 'Bar' }],
            dialogVisible: false,
        };
    },
    methods: {
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      }
    },
    computed: {
        pages() {
            const pages = []
            this.allprojects.forEach((item, index) => {
                const page = Math.floor(index / 4)//One line has four items
                if (!pages[page]) {
                    pages[page] = []
                }
                pages[page].push(item)
            })
            return pages
        }
    }
}
</script>

<style>
.el-dialog__wrapper.dialog-fade-leave-active,
.el-message-box__wrapper.msgbox-fade-leave-active {
    transition: none;
}

</style>