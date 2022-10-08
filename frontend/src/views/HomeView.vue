<template>
  <div class="feed">
    <NewsCard v-for="record in news" :key="record.title" :record="record"></NewsCard>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";

import NewsCard from '@/components/NewsCard.vue'
import { NewsRecord } from "@/utilities/types";

export default defineComponent({
  name: "HomeView",
  components: {
    NewsCard
  },
  setup() {
    const news = ref<NewsRecord[]>([
      {
        type: 'Митап',
        title: "Enterprise и тысячи микросервисов: архитектурные принципы, управление и проектирование",
        description: "Поговорим о том, как Enterprise переходит на темную сторону микрофронтенда. Расскажем (и даже покажем demo), как в ВТБ распиливают монолит на независимые фронты и строят их с нуля на разных проектах. Подробно и в деталях поделимся опытом, а также ответим на ваши вопросы. Митап организован при поддержке телеграм-сообществ React и JS",
        award: "104,75 ₽",
        date: new Date()
      },
      {
        type: 'Менторинг',
        title: "Микрофронтенд в ВТБ: real cases",
        description: "Переход на микросервисную архитектуру — один из ключевых трендов последних лет. На митапе обсудим, как работает с микросервисами один из крупнейших банков на рынке. Мы расскажем вам: · Как структурировать ландшафт архитектуры вокруг пользователя, а не вокруг конкретных решений. · Как управлять, развивать и добиваться эффективного результата с целым ландшафтом микросервисов · Как обеспечить их грамотное сопровождение А также поделимся реальными кейсами проектирования и управления микросервисами в ВТБ на примере мобильного приложения ВТБ Онлайн.",
        award: "284,48 ₽",
        date: new Date(124455)
      },
    ])

    return {
      news,
      news_lenght: computed(() => news.value.length || 0)
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
}

//TODO: add point to header
:deep(h1.route__name) {
  &::after {
    content: v-bind(news_lenght);
    position: absolute;
    top: -12px;
    right: 0;
    transform: translateX(-100%);

    height: 32px;
    width: 32px;

    display: grid;
    place-items: center;

    background-color: rgb(var(--text-primary--hover));
    color: rgb(var(--surface));

    font-family: 'Inter';
    font-style: normal;
    font-weight: 500;
    font-size: 18px;
    line-height: 22px;
    letter-spacing: -0.32px;

    @media (min-width: 768px) {
      height: 40px;
      width: 40px;
      font-size: 24px;
      line-height: 29px;
    }

  }
}
</style>
