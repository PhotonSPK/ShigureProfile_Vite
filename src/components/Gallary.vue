<script setup lang="ts">
import { Fancybox } from "@fancyapps/ui";
import '@fancyapps/ui/dist/fancybox/fancybox.css';
import MasonryWall from "@yeger/vue-masonry-wall";
import { onMounted } from 'vue';
import illustrations from '../illustrations.json';

onMounted(async () => {
    Fancybox.bind('[data-fancybox]', {

    });
})

</script>

<template>
    <Suspense>
        <MasonryWall :items="illustrations" :ssr-columns="1" :column-width="300" :gap="16">
            <template #default="{ item }">
                <img v-if="item.length === 0 && !item.nsfw" class="card" :src="`/imgs/illustrations/${item.illustrator}_${item.date}.avif`" data-fancybox />
                <img v-else-if="item.length === 0 && item.nsfw" class="card blur-sm brightness-50" :src="`/imgs/illustrations/${item.illustrator}_${item.date}.avif`" data-fancybox />
                <div v-else>
                    <div class="card flex">
                        <img v-if="!item.nsfw" :src="`/imgs/illustrations/${item.illustrator}_${item.date}/0.avif`" :data-fancybox="`${item.illustrator}_${item.date}`" />
                        <img v-else class="blur-sm brightness-50" :src="`/imgs/illustrations/${item.illustrator}_${item.date}/0.avif`" :data-fancybox="`${item.illustrator}_${item.date}`" />
                        <div class="no-display">
                            <img v-for="index in item.length-1" :src="`/imgs/illustrations/${item.illustrator}_${item.date}/${index}.avif`" :data-fancybox="`${item.illustrator}_${item.date}`"/>
                        </div>
                    </div>
                </div>
            </template>
        </MasonryWall>
    </Suspense>
</template>

<style scoped>
.card {
    border-radius: 0.5rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.no-display {
    display: none;
}
</style>