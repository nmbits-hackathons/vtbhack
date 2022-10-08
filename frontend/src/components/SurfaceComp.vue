<template>
  <section class="surface">
    <slot/>
  </section>
</template>

<style lang="scss" scoped>
.surface {
  border-radius: 24px;
  background: rgb(var(--surface));
  padding: 8px 16px 24px;

  @media (min-width: 768px) {
    padding: 16px 24px 32px;
  }
}
</style>