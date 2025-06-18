<template>
    <div class="box">
        <button @click="handleClick">点击我</button>
        <p>{{ text }}</p>
    </div>
</template>
<script setup>
import { ref } from 'vue';

const text = ref('Hello World');

function handleClick() {
    text.value = '你点击了按钮';
}
</script>

<style scoped>
.box {
    border: 1px solid #333;
    padding: 20px;
}
</style>

