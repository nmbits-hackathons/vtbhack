<template>
  <Surface class="wallet__transactions">
    <h3>{{ data.date.toLocaleDateString('ru-RU', { month: 'long', day: 'numeric' })  }}</h3>

    <div class="wallet__transaction_wrapper" v-for="trans in data.transactions" :key="trans.transactionType">
      <component class="transaction__icon" :class="[trans.transactionType]" :is="
      defineAsyncComponent(() => import(`@/components/Icons/${transactionsAliases.components[trans.transactionType]}.vue`))
      " />

      <div class="transaction__info">
        <div class="transaction__alias">
          {{ transactionsAliases.text[trans.transactionType] }}
        </div>

        <div class="transaction__amount" :class="{
          minus: trans.amount.includes('–')
        }">
          {{ trans.amount }}
        </div>
      </div>
    </div>
  </Surface>
</template>

<script lang="ts">
import { defineComponent, ref, defineAsyncComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import { TransactionsData } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface
  },
  props: {
    data: {
      type: Object as () => TransactionsData,
      required: true
    } 
  },
  setup() {
    const transactionsAliases = ref({
      text: {
        marketplace: "Покупка на маркетплейсе",
        events: "Участие в мероприятиях",
        thanks: "Благодарности",
        nft: "Обмен NFT"
      },
      components: {
        marketplace: "MarketplaceIcon",
        events: "FeedIcon",
        thanks: "ThanksIcon",
        nft: "CollectionsIcon"
      }
    })

    return {
      transactionsAliases,
      defineAsyncComponent
    }
  },
})
</script>

<style lang="scss" scoped>
.wallet__transactions {
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

  .wallet__transaction_wrapper {
    display: flex;
    gap: 16px;
    .transaction__icon {
      margin: auto 0;

      &.marketplace {
        color: #66BE66;
      }

      &.events {
        color: #3264F6;
      }

      &.thanks {
        color: #001AFF;
      }

      &.nft {
        color: #FFA500;
      }
    }

    .transaction__info {
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

      &:not(:last-child) {
        border-bottom: 1px solid rgb(var(--divider-primary));
      }

      .transaction__amount.minus {
        color: #F13F3F;
      }
      
    }
  }
}
</style>
