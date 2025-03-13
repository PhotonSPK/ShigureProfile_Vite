<script setup lang="ts">
// const avatars = ["114514", "1919810"];
const { avatars } = defineProps<{ avatars: string[] }>();
const currentIndex = defineModel('currentIndex', { type: Number, required: true });
function switchAvatar(direction: number) {
    currentIndex.value = (currentIndex.value + direction + avatars.length) % avatars.length;
}
</script>

<template>
    <div class="flex justify-between items-center bg-primary">
        <button class="p-4" v-on:click="switchAvatar(-1)">
            L
        </button>
        <div class="text-center font-bold shrink-0">
            <h1 class="text-2xl">
                雪野時雨
            </h1>
            <h2 class="text-lg">
                {{ avatars[currentIndex] }}
            </h2>
        </div>
        <button class="p-4" v-on:click="switchAvatar(1)">
            R
        </button>
    </div>
</template>

<style scoped>
button {
    background-color: #6495ED;
    cursor: pointer;
    font-size: 1.5rem;
    transition: all 200ms;
}

button:hover {
    background-color: #4169E1;
}

button:active {
    background-color: #1E90FF;
}
</style>