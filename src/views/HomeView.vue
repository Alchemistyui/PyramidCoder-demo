
<template>

  <div class="vqa_intro ja" v-if="isJan">
    <h1>視覚的質問応答 Visual Question Answering (VQA)</h1>
    <p> 視覚的質問応答とは、画像や動画などの視覚情報に基づいて、自然言語の質問に対して正確な答えを提供するタスクです。</p>
    <img class="card_img" src="@/assets/imgs/home/vqa_task.png" style="width: 50%; margin: 0 auto;" />

    <h1>プログラムによる視覚的な質問回答 (Programmatic VQA)</h1>
    <p> プログラム的視覚的質問応答（PVQA）とは、画像や動画に関する質問に対して、コードを生成して答える方法です。これにより、複雑な視覚的推論が必要な質問にも対応できるようになります。 <br>
    <ul>
      <li>大規模言語モデル (LLM) を利用して、入力された質問をステップに分解するコードを生成します。</li>
      <li>生成されたコードは、画像処理モジュールと基本的な Python 関数を呼び出します。</li>
      <li>明示的なコード実行プロセスにより、モデルの推論に関する洞察が得られます。</li>
    </ul>
    <img class="card_img" src="@/assets/imgs/home/pvqa_model.png" style="width: 60%; margin: 0 auto;" />
    </p>
  </div>

  <div class="vqa_intro en" v-else>
    <h1>Visual Question Answering (VQA)</h1>
    <p> General visual-language task which integrates the understanding of text and image information.</p>
    <ul>
      <li>Inputs: an image/video + its corresponding question</li>
      <li>Output: the answer to the question</li>
    </ul>
    <img class="card_img" src="@/assets/imgs/home/vqa_task.png" style="width: 50%; margin: 0 auto;" />

    <h1>Programmatic VQA</h1>
    <p> Programmatic Visual Question Answering (PVQA) is a method of generating programs or code to answer questions about images, allowing the model to answer questions that require complex visual reasoning. <br>
    <ul>
      <li>Utilize large language models (LLMs) to generate code that breaks down the input question into steps.</li>
      <li>The generated code invokes image processing modules and basic Python functions.</li>
      <li>The explicit code execution process provides insights into the model's reasoning.</li>
    </ul>
    <img class="card_img" src="@/assets/imgs/home/pvqa_model.png" style="width: 60%; margin: 0 auto;" />
    </p>
  </div>

  <div class="motivation ja" v-if="isJan">
    <h1>問題点と動機</h1>
    <p>
      LLMのプロンプトとは、大規模言語モデル（LLM）に対して特定の応答を生成させるために入力する指示や質問のことです。プロンプトを使うことで、LLMは与えられた文脈に基づいてテキストを生成し、質問に答えたり、特定のタスクを実行したりすることができます。
    </p>
    <h3>問題点</h3>
    <p>既存のPVQAモデルで使用されるプロンプト(IO prompting)は簡単すぎます。
    <ul>
      <li>そのため、LLMからドメイン特有の知識を引き出せず、シンプルで類似したコードしか生成できません。</li>
      <li>また、生成されるコードが1つだけで、質問に対する複数の解決策をうまく活用できていません。</li>
    </ul>
    </p>

    <h3>動機</h3>
    <p>より複雑な質問に対応するために、PVQAのプロンプトを改善し、多様な解決策の探索して複数のコードを生成することで、PVQAモデルの性能を向上させます。</p>
    <img class="card_img" src="@/assets/imgs/home/motivation.png" style="width: 60%; margin: 0 auto;" />
  </div>

  <div class="motivation en" v-else>
    <h1>Problem and Motivation</h1>
    <p>
      A prompt for an LLM refers to instructions or questions inputted to a large language model (LLM) to generate specific responses. By using prompts, the LLM can generate text based on the given context, answer questions, or perform specific tasks.
    </p>
    <h3>Current Problem</h3>
    <p>The prompts used in existing PVQA models are too simplistic. 
    <ul>
      <li>Struggles to elicit domain-specific knowledge from LLMs, resulting in unclear or overly simplistic code.</li>
      <li>Generates only one code solution and does not leverage multiple potential solutions to the question.</li>
    </ul>
    </p>

    <h3>Motivation</h3>
    <p>To handle more complex questions, we aim to improve PVQA prompts and explore diverse solutions by generating multiple codes, thereby enhancing the performance of PVQA models.</p>
    <img class="card_img" src="@/assets/imgs/home/motivation.png" style="width: 60%; margin: 0 auto;" />
  </div>


  <div class="model_gif ja" v-if="isJan">
    <h1>提案手法 - PyramidCoder</h1>
    <p> PVQAのコード生成プロンプト手法であり、3 つのモジュールからなる階層フレームワークです。 <br>
    <ol>
      <li style="color: #1C9D51;">入力質問の意味を保持したまま、多様な表現に言い換えて、複数の表現を生成します。</li>
      <li style="color: #0E70BC;">複数のコードを生成し、質問に関連する潜在的な解決策を最大限に活用します。</li>
      <li style="color: #F5BB39;">最終的な答えはコードを実行した後の答えの頻度と、答えと質問の意味的な一貫性に基づいてを選択されます。</li>
    </ol>
    <img class="card_img" src="@/assets/imgs/home/pyramidcoder_gif.gif" style="width: 70%; margin: 0 auto;" />
    </p>
  </div>

  <div class="model_gif en" v-else>
    <h1>Proposed Method  - PyramidCoder</h1>
    <p> A PVQA code generation prompting method consisting of a hierarchical framework with three modules. <br>
    <ol>
      <li style="color: #1C9D51;">Rephrase the input question into various expressions while preserving its meaning, generating multiple variations.</li>
      <li style="color: #0E70BC;">Generate multiple codes to maximize the potential solutions related to the question.</li>
      <li style="color: #F5BB39;">The final answer is selected based on the frequency of answers and the semantic consistency between the answers and the question after executing the codes.</li>
    </ol>
    <img class="card_img" src="@/assets/imgs/home/pyramidcoder_gif.gif" style="width: 70%; margin: 0 auto;" />
    </p>
  </div>



</template>


<script>
export default {
  data() {
    return {
      refreshkey: 0 // Assuming refreshkey is used for something else in your component
    };
  },
  computed: {
    isJan() {
      return this.$route.query.isJan === 'true'; // Ensure it is evaluated as a boolean
    }
  },
  watch: {
    '$route.query.isJan': function(newVal) {
      console.log(newVal); // Logging the new value
      this.refreshkey++; // If you need to trigger refreshkey on route change
    }
  }
};
</script>

<style scoped>
.item {
  padding: 18px 0;
}

.card_img {
  max-width: 100%;
  max-height: 100%;
  display: block;
  display: flex;
  align-items: center;
}
</style>
