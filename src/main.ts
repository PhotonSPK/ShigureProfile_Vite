import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import MasonryWall from '@yeger/vue-masonry-wall'


createApp(App).use(MasonryWall).mount('#app')
