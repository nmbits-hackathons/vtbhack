<template>
  <Surface class="rating">
    <h3>Топ-{{rating.length}} за сегодня</h3>

    <div class="rating__wrapper" v-for="(person, number) in rating" :key="number">
      <div class="rating__icon">{{number}}</div>

      <div class="rating__info">
        <div class="rating__name">
          {{ person.name }}
        </div>
      </div>
    </div>
  </Surface>
</template>

<script lang="ts">
import { defineComponent, ref, defineAsyncComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'

export default defineComponent({
  components: {
    Surface
  },
  setup() {
    const rating = ref([
      {
        name: "Платон Лапп"
      },
      {
        name: "Дмитрий Воронцов"
      },
      {
        name: "Алексей Торопов"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
      {
        name: "Платон Лапп"
      },
    ])

    return {
      rating
    }
  },
})
</script>

<style lang="scss" scoped>
.rating {
  padding: 16px 16px 8px;
  
  @media (min-width: 768px) {
    padding: 24px 24px 8px;
  }

  h3 {
    font-weight: 600;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: rgb(var(--text-primary));
    margin-bottom: 8px;
  }

  .rating__wrapper {
    display: flex;
    gap: 16px;
    .rating__icon {
      margin: auto 0;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: grid;
      place-items: center;

      font-weight: 500;
      font-size: 18px;
      line-height: 22px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      background: #F4F7FB;
    }

    .rating__info {
      flex: 1;
      padding: 16px 0 24px;
      display: flex;
      gap: 24px;
      justify-content: space-between;
      white-space: nowrap;

      font-weight: 500;
      font-size: 18px;
      line-height: 22px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));

      
    }
  }

  .rating__wrapper:not(:last-child) .rating__info {
    border-bottom: 1px solid rgb(var(--divider-primary));
  }
}
</style>
