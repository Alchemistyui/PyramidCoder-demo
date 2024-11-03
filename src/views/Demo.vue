<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2024-10-24
 * @FilePath: /PyramidCoder-demo-main/src/views/Demo.vue
 * @Description: 
 * 
 * Copyright (c) 2024, All Rights Reserved. 
-->

<template>
    <main class="card_view">

        <el-row v-for="(page, index) of pages" :key="index" type="flex" justify="center">
            <el-col :span="8" v-for="(item, innerindex) of page" :key="item.projectId">
                <el-card shadow="hover" class="example_card">
                    <div v-for="(image, imageIndex) in item.image" :key="imageIndex" class="image-container">
                        <img :src="'data:image/png;base64,' + image" class="example_image">
                    </div>
                    <div>

                        <p>{{ item.question }}</p>
                        <p>(日本語: {{ item.ja_question }})</p>
                        <el-button @click="item.dialogVisible = true; this.questionTypingVisible = true">Try this</el-button>
                        <!-- <el-button type="text" @click="item.dialogVisible = true"><p>{{ item.question }}</p>
                            <br /><p>(日本語: {{ item.ja_question }})</p>
                        </el-button> -->
                    </div>
                    <el-dialog title="PyramidCoder Generation" v-model="item.dialogVisible" :before-close="handleDialogClose">
                        <!-- <el-button type="text" @click="showDialog(item.projectId)"><span>{{ item.question }}</span></el-button>
                        
                        <el-dialog :title="'PyramidCoder Generation - ' + item.projectId" :visible.sync="dialogVisible[item.projectId]"> -->
                        <h2 v-if="isJan">Input Image(s)</h2>
                        <h2 v-else>入力画像</h2>
                        <div v-for="(image, imageIndex) in item.image" :key="imageIndex" class="image-container">
                            <img :src="'data:image/png;base64,' + image" class="example_image">
                        </div>
                        <h2 v-if="isJan">Input Question</h2>
                        <h2 v-else>入力質問</h2>
                        <p>{{ item.question }}</p>
                        <p>(日本語: {{ item.ja_question }})</p>

                        <img class="card_img" src="@/assets/imgs/examples/pink_arrow.png"
                            style="width: 5%; margin: 0 auto;" />

                        <h2 v-if="isJan">Question Rephrasing</h2>
                        <h2 v-else>質問の言い換え</h2>
                        <Typing v-if="questionTypingVisible" :fullText="getRandomCode(item.queries)" :typingSpeed="30" :thinkingTime="1000"
                            @typing-complete="QuestionTypingComplete" />
                        <div v-if="showCodeDiv">
                            <h2 v-if="isJan">Code generation</h2>
                            <h2 v-else>コード生成</h2>
                            <Typing v-if="codeTypingVisible" :fullText="getRandomCode(item.codes)" :typingSpeed="30"
                                :thinkingTime="3200" @typing-complete="CodeTypingComplete" />
                        </div>
                        <div v-if="showAnswerDiv">
                            <h2 v-if="isJan">Code execution</h2>
                            <h2 v-else>コード実行</h2>
                            <img v-if="!showAnswer" src="@/assets/imgs/examples/loading.gif"
                                style="width: 3%; margin: 0 auto;" />
                            <!-- <p v-else>{{ item.answer }}</p> -->
                            <div v-else>
                                <p v-if="isJan">Answer: {{ item.answer }}</p>
                                <p v-else>答え: {{ item.answer }}</p>
                                <p v-if="isJan">Correct Answer: {{ item.answer }}</p>
                                <p v-else>正解: {{ item.answer }}</p>
                                
                            </div>

                            <!-- <Typing v-if="codeTypingVisible" :fullText="getRandomCode(item.codes)" :typingSpeed="100" :thinkingTime="3000" /> -->
                        </div>

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
import { nextTick } from 'vue';
// import { reactive, toRefs } from 'vue';

export default {
    components: {
        Typing
    },
    data() {
        return {
            examples: [],
            showCodeDiv: false,
            codeTypingVisible: false,
            showAnswerDiv: false,
            showAnswer: false,
            questionTypingVisible: false,
            dialogVisible: {}
        };
    },
    methods: {
        getRandomCode(codes) {
            if (Array.isArray(codes) && codes.length > 0) {
                const randomIndex = Math.floor(Math.random() * codes.length);
                // console.log(codes[randomIndex]);
                return codes[randomIndex];
            } else {
                return ''; // Return an empty string or a default value if the list is empty
            }
        },
        QuestionTypingComplete() {
            this.showCodeDiv = true; // Show the hidden div when typing is complete
            nextTick(() => {
                this.codeTypingVisible = true;
            });
        },
        CodeTypingComplete() {
            this.showAnswerDiv = true; // Show the hidden div when typing is complete
            // Delay for 2 seconds before showing the answer
            setTimeout(() => {
                this.showAnswer = true;
            }, 3000);
        },
        handleDialogClose(done) {
            this.showCodeDiv = false;
            this.codeTypingVisible = false;
            this.showAnswerDiv = false;
            this.showAnswer = false;
            this.questionTypingVisible = false;
            done();
        }
    },
    computed: {
        pages() {
            const pages = []
            this.examples.forEach((item, index) => {
                const page = Math.floor(index / 3)//One line has four items
                if (!pages[page]) {
                    pages[page] = []
                }
                pages[page].push(item)
            })
            return pages
        },
        isJan() {
            return this.$route.query.isJan === 'true'; // Ensure it is evaluated as a boolean
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