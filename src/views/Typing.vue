<template>
    <div class="typing-container">
      <p class="typing-text">
        <span v-for="(char, index) in displayedText" :key="index" class="sentence">{{ char }}</span>
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
              this.notifyTypingComplete(); // 通知父组件打字完成
            }
          }, this.typingSpeed);
        }, this.thinkingTime);
      },
      hideCursor() {
        setTimeout(() => {
          this.showCursor = false;
        }, 500);
      },
      notifyTypingComplete() {
        this.$emit('typingComplete');
      }
    },
  };
  </script>
  
  <style scoped>
  .typing-container {
    font-family: 'Courier New', Courier, monospace;
    font-size: 16px;
    background-color: aliceblue;
    /* width: 80%; */
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

.sentence {
    white-space: pre-wrap;
  }

  </style>
  