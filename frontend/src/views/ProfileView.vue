<template>
  <div class="profile">
    <ProfileWallet/>

    <div class="profile__transactions">
      <WalletTransactions v-for="(trans, index) in transactions" :key="index" :data="trans" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import ProfileWallet from '@/components/ProfileWallet.vue'
import WalletTransactions from '@/components/WalletTransactions.vue'
import { TransactionsData } from '@/utilities/types'

export default defineComponent({
  components: {
    ProfileWallet,
    WalletTransactions
  },
  setup() {
    const transactions = ref<TransactionsData[]>([
      {
        date: new Date(),
        transactions: [
          {
            transactionType: 'marketplace',
            amount: '–299,89 ₽'
          },
          {
            transactionType: 'events',
            amount: '+244,89 ₽'
          },
          {
            transactionType: 'thanks',
            amount: '+554 ₽',
          },
          {
            transactionType: 'nft',
            amount: '-1'
          }
        ]
      },
      {
        date: new Date(35356567),
        transactions: [
          {
            transactionType: 'events',
            amount: '+2323,65 ₽'
          },
          {
            transactionType: 'marketplace',
            amount: '–32,45 ₽'
          },
          {
            transactionType: 'nft',
            amount: '+1'
          },
          {
            transactionType: 'thanks',
            amount: '+346 ₽',
          },
        ]
      },
    ])

    return {
      transactions
    }
  },
})
</script>

<style lang="scss" scoped>
.profile {
  display: flex;
  flex-flow: column;
  gap: 16px;

  .profile__transactions {
    display: flex;
    flex-flow: column;
    gap: 8px;
  }
}
</style>
