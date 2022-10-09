<template>
  <Surface class="profile__wallet">

    <div class="wallet__currencies">
      <h3>Кошелёк</h3>
      <h2 class="wallet__roubles">{{ wallet.coins?.toFixed(2) }} ₽<h5 class="wallet__matic">{{ wallet.matic?.toFixed(2) }} GAS</h5></h2>
    </div>

    <div class="wallet__actions">
      <router-link :to="{
          name: 'Marketplace'
        }"
        custom
        v-slot="{ navigate }"
      >
      <Button @click="navigate" data-variant="secondary">В маркетплейс</Button>
    </router-link>
      <router-link :to="{
          name: 'Collections'
        }"
        custom
        v-slot="{ navigate }"
      >
      <Button @click="navigate" data-variant="primary">Поблагодарить</Button>
    </router-link>
    </div>
  </Surface>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import { useStore } from 'vuex'
import { Wallet } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface,
    Button
  },
  setup() {
    const store = useStore()

    const { value: wallet } = computed<Wallet>(() => store.state.wallet)

    return {
      wallet 
    }
  },
})
</script>

<style lang="scss" scoped>
.profile__wallet {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 24px;

  .wallet__currencies {
    h3 {
      font-weight: 600;
      font-size: 20px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      margin-bottom: 8px;
      
    }
    .wallet__roubles {
      font-weight: 600;
      font-size: 32px;
      line-height: 39px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary--hover));
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .wallet__matic { 
      font-weight: 600;
      font-size: 18px;
      line-height: 22px;
      /* identical to box height */

      letter-spacing: -0.04em;

      color: rgb(var(--text-secondary) / .4);
    }
  }

  .wallet__actions {
    margin-top: auto;

    display: flex;
    flex-wrap: wrap;
    gap: 8px;

    > * {
      flex-basis: 160px;
      flex-grow: 1;
    }
  }
}
</style>
