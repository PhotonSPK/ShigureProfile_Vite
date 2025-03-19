import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import MasonryWall from '@yeger/vue-masonry-wall'
import Particles from "@tsparticles/vue3";
import { loadSlim } from "@tsparticles/slim";

createApp(App).use(MasonryWall).use(Particles, {
    init: async engine => {
        await loadSlim(engine);
    },
}).mount('#app')