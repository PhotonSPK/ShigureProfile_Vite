<script setup lang="ts">
import { ref } from "vue";
import Portrait from './components/Portrait.vue';
import TitleWithSwitch from './components/TitleWithSwitch.vue';
import Gallary from "./components/Gallary.vue";

const avatars = {
  "recruit": "新进干员",
  "combat": "战斗特工",
}

let currentIndex = ref(0);
</script>

<template>
  <div class="container mx-auto my-16 grid grid-cols-1 lg:grid-cols-12 gap-4 ">
    <div class="lg:col-span-4">
      <div class="card">
        <Portrait :avatar="Object.keys(avatars)[currentIndex]" />
        <TitleWithSwitch v-model:currentIndex="currentIndex" :avatars="Object.values(avatars)" />
      </div>
      <div class="card">
        <p>所有图像以 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans" target="_blank">CC-BY-NC-SA
            4.0</a> 方式分享</p>
        <p>禁止 R18G / 违法 / 政治相关二次创作.</p>
        <p>2025 © AkulaQWQ All right reserved.</p>
        <p>Illustrators have their own right.</p>
      </div>
    </div>
    <div class="lg:col-span-8">
      <div class="card">
        <p>身份不明的电波系兽耳少女，自称是超级特工。</p>
        <p>口中经常说着令人费解的话语，时常在各种意想不到的地方出现。</p>
        <p>虽然平时一副不务正业的样子，但是干起正事来比任何人都要努力。 </p>
      </div>
      <div>
        <Gallary />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  margin-bottom: calc(var(--spacing) * 4);
  background-color: oklch(0.274 0.006 286.033);
  border-radius: 0.5rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  transition: all 0.3s;
}
</style>