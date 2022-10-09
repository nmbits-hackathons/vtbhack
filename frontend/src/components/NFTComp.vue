<template>
  <Surface class="nft_item__wrapper" :class="[item.size]">
    <img :src="item.image" :alt="item.title">

    <div class="nft_item__description">
      <div class="nft_item__info">
        <h3 class="nft_item__collection">{{item.collection}}</h3>
        <h5 class="nft_item__title">{{item.title}}</h5>
      </div>

      <Button @click="$router.push({
        name: 'Exchange',
        params: {
          id: 2
        }
      })" data-variant="secondary" class="nft_item__exchange">Обменять</Button>
    </div>
  </Surface>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import { NFTItem } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface,
    Button
  },
  props: {
    item: {
      type: Object as () => NFTItem,
      required: true
    }
  }
})
</script>


<style lang="scss" scoped>
.nft_item__wrapper {
  padding: 0 0 16px 0;
  overflow: hidden;

  display: flex;
  flex-flow: column;
  gap: 18px;

  grid-column: span 1;

  
  @media (min-width: 768px) {
    &, &.sm {
      grid-column: span 1;
  
      .nft_item__exchange {
        flex-basis: 100%;
      }
    }
  
    &.md {
      grid-column: span 2;
  
      .nft_item__exchange {
        flex-basis:  auto;
      }
    }
    &.big {
      grid-column: span 3;
  
      .nft_item__exchange {
        flex-basis:  auto;
      }
    }
  }


  > img {
    width: 100%
  }

  .nft_item__description {
    margin-top: auto;
    padding: 0 16px;
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
    justify-content: space-between;


    .nft_item__collection {
      font-weight: 400;
      font-size: 16px;
      line-height: 120%;
      color: rgb(var(--text-primary--hover));
      margin-bottom: 8px;
    }

    .nft_item__title {
      font-weight: 700;
      font-size: 20px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
    }

    
  }
}
</style>