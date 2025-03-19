<script setup lang="ts">
import { onMounted, onUnmounted, onUpdated } from "vue";
import { Fancybox } from "@fancyapps/ui";
import '@fancyapps/ui/dist/fancybox/fancybox.css';
defineProps<{ refKey: string, path: string }>();

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
    }
};

onMounted(() => {
    Fancybox.bind('[data-fancybox-transition]', fancyBoxOption);
});

onUpdated(() => {
    Fancybox.unbind('[data-fancybox-transition]');
    Fancybox.close();
    Fancybox.bind('[data-fancybox-transition]', fancyBoxOption);
})

onUnmounted(() => {
    Fancybox.destroy();
});
</script>

<template>
    <Transition name="fade" mode="out-in">
        <img class="transition-all" :key="refKey" :src="path" data-fancybox-transition/>
    </Transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 100ms ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>