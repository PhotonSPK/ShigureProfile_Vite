<script setup lang="ts">
import { onMounted, ref } from "vue";
import TransitionableImage from "./components/TransitionableImage.vue";
import TitleWithSwitch from './components/TitleWithSwitch.vue';
import Gallary from "./components/Gallary.vue";
import Twikoo from "./components/Twikoo.vue";

const counterUrl = 'https://count.akula.moe/akula:shigure?theme=rule34';
const svgContent = ref('');
const avatars = {
  "airborne": "空降精英",
  "combat": "战斗特工",
  "recruit": "新进干员",
}

let currentIndex = ref(0);
Object.keys(avatars).forEach((key) => {
  const img = new Image();
  img.src = `https://img.akula.moe/portraits/shigure_${key}.avif`;
  img.src = `https://img.akula.moe/composes/shigure_${key}_compose.avif`;
});

onMounted(async () => {
  svgContent.value = await fetch(counterUrl).then((res) => res.text());
});
</script>

<template>
  <vue-particles id="tsparticles" url="/particles.json" />
  <div class="container mx-auto my-16 grid grid-cols-1 lg:grid-cols-12 gap-4 ">
    <div class="lg:col-span-4">
      <div class="card">
        <TransitionableImage :refKey="ref(Object.keys(avatars)[currentIndex]).value"
          :path="`https://img.akula.moe/portraits/shigure_${Object.keys(avatars)[currentIndex]}.avif`" />
        <TitleWithSwitch v-model:currentIndex="currentIndex" :avatars="Object.values(avatars)" />
        <div>

        </div>
        <div class="leading-8 text-center bg-primary">
          <p>身份不明的电波系兽耳少女，自称是超级特工。</p>
          <p>口中经常说着令人费解的话，时常在意想不到的地方出现。</p>
          <p>虽然平时不务正业的样子，但是干起正事来比任何人都要努力。 </p>
        </div>
      </div>
      <div class="card text-center">
        <p>一代目画师: <a href="https://www.mihuashi.com/profiles/1446956/" target="_blank">Byx</a></p>
        <p>二代目画师: <a href="https://www.mihuashi.com/profiles/1182712/" target="_blank">瓜兮兮的～</a></p>
        <p>三代目画师: <a href="https://www.mihuashi.com/profiles/1857409/" target="_blank">Dorgar-渔刀</a></p>
      </div>
      <div class="card text-center">
        <p>所有图像以 <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans" target="_blank">CC-BY-NC-SA
            4.0</a> 方式分享</p>
        <p>禁止 R18G / 违法 / 政治相关二次创作.</p>
        <p>禁止用于 AI 训练.</p>
        <p>2025 © Akula Arius. All right reserved.</p>
        <p>Illustrators have their own right.</p>
        <footer>
          <a href=" https://icp.gov.moe/?keyword=20247460" target="_blank">萌ICP备20247460号</a>
          <span style="color: transparent;">Nobody loves me :(</span>
        </footer>
      </div>
      <div class="card flex justify-center">
        <Suspense>
          <div v-html="svgContent"></div>
        </Suspense>
      </div>
      <div class="card">
        <Twikoo />
      </div>
    </div>
    <div class="lg:col-span-8">
      <div class="card">
        <TransitionableImage :refKey="ref(Object.keys(avatars)[currentIndex]).value"
          :path="`https://img.akula.moe/composes/shigure_${Object.keys(avatars)[currentIndex]}_compose.avif`" />
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
