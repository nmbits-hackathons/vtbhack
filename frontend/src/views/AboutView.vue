<template>
  <div class="about">
    <p>{{ store.dispatch('wallet/transferMatic', {
      toPublicKey: '',
      amount: 0.5
    }) }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useStore } from 'vuex'

export default defineComponent({
  setup() {
    const store = useStore()

    return {
      store
    }
  },
})
</script>

