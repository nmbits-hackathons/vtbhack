<template>
  <header-comp></header-comp>
  <main>
    <h1 class="route__name">{{ normalizedRoute }}</h1>

    <MenuComp class="menu__wrapper"/>

    <router-view :class="['router__view']" />
  </main>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'

import HeaderComp from '@/components/HeaderComp.vue'
import MenuComp from '@/components/MenuComp.vue'
import { useRoute } from 'vue-router'
import { useNormalizedRoute } from '@/utilities/composables/useNormalizedRoute'

export default defineComponent({
  components: {
    HeaderComp,
    MenuComp
  },
  setup() {
    const route = useRoute()
    const normalizedRoute = computed(() => useNormalizedRoute(route.name))

    return {
      normalizedRoute
    }
    
  },
})
</script>


<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");

:root {
  --background: 244 247 251;
  --surface: 255 255 255;

  --text-primary: 0 0 0;
  --text-primary--hover: 50 100 246;

  --text-secondary: 17 17 17;

  --divider-primary: 232 236 241;
  --accent: 18 39 144;

  --button-primary: 50 100 246;
  --button-primary-text: 255 255 255;
  --button-primary-hover: 18 39 144;

  --button-secondary: 244 247 251;
  --button-secondary-text: 0 0 0;
  --button-secondary-hover: 255 255 255;

  --transition: all 0.2s ease-in-out;

  --header-height: 64px;
}

#app {
  font-family: "Inter", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: rgb(var(--background));
}

*,
::after,
::before {
  box-sizing: border-box;
}

h1, h2, h3, h4, h5, h6, p {
  margin: 0;
}

body {
  margin: 0;
}

main {
  padding: 0;
  margin: 0 auto;
  min-height: 100vh;
  max-width: 1920px;
  display: grid;
  padding: calc(var(--header-height) + 40px) clamp(16px, 5vw, 64px);
  grid: "route" min-content
        "content" 1fr / 100%;
  ;
  gap: 24px;

  @media (min-width: 1200px) {
    grid: 'route route' min-content
          "menu content" 1fr / 260px 762px;
    ;
    gap: 32px 64px;
    padding-bottom: 16px;
  }

  .route__name {
    grid-area: route; 
    font-weight: 600;
    font-size: 40px;
    line-height: 48px;
    letter-spacing: -0.32px;
    color: rgb(var(--text-secondary));
    margin: 0;
    position: relative;
    
    @media (min-width: 768px) {
      font-size: 64px;
      line-height: 77px;
    }

    @media (min-width: 1200px) {
      padding-bottom: 24px;
      border-bottom: 1px solid rgb(var(--divider-primary));
    }
  }

  .menu__wrapper {
    grid-area: menu;

    @media (min-width: 1200px) {
      max-width: 220px;
    }
  }

  .router-view {
    grid-area: content;
  }

}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
