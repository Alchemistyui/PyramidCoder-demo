<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-08-20
 * @FilePath: /PyramidCoder-demo/src/views/Demo.vue
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
-->

<template>
    <main class="card_view">
        <!-- <el-button type="text" @click="dialogVisible = true">{{dialogVisible}}</el-button> -->

        <!-- <el-dialog title="提示" v-model="dialogVisible" width="30%" :before-close="handleClose">
            <span>这是一段信息</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </el-dialog> -->


        <el-row v-for="(page, index) of pages" :key="index" type="flex" justify="center">
            <el-col :span="6" v-for="(item, innerindex) of page" :key="item.projectId">
                <el-card shadow="hover" class="example_card">
                    <div v-for="(image, imageIndex) in item.image" :key="imageIndex" class="image-container">
                        <img :src="'data:image/png;base64,' + image" class="example_image">
                    </div>
                    <div>
                        
                        <p>{{ item.question }}</p>
                        <p>(日本語: {{ item.ja_question }})</p>
                        <el-button @click="item.dialogVisible = true">Try this</el-button>
                        <!-- <el-button type="text" @click="item.dialogVisible = true"><p>{{ item.question }}</p>
                            <br /><p>(日本語: {{ item.ja_question }})</p>
                        </el-button> -->
                    </div>
                        <el-dialog title="PyramidCoder Generation" v-model="item.dialogVisible">
                            <!-- <el-button type="text" @click="showDialog(item.projectId)"><span>{{ item.question }}</span></el-button>
                        
                        <el-dialog :title="'PyramidCoder Generation - ' + item.projectId" :visible.sync="dialogVisible[item.projectId]"> -->
                            <h2>Input Image(s)</h2>
                            <div v-for="(image, imageIndex) in item.image" :key="imageIndex" class="image-container">
                                <img :src="'data:image/png;base64,' + image" class="example_image">
                            </div>
                            <h2>Input Question</h2>
                            <p>{{ item.question }}</p>
                            <p>(日本語: {{ item.ja_question }})</p>

                            <img class="card_img" src="@/assets/imgs/examples/pink_arrow.png" style="width: 5%; margin: 0 auto;" />

                            <h2>Question Rephrasing</h2>
                            <Typing :fullText="getRandomCode(item.queries)" :typingSpeed="50" :thinkingTime="1000" />
                            <h2>Code generation</h2>
                            <Typing :fullText="getRandomCode(item.codes)" :typingSpeed="100" :thinkingTime="4000" />
                            <!-- <img class="card_img" src="@/assets/imgs/examples/loading.gif" style="width: 5%; margin: 0 auto;" /> -->
                        </el-dialog>
                </el-card>
            </el-col>
        </el-row>
    </main>

</template>

<script>
import axios from "axios";
import Typing from './Typing.vue';
import { API_BASE_URL } from '@/config.js';
// import { reactive, toRefs } from 'vue';

export default {
    components: {
        Typing
    },
    data() {
        return {
            examples: [],
            dialogVisible: {}
        };
    },
    methods: {
        getRandomCode(codes) {
            if (Array.isArray(codes) && codes.length > 0) {
                const randomIndex = Math.floor(Math.random() * codes.length);
                return codes[randomIndex];
            } else {
                return ''; // Return an empty string or a default value if the list is empty
            }
        },
    },
    computed: {
        pages() {
            const pages = []
            this.examples.forEach((item, index) => {
                const page = Math.floor(index / 4)//One line has four items
                if (!pages[page]) {
                    pages[page] = []
                }
                pages[page].push(item)
            })
            return pages
        }
    },
    created() {
        axios.get(`${API_BASE_URL}/get_examples`, {
            headers: { 'Content-Type': 'application/json' },
            params: {},
        })
            .then((response) => {
                this.examples = response.data;
                // console.log(this.examples);
            })
            .catch((error) => {
                console.error(error);
            });
    }
}
</script>

<style>

.el-card {
    type: 'flex';
    justify: 'center';
}

.image-container {
    display: inline-block;
}

.example_image {
    width: 100%;
    /* height: 200px; */
    height: 8rem;
    object-fit: contain;
    padding: 0 5px;
}


.el-card__body {
    padding: 1rem;
}
</style>