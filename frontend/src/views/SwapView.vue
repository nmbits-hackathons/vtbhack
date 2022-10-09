<template>
  <Surface class="exchange__wrapper">
    <img :src="require(`@/assets/exchange/exchange${$route.params.id}.png`)" alt="Exchange">

    <div class="exchange__text">
      <h2>Обменять <span>Untitled (Variation Four)</span> на <span>{{$route.params.id == '1' ? 'Серую гарнитуру': '[1e] big time'}}</span>?</h2>

      <Button data-variant="primary" @click="openModal = !openModal">Обменять</Button>
    </div>

    <teleport to="main">
      <transition name="fade">
        <Modal v-if="openModal" @close="$router.push({name: 'Marketplace'})"
        class="modal__exchange"
        >
          <img :src="require(`@/assets/exchange/exchange${$route.params.id}success.png`)" alt="Exchange">

          <h2>Поздравляем!</h2>
          <p>Вы успешно обменяли свой NFT на {{$route.params.id == '1' ? 'Серую гарнитуру': '[1e] big time'}}</p>

          <Button class="modal__button" data-variant="primary" @click="$router.push({
          name: 'Marketplace'
        })">В маркетплейс</Button>
        </Modal>
      </transition>
    </teleport>
  </Surface>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import Modal from '@/components/ModalComp.vue'

export default defineComponent({
  components: {
    Surface,
    Button,
    Modal
  },  
  setup() {
    const openModal = ref(false)

    return {
      openModal
    }
  }
})
</script>

<style lang="scss" scoped>
.exchange__wrapper {
  padding: 32px;
  display: flex;
  flex-flow: column;
  gap: 32px;
  height: fit-content;

  .exchange__text {
    display: flex;
    justify-content: space-between;
    gap: 32px;
    flex-wrap: wrap;

    
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

  .modal__exchange {
    img {
      margin-bottom: 16px;
      width: 100%;
    }
    h2 {
      margin-bottom: 8px;
      padding: 0 24px;
    }
    p {
      margin-bottom: 24px;
      padding: 0 24px;
    }
    .modal__button {
      margin: 0 24px 32px;
    }
  }
</style>
