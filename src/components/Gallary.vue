<script setup lang="ts">
import { Fancybox } from "@fancyapps/ui";
import '@fancyapps/ui/dist/fancybox/fancybox.css';
import MasonryWall from "@yeger/vue-masonry-wall";
import illustrations from '../illustrations.json';
import illustrators from '../illustrators.json';
import { onMounted, onUnmounted, onUpdated } from "vue";

interface Illustrators {
    [key: string]: {
        [key: string]: string;
    };
}

const illustratorsTyped: Illustrators = illustrators;

interface Illustration {
    illustrator: string;
    date: string;
}

function makePath(item: Illustration, index: number = -1): string {
    if (index >= 0)
        return `https://img.akula.moe/illustrations/${item.illustrator}_${item.date}/${index.toString().padStart(2, '0')}.avif`;
    else
        return `https://img.akula.moe/illustrations/${item.illustrator}_${item.date}.avif`;

}

function makeIllustratorContact(item: Illustration): HTMLElement {
    const contact: Record<string, string> = illustratorsTyped[item.illustrator];
    const div = document.createElement('div');
    div.classList.add('flex', 'gap-2');
    for (const key in contact) {
        const a = document.createElement('a');
        a.href = contact[key];
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        a.textContent = key;
        div.appendChild(a);
    }

    return div;
}

const fancyBoxOption: Object = {
    compact: false,
    idle: false,
    dragToClose: true,
    commonCaption: true,
    showClass: 'f-fadeIn',
    Toolbar: {
        absolute: true,
        display: {
            left: [],
            middle: [],
            right: ['close', 'download', 'fullscreen'],
        },
    },
    tpl: {
        main: `<div class="fancybox__container has-sidebar" role="dialog" aria-modal="true" aria-label="{{MODAL}}" tabindex="-1">
                <div class="fancybox__backdrop"></div>
                <div class="fancybox__cols">
                <div class="fancybox__col">
                    <div class="fancybox__carousel"></div>
                    <div class="fancybox__footer"></div>
                </div>
                <div class="fancybox__col">
                    <div id="fancybox_content" class="fancybox__data">
                        <br />
                    </div>
                </div>
                </div>
            </div>`
    },
    on: {
        'Carousel.ready Carousel.change': (fancybox: Fancybox) => {
            const contentVal = fancybox!.getSlide()!.triggerEl!.dataset.content;
            const contentEl = document.getElementById('fancybox_content');

            if (contentEl) {
                contentEl.innerHTML = contentVal || '';
            }
        },
    },
}

onMounted(() => {
    Fancybox.bind('[data-fancybox]', fancyBoxOption);
});

onUpdated(() => {
    Fancybox.unbind('[data-fancybox]');
    Fancybox.close();
    Fancybox.bind('[data-fancybox]', fancyBoxOption);
})

onUnmounted(() => {
    Fancybox.destroy();
});

</script>

<template>
    <MasonryWall :items="illustrations" :column-width="200" :gap="16">
        <template #default="{ item }">
            <!-- single image -->
            <img v-if="item.length === 0 && !item.nsfw" class="card" :src="makePath(item)" data-fancybox
                :data-content="`画师: ${item.illustrator} ${makeIllustratorContact(item).outerHTML}`" loading="lazy" />
            <!-- single nsfw image -->
            <a v-else-if="item.length === 0 && item.nsfw" data-fancybox :data-src="makePath(item)"
                :data-content="`画师: ${item.illustrator} ${makeIllustratorContact(item).outerHTML}`">
                <div class="relative">
                    <img class="card" :src="makePath(item)" loading="lazy" />
                    <div
                        class="card absolute backdrop-blur-sm backdrop-brightness-50 inset-0 flex items-center justify-center">
                        <img class="max-w-full max-h-full object-contain" src="/src/assets/nsfw.avif" />
                    </div>
                </div>
            </a>
            <!-- multiple image -->
            <a v-else class="card" :data-src="makePath(item, 0)" :data-fancybox="`${item.illustrator}_${item.date}`"
                :data-content="`画师: ${item.illustrator} ${makeIllustratorContact(item).outerHTML}`">
                <img v-if="!item.nsfw" :src="makePath(item, 0)" :data-fancybox="`${item.illustrator}_${item.date}`"
                    loading="lazy" />
                <!-- multiple nsfw image -->
                <div v-else class="relative">
                    <img class="card" :src="makePath(item, 0)" loading="lazy" />
                    <div
                        class="card absolute backdrop-blur-sm backdrop-brightness-50 inset-0 flex items-center justify-center">
                        <img class="max-w-full max-h-full object-contain" src="/src/assets/nsfw.avif" />
                    </div>
                </div>
                <div class="no-display">
                    <img v-for="index in item.length - 1" :src="makePath(item, index)"
                        :data-fancybox="`${item.illustrator}_${item.date}`"
                        :data-content="`画师: ${item.illustrator} ${makeIllustratorContact(item).outerHTML}`"
                        loading="lazy" />
                </div>
            </a>
        </template>
    </MasonryWall>
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

<style>
.fancybox__container {
    --right-col-width: 0px;
}

.fancybox__container.has-sidebar {
    --right-col-width: clamp(150px, 20vw, 300px);
}

.fancybox__cols {
    display: grid;
    grid-template-columns: minmax(0, 1fr) var(--right-col-width);

    height: 100%;
}

.fancybox__col {
    display: flex;
    flex-direction: column;
    min-height: 0;

    position: relative;
    overflow: hidden;
}

.fancybox__data {
    padding: 1rem;
    overflow: auto;
}
</style>