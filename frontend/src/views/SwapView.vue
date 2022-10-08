<template>
  <Surface class="exchange__wrapper">
    <img :src="require(`@/assets/exchange/exchange${$route.params.id}.png`)" alt="Exchange">

    <div class="exchange__text">
      <h2>Обменять <span>Untitled (Variation Four)</span> на <span>Серую гарнитуру</span>?</h2>

      <Button data-variant="primary">Обменять</Button>
    </div>
  </Surface>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'

export default defineComponent({
  components: {
    Surface,
    Button
  },  
})
</script>

<style lang="scss" scoped>
.exchange__wrapper {
  padding: 32px;
  display: flex;
  flex-flow: column;
  gap: 32px;
  height: fit-content;

  .exchange__text {
    display: flex;
    justify-content: space-between;
    gap: 32px;
    flex-wrap: wrap;

    h2 {
      font-weight: 600;
      font-size: 24px;
      line-height: 29px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      max-width: 60%;

      span {
        color: rgb(var(--text-primary--hover));
      }
    }
  }
}
</style>
