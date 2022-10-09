<template>
  <div class="feed">
    <div class="feed__tabs">
      <div class="feed__tab" @click="currentTab = 0" :class="{
        active: currentTab == 0
      }">Предстоящие</div>
      <div class="feed__tab" @click="currentTab = 1" :class="{
        active: currentTab == 1
      }">Завершенные</div>

      <div class="feed__sort" @click="isOpenSort = !isOpenSort">
        <ListIcon class="sort__icon"/>
        Сортировать

        <transition name="fade">
          <div v-if="isOpenSort" class="sort__modal">
            <div class="sort__item">По релевантности</div>
            <div class="sort__item">Сначала новые</div>
            <div class="sort__item">Самые популярные</div>
          </div>
        </transition>
      </div>
    </div>

    <label for="search" class="feed__search">
      <svg width="17" height="20" viewBox="0 0 17 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g opacity="0.2">
          <path d="M8.00653 15.9985C9.14873 15.999 10.2775 15.7535 11.3162 15.2785L14.2493 19.4347C14.5236 19.8241 14.9851 20.0376 15.4594 19.9945C15.9339 19.9515 16.3494 19.6586 16.5493 19.2262C16.7492 18.794 16.7034 18.2876 16.4289 17.8982L13.526 13.782C15.3318 12.0562 16.2276 9.5858 15.9478 7.10357C15.6682 4.62128 14.2451 2.41242 12.1003 1.13161C9.95588 -0.149205 7.33616 -0.354717 5.01838 0.576192C2.70048 1.5071 0.950256 3.46718 0.287234 5.87555C-0.376086 8.28368 0.123794 10.8636 1.63845 12.8498C3.15311 14.8359 5.50868 16.0007 8.0068 15.9984L8.00653 15.9985ZM8.00653 2.66667C9.42102 2.66667 10.7774 3.22836 11.7775 4.22852C12.7774 5.22871 13.3393 6.58505 13.3393 7.99924C13.3393 9.41372 12.7774 10.7701 11.7775 11.7702C10.7773 12.7701 9.42096 13.332 8.00653 13.332C6.59228 13.332 5.23594 12.7701 4.23581 11.7702C3.23563 10.77 2.67396 9.41366 2.67396 7.99924C2.67396 6.58499 3.23566 5.22865 4.23581 4.22852C5.236 3.22833 6.59234 2.66667 8.00653 2.66667Z" fill="black"/>
          </g>
      </svg>
      <input type="text" id="search" placeholder="Поиск мероприятий">
    </label>
    <NewsCard v-for="record in news" :key="record.title" :record="record"></NewsCard>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeMount, ref } from "vue";

import NewsCard from '@/components/NewsCard.vue'
import ListIcon from '@/components/Icons/ListIcon.vue'
import { Event } from "@/utilities/types";
import { useStore } from "vuex";

export default defineComponent({
  name: "HomeView",
  components: {
    NewsCard,
    ListIcon
  },
  setup() {
    const store = useStore()

    const news = computed<Event[]>(() => store.getters['utilities/getState']('events'))
    const isOpenSort = ref(false)
    const currentTab = ref(0)

    onBeforeMount(() => {
      store.dispatch('utilities/init')
    })

    return {
      news,
      news_lenght: computed(() => news.value.length || 0),
      isOpenSort,
      currentTab
    }
  }
});
</script>

<style lang="scss" scoped>
.feed {
  display: flex;
  flex-flow: column;
  gap: 20px;

  @media (min-width: 768px) {
    gap: 16px;
  }

  .feed__tabs {
    display: flex;
    flex-wrap: wrap;
    border-bottom: 1px solid rgb(var(--divider-primary));

    .feed__tab {
      padding: 24px;
      font-weight: 500;
      font-size: 20px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      border-bottom: 3px solid transparent;
      transition: var(--transition);
      cursor: pointer;

      &:hover, &.active {
        border-color: rgb(var(--text-primary--hover));
      }
    }

    .feed__sort {
      margin-left: auto;
      padding: 24px;
      font-weight: 500;
      font-size: 20px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: rgb(var(--text-primary));
      transition: var(--transition);
      cursor: pointer;
      position: relative;

      .sort__icon {
        margin-right: 16px;
      }

      .sort__modal {
        position: absolute;
        bottom: 0;
        left: 0;
        // right: 0;
        overflow: hidden;
        transform: translateY(100%);
        background: rgb(var(--surface));
        border: 1px solid rgb(var(--divider-primary));
        box-shadow: 0px 8px 18px rgba(0, 0, 0, 0.04);
        border-radius: 16px;
        display: grid;

        .sort__item {
          padding: 16px 24px;

          font-weight: 400;
          font-size: 18px;
          line-height: 150%;
          color: rgb(var(--text-secondary) /.8);
          white-space: nowrap;
          transition: var(--transition);

          &:hover {
            background: rgb(var(--divider-primary));
          }
        }
      }
    }
  }

  .feed__search {
    background: rgb(var(--surface));
    border-radius: 24px;
    display: flex;
    padding: 24px;
    gap: 16px;

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

      &::placeholder {
        color: rgb(var(--text-primary) / .2);
      }
    }
  }
}
</style>
