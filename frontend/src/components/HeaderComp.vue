<template>
  <nav>
    <router-link to="/" class="nav__logo">
      <img src="../assets/logo.svg" alt="Logo">
    </router-link>

    <router-link :to="{
      name: 'Profile',
      params: {
        id: user.id
      }
    }" class="nav__account">
      <HumanIcon/>

      <span class="nav__user">{{ user.first_name }} {{ user.last_name }}</span>
    </router-link>
  </nav>
</template>

<script lang="ts">
import { User } from '@/utilities/types'
import { computed, defineComponent } from 'vue'
import { useStore } from 'vuex'
import HumanIcon from './Icons/HumanIcon.vue'

export default defineComponent({
  components: {
    HumanIcon
  },
  setup() {
    const store = useStore()

    const { value: user } = computed<User>(() => store.state.user)

    return {
      user
    }
  }
})
</script>

<style lang="scss" scoped>
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;

  padding: 16px clamp(24px, 5vw, 64px);
  max-height: var(--header-height);

  background: rgb(var(--background));

  display: flex;
  justify-content: space-between;
  gap: 8px;
  z-index: 1;

  .nav__account {
    display: flex;
    align-items: center;
    gap: 11px;

    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: rgb(var(--text-primary));

    transition: var(--transition);

    text-decoration: none;

    &:hover {
      color: rgb(var(--text-primary--hover));
    }

    .nav__user {
      display: none;

      @media (min-width: 552px) {
        display: inherit;
      }
    }
  }
}
</style>
