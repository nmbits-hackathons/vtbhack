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
      
      <Button @click="openModal = !openModal" data-variant="primary">Поблагодарить</Button>
    </div>

    <teleport to="main">
      <transition name="fade">
        <Modal v-if="openModal" @close="openModal = !openModal"
        class="modal__thanks"
        >
          <h2>Поблагодарить</h2>
          <p>Поблагодарите коллегу отправив ему перевод в цифровых рублях или NFT</p>

          <input id="fio" type="text" placeholder="ФИО коллеги">
          <input v-maska="'#*'" v-model="summary" id="summary_amount" type="text" placeholder="Сумма перевода или Токен-ID">

          <Button class="modal__button" data-variant="primary" @click="timeout">Поблагодарить</Button>
        </Modal>
      </transition>
    </teleport>
  </Surface>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import Modal from '@/components/ModalComp.vue'

import { useStore } from 'vuex'
import { Wallet } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface,
    Button,
    Modal
  },
  setup() {
    const store = useStore()

    const { value: wallet } = computed<Wallet>(() => store.state.wallet)

    const openModal = ref(false)
    const summary = ref(null)

    const timeout = () => {
      setTimeout(() => {
        openModal.value = !openModal.value
        store.commit('wallet/setState', {
          key: 'coins',
          value: (wallet.coins || summary.value || 0) - (summary.value || 0)
        })
      }, 1250)
    }

    return {
      wallet,
      openModal,
      timeout,
      summary
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
      white-space: nowrap;
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

  p {
    font-weight: 400;
    font-size: 16px;
    line-height: 120%;
    color: rgb(var(--text-primary)  / .4);
  }

.modal__thanks {
  :deep(.modal__content) {
    padding: 32px 24px;
  }

  h2 {
    margin-bottom: 8px;
  }
  p {
    margin-bottom: 24px;
  }
  input {
    margin-bottom: 12px;
  }
  .modal__button {
    margin-top: 12px;
  }

  input {
    font-family: "Inter";
    font-weight: 500;
    font-size: 18px;
    line-height: 22px;
    letter-spacing: -0.06px;
    color: var(--text-primary);
    border: none;
    background: none;
    width: 100%;
    outline: none;
    padding: 16px 12px;
    border: 1px solid rgb(var(--divider-primary));
    border-radius: 8px;

    &::placeholder {
      color: rgb(var(--text-primary) / .2);
    }
  }
}
</style>
