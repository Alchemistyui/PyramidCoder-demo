<!-- <template>
    <div class="typing-container">
      <p class="typing-text">
        <span v-for="(char, index) in displayedText" :key="index">{{ char }}</span>
        <span v-if="showCursor" class="cursor">|</span>
      </p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        fullText: "这是 ChatGPT 的打字效果示例。",
        displayedText: "",
        showCursor: true,
        typingSpeed: 100, // typing speed in milliseconds
        thinkingTime: 2000, // time to wait before typing starts
      };
    },
    mounted() {
      this.startTyping();
    },
    methods: {
      startTyping() {
        // simulate thinking time before typing starts
        setTimeout(() => {
          let index = 0;
          const typingInterval = setInterval(() => {
            this.displayedText += this.fullText.charAt(index);
            index++;
            if (index === this.fullText.length) {
              clearInterval(typingInterval);
              this.hideCursor(); // hide cursor after typing is done
            }
          }, this.typingSpeed);
        }, this.thinkingTime);
      },
      hideCursor() {
        setTimeout(() => {
          this.showCursor = false;
        }, 200); 
      },
    },
  };
  </script>
  
  <style scoped>
  .typing-container {
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    background-color: aliceblue;
    width: 10%;
    border-radius: 5px;
  }
  
  .typing-text {
    display: inline;
  }
  
  .cursor {
    display: inline-block;
    font-size: 20px;
    font-weight: bold;
    position: relative;
    animation: blink 1s step-end infinite;
  }
  
  @keyframes blink {
    from, to {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
  }
  </style>
   -->

   <template>
    <div class="typing-container">
      <p class="typing-text">
        <span v-for="(char, index) in displayedText" :key="index">{{ char }}</span>
        <span v-if="showCursor" class="cursor">|</span>
      </p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      fullText: {
        type: String,
        required: true
      },
      typingSpeed: {
        type: Number,
        default: 100 // Default typing speed in milliseconds
      },
      thinkingTime: {
        type: Number,
        default: 2000 // Default thinking time in milliseconds
      }
    },
    data() {
      return {
        displayedText: "",
        showCursor: true,
      };
    },
    mounted() {
      if (this.fullText) {
        this.startTyping();
      } else {
        console.error('fullText prop is not provided or is empty.');
      }
    },
    methods: {
      startTyping() {
        setTimeout(() => {
          let index = 0;
          const typingInterval = setInterval(() => {
            if (this.fullText && index < this.fullText.length) {
              this.displayedText += this.fullText.charAt(index);
              index++;
            } else {
              clearInterval(typingInterval);
              this.hideCursor();
            }
          }, this.typingSpeed);
        }, this.thinkingTime);
      },
      hideCursor() {
        setTimeout(() => {
          this.showCursor = false;
        }, 500);
      },
    },
  };
  </script>
  
  <style scoped>
  .typing-container {
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    background-color: aliceblue;
    width: 80%;
    border-radius: 5px;
  }
  
  .typing-text {
    display: inline;
  }
  
  .cursor {
    display: inline-block;
    font-size: 20px;
    font-weight: bold;
    position: relative;
    animation: blink 1s step-end infinite;
  }
  
  @keyframes blink {
    from, to {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
  }
  </style>
  
  