<script setup lang="ts">
import { Fancybox } from "@fancyapps/ui";
import '@fancyapps/ui/dist/fancybox/fancybox.css';
import MasonryWall from "@yeger/vue-masonry-wall";
import { onMounted } from 'vue';
import illustrations from '../illustrations.json';

onMounted(async () => {
    console.log(illustrations);
    Fancybox.bind('[data-fancybox]', {

    });
})

</script>

<template>
    <Suspense>
        <MasonryWall :items="illustrations" :ssr-columns="1" :column-width="300" :gap="16">
            <template #default="{ item }">
                <img class="card" :src="`/imgs/illustrations/${item.illustrator}-${item.date}.avif`" data-fancybox />
            </template>
        </MasonryWall>
    </Suspense>
</template>

<style scoped>
.card {
    border-radius: 0.5rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>