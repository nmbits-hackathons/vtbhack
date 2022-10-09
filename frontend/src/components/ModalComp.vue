<template>
  <div class="modal__background_wrapper">
    <div class="modal__wrapper" v-click-outside="closeModal">
      <div class="modal__content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup(props, { emit }) {
    const closeModal = () => {
      emit("close");
    };
    return {
      closeModal,
    };
  },
});
</script>

<style lang="scss" scoped>
.modal__background_wrapper {
  min-height: 100vh;
  width: 100%;
  z-index: 9998;
  position: fixed;
  left: 0;
  top: 0;
  background: rgba(0, 0, 0, 0.4);
  display: grid;
  place-items: center;
  padding: 1rem;
}

.modal__wrapper {
  width: min(500px, 100%);
  background: rgb(var(--surface));
  border: 1px solid rgb(var(--divider-primary));
  border-radius: 24px;
  position: relative;
  z-index: 9999;
  overflow: hidden;

  .modal__content {
    padding: 0 0px 16px;
  }
}
</style>
