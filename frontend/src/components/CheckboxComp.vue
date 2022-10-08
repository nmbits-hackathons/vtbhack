<template>
  <div
    class="checkbox-wrapper"
    @click="checked = !checked; $emit('update:modelValue', checked);"
  >
    <div
      class="checkbox"
      :class="{'checked': checked}"
    >
      <div class="checkbox-control">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M23 6.3518L9.11678 20L2 13.0037L4.3923 10.6519L9.11678 15.2964L20.6077 4L23 6.3518Z" fill="white" />
        </svg>
      </div>
      <input
        v-model="checked"
        type="checkbox"
        name="checkbox"
      >
    </div>
    <div
      v-if="label"
      class="label"
    >
      {{ label }}
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent, ref } from 'vue';

  export default defineComponent({
    name: 'CheckboxComp',

    props: {
      label: {
        type: String,
        default: '',
      },
      modelValue: {
        type: Boolean,
        default: false,
      },
    },

    setup(props) {
      const checked = ref(props.modelValue);
      return { checked };
    },
  });
</script>

<style lang="scss" scoped>
.checkbox-wrapper {
  $size: 1.25rem;

  display: inline-flex;
  align-items: center;

  &:hover {
    cursor: pointer;
  }

  .checkbox {
    width: $size;
    height: $size;
    border: 1px solid rgb(var(--divider-primary));
    border-radius: .1875rem;
    transition: all 0.1s ease-out;

    .checkbox-control {
      text-align: center;
      line-height: $size;

      svg {
        transform-origin: center;
        transform: scale(0);
        transition: transform 0.1s ease-out;
      }
    }

    &.checked {
      background-color: rgb(var(--text-primary--hover));
      border-color: rgb(var(--text-primary--hover));

      svg {
        transform: scale(.8);
      }
    }

    input {
      width: 0;
      height: 0;
      opacity: 0;
    }
  }

  .label {
    flex: 1;
    padding-left: .75rem;
    font-weight: 500;
    font-size: 18px;
    line-height: 22px;
    letter-spacing: -0.02em;
    color: rgb(var(--text-primary));
  }
}
</style>
