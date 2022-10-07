<template>
  <main>
    <router-view />
  </main>
</template>

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

body {
  margin: 0;
}

main {
  padding: 0;
  margin: 0 auto;
  min-height: 100vh;
  max-width: 1920px;
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
