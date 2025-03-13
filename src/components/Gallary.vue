<script setup lang="ts">
import MasonryWall from '@yeger/vue-masonry-wall'
import { Fancybox } from "@fancyapps/ui";
import '@fancyapps/ui/dist/fancybox/fancybox.css';
import illustrations from '../assets/illustrations.json'
import { onMounted } from 'vue';

console.log(illustrations)
onMounted(() => {
    Fancybox.bind('[data-fancybox]', {

    });
})

</script>

<template>
    <MasonryWall :items="illustrations" :ssr-columns="1" :column-width="200" :gap="16">
        <template #default="{ item }">
            <img data-fancybox :src="`/imgs/${item.illustrator}_${item.date}.png`" class="card" />
        </template>
    </MasonryWall>
</template>

<style scoped>
.card {
    border-radius: 0.5rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>