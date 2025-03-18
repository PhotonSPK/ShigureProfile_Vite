<script setup lang="ts">
defineProps<{ avatar: string }>()
</script>

<template>
    <img :src="`/imgs/portraits/shigure_${avatar}.avif`" alt="Shigure" />
</template>