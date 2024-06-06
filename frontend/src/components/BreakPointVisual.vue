<!-- BreakPointVisual.vue
  componets related to tailwind to show the breakpoints as the screen changes to better design responsive web pages
-->
<template>
  <div class="fixed top-0 left-0 m-1 p-1 z-50 font-mono text-white h-10 w-10 rounded-full flex items-center justify-center bg-gray-700 xxs:bg-purple-500 sm:bg-pink-500 md:bg-orange-500 lg:bg-green-500 xl:bg-blue-500 2xl:bg-black">
    <div class="block xxs:hidden">xxs</div>
    <div class="hidden xxs:block sm:hidden">xs</div> 
    <div class="hidden sm:block md:hidden">sm</div>
    <div class="hidden md:block lg:hidden">md</div>
    <div class="hidden lg:block xl:hidden">lg</div>
    <div class="hidden xl:block 2xl:hidden">xl</div>
    <div class="hidden 2xl:block">2xl</div>
  </div>
</template>

<script>
export default {
  name: 'BreakPointVisual'
};
</script>

<style scoped>
</style>
