<script setup lang="ts">
defineProps<{ avatar: string }>()
</script>

<template>
    <img :src="`/src/assets/portraits/shigure_${avatar}.avif`" alt="Shigure" />
</template>