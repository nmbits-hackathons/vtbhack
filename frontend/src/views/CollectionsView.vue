<template>
  <div class="marketplace__wrapper">
    <div class="marketplace__items">
      <NFT v-for="(item, index) in items" :key="index" :item="item"/>
    </div>
  </div>
</template>

<script lang="ts">
import { MarketplaceItem, NFTItem } from '@/utilities/types';
import { defineComponent, ref } from 'vue'

import NFT from '@/components/NFTComp.vue'

export default defineComponent({
  components: {
    NFT
  },
  setup() {
    const items = ref<NFTItem[]>([
      {
        image: require('@/assets/nft/blind.png'),
        collection: 'Bilnd Abstract',
        title: "Untitled (Variation Four)",
      },
      {
        image: require('@/assets/nft/blind2.png'),
        collection: 'Bilnd Abstract',
        title: "Register",
      },
      {
        image: require('@/assets/nft/hashrunes.png'),
        collection: 'Hashrunes',
        title: "[1e] big time",
      },
      {
        image: require('@/assets/nft/tobler.png'),
        collection: 'Tobler art',
        title: "Football",
      },
      {
        image: require('@/assets/nft/contempix.png'),
        collection: 'CONTEMPIX',
        title: "Bank",
      },
      {
        image: require('@/assets/nft/blind3.png'),
        collection: 'Bilnd Abstract',
        title: "Fennel & Chamomile",
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
