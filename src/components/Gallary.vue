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
        <MasonryWall :items="illustrations" :column-width="200" :gap="16">
            <template #default="{ item }">
                <img v-if="item.length === 0 && !item.nsfw" class="card"
                    :src="`/imgs/illustrations/${item.illustrator}_${item.date}.avif`" data-fancybox />
                <a v-else-if="item.length === 0 && item.nsfw" data-fancybox
                    :data-src="`/imgs/illustrations/${item.illustrator}_${item.date}.avif`">
                    <div class="relative">
                        <img class="card" :src="`/imgs/illustrations/${item.illustrator}_${item.date}.avif`" />
                        <div
                            class="card absolute backdrop-blur-sm backdrop-brightness-50 inset-0 flex items-center justify-center">
                            <img class="" src="/src/assets/nsfw.avif" />
                        </div>
                    </div>
                </a>
                <a v-else class="card" :data-src="`/imgs/illustrations/${item.illustrator}_${item.date}/00.avif`"
                    :data-fancybox="`${item.illustrator}_${item.date}`">
                    <img v-if="!item.nsfw" :src="`/imgs/illustrations/${item.illustrator}_${item.date}/00.avif`"
                        :data-fancybox="`${item.illustrator}_${item.date}`" />
                    <div v-else class="relative">
                        <img class="card" :src="`/imgs/illustrations/${item.illustrator}_${item.date}/00.avif`" />
                        <div
                            class="card absolute backdrop-blur-sm backdrop-brightness-50 inset-0 flex items-center justify-center">
                            <img class="" src="/src/assets/nsfw.avif" />
                        </div>
                    </div>
                    <div class="no-display">
                        <img v-for="index in item.length - 1"
                            :src="`/imgs/illustrations/${item.illustrator}_${item.date}/${index.toString().padStart(2, '0')}.avif`"
                            :data-fancybox="`${item.illustrator}_${item.date}`" />
                    </div>
                </a>
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