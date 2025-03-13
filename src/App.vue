<script setup lang="ts">
import { ref } from "vue";
import Portrait from './components/Portrait.vue';
import TitleWithSwitch from './components/TitleWithSwitch.vue';

const avatars = {
  "recruit": "新进干员",
  "combat": "战斗特工",
}

let currentIndex = ref(0);
</script>

<template>
  <div class="container mx-auto mt-16 grid grid-cols-1 lg:grid-cols-12 gap-4 ">
    <div class="card lg:col-span-4">
      <Portrait :avatar="Object.keys(avatars)[currentIndex]" />
      <TitleWithSwitch v-model:currentIndex="currentIndex" :avatars="Object.values(avatars)" />
    </div>
    <div class="card lg:col-span-8">
      1919810
    </div>
  </div>
</template>

<style scoped>
.card {
  background-color: oklch(0.274 0.006 286.033);
  border-radius: 0.5rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  transition: all 0.3s;
}
</style>