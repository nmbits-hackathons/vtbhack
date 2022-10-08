<template>
  <div class="marketplace__wrapper">
    <div class="marketplace__items">
      <router-link :to="'/'" class="marketplace__exchange_nft">
        <h2>Обменивайте<br>NFT на товары</h2>
        <p>Попробуйте</p>
      </router-link>
      <Marketplace v-for="(item, index) in items" :key="index" :item="item"/>
    </div>
  </div>
</template>

<script lang="ts">
import { MarketplaceItem } from '@/utilities/types';
import { defineComponent, ref } from 'vue'

import Marketplace from '@/components/MarketplaceItem.vue'

export default defineComponent({
  components: {
    Marketplace
  },
  setup() {
    const items = ref<MarketplaceItem[]>([
      {
        image: require('@/assets/speaker_sm.png'),
        price: 2500,
        title: "Маленькая умная колонка",
        size: "md"
      },
      {
        image: require('@/assets/headphones.png'),
        price: 3500,
        title: "Гарнитура",
      },
      {
        image: require('@/assets/speaker_big.png'),
        price: 4900,
        title: "Большая колонка",
      },
      {
        image: require('@/assets/binocol.png'),
        price: 2380,
        title: "Бинокль для охоты и рыбалки",
      },
      {
        image: require('@/assets/camera.png'),
        price: 12450,
        title: "Экшн-камера",
      },
      {
        image: require('@/assets/speaker_sm.png'),
        price: 2500,
        title: "Маленькая умная колонка",
        size: 'md'  
      },
      {
        image: require('@/assets/headphones.png'),
        price: 3500,
        title: "Гарнитура",
      },
      {
        image: require('@/assets/speaker_big.png'),
        price: 4900,
        title: "Большая колонка",
        size: 'big'
      },
      {
        image: require('@/assets/binocol.png'),
        price: 2380,
        title: "Бинокль для охоты и рыбалки",
        size: 'md'  
      },
      {
        image: require('@/assets/camera.png'),
        price: 12450,
        title: "Экшн-камера",
      },
    ])

    return {
      items
    }
  },
})
</script>

<style lang="scss" scoped>
.marketplace__items {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-flow: dense;
  gap: 12px;

  .marketplace__exchange_nft {
    @media (min-width: 768px) {
      grid-column-start:1;
      grid-column-end: -1;

    }
    background: rgb(var(--button-primary)) url('../assets/flower.svg');
    background-repeat: no-repeat;
    background-position: right bottom;
    border-radius: 24px;
    padding: 24px 32px 48px;

    text-decoration: none;

    h2 {
      font-weight: 600;
      font-size: 32px;
      line-height: 100%;
      letter-spacing: -0.04em;
      color: rgb(var(--button-primary-text));
      margin-bottom: 24px;
    }

    p {
      font-weight: 500;
      font-size: 20px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: rgb(var(--button-primary-text) / .8);
    }
  }

}
</style>
