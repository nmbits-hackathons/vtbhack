<template>
  <section class="menu__wrapper_left">
    <div class="user__links">
      <router-link
        class="user__link"
        :class="{
          active: $route.name == link.route.name
        }"
        :to="link.route"
        v-for="link in links"
        :key="link.route.name"
      >
        <span class="link__icon">
          <!-- TODO: paint only icon -->
          <component :is="
            defineAsyncComponent(() => 
              import(`@/components/Icons/${link.icon}.vue`))
          " />
        </span>

        <span class="link__text">{{ link.text ? link.text : useNormalizedRoute(link.route.name) }}</span>
      </router-link>
    </div>
  </section>
</template>

<script lang="ts">
import { computed, defineComponent, defineAsyncComponent } from "vue";
import { useStore } from "vuex";
import { useNormalizedRoute } from '@/utilities/composables/useNormalizedRoute'

export default defineComponent({
  setup() {
    const store = useStore();

    const { value: id } = computed(() => store.state.user.id);
    const links = computed(() => [
      {
        icon: 'HumanIcon',
        text: "Аккаунт",
        route: {
          name: "Profile",
          params: {
            id: id,
          },
        }
      },
      {
        icon: 'FeedIcon',
        route: {
          name: "Home",
        }
      },
      {
        icon: 'MarketplaceIcon',
        route: {
          name: "Marketplace",
        }
      },
      {
        icon: 'CollectionsIcon',
        route: {
          name: "Collections",
        }
      },
      {
        icon: 'RatingIcon',
        route: {
          name: "Rating",
        }
      },
    ]);

    return {
      links,
      id,
      defineAsyncComponent,
      useNormalizedRoute
    };
  },
});
</script>

<style lang="scss" scoped>
.menu__wrapper_left {
  position: fixed;
  background: rgb(var(--surface));
  bottom: 0;
  left: 0;
  right: 0;
  @media (min-width: 1200px) {
    position: relative;
    background: none;
  }
  .user__links {
    display: grid;
    grid-auto-flow: column;
    padding: clamp(2px, 1vw, 8px) clamp(8px, 5vw, 40px);
    place-items: center;
    @media (min-width: 1200px) {
      gap: 16px;
      grid-auto-flow: row;
      place-items: inherit;
      padding: 0;
    }

    .user__link {
      transition: var(--transition);
      border-radius: 16px;

      font-weight: 500;
      font-size: clamp(9px, 3vw, 14px);
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));


      &.active, &:hover {
        color: rgb(var(--text-primary--hover));
        background: rgb(var(--surface));
      }

      display: flex;
      flex-flow: column;
      align-items: center;
      gap: 8px;
      padding: clamp(8px, 5vw, 16px) 0;
      
      text-decoration: none;
      width: 100%;

      @media (min-width: 1200px) {
        padding: 16px 24px;
        flex-flow: row;
        font-size: 20px;
        gap: 16px;
        color: rgb(var(--text-primary));
      }

    }
  }
}
</style>
