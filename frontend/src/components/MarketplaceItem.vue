<template>
  <Surface class="marketplace_item__wrapper" :class="[item.size]">
    <img :src="item.image" :alt="item.title">

    <div class="marketplace_item__description">
      <div class="marketplace_item__info">
        <h3 class="marketplace_item__price">{{item.price}} ₽</h3>
        <h5 class="marketplace_item__title">{{item.title}}</h5>
      </div>

      <Button @click="$router.push({
        name: 'Exchange',
        params: {
          id: 1
        }
      })" data-variant="secondary" class="marketplace_item__buy">Обменять</Button>
    </div>
  </Surface>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import { MarketplaceItem } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface,
    Button
  },
  props: {
    item: {
      type: Object as () => MarketplaceItem,
      required: true
    }
  }
})
</script>


<style lang="scss" scoped>
.marketplace_item__wrapper {
  padding: 0 0 16px 0;
  overflow: hidden;

  display: flex;
  flex-flow: column;
  gap: 18px;

  grid-column: span 1;

  
  @media (min-width: 768px) {
    &, &.sm {
      grid-column: span 1;
  
      .marketplace_item__buy {
        flex-basis: 100%;
      }
    }
  
    &.md {
      grid-column: span 2;
  
      .marketplace_item__buy {
        flex-basis:  auto;
      }
    }
    &.big {
      grid-column: span 3;
  
      .marketplace_item__buy {
        flex-basis:  auto;
      }
    }
  }


  > img {
    width: 100%
  }

  .marketplace_item__description {
    margin-top: auto;
    padding: 0 16px;
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
    justify-content: space-between;


    .marketplace_item__price {
      font-weight: 600;
      font-size: 24px;
      line-height: 29px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      margin-bottom: 8px;
    }

    .marketplace_item__title {
      font-style: normal;
      font-weight: 400;
      font-size: 16px;
      line-height: 120%;
    }

    
  }
}
</style>