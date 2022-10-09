<template>
  <Surface class="record__wrapper">
    <h2>Мероприятние</h2>

    <div class="record__fields">
      <div class="record__field">
        <h5>Тип мероприятия</h5>
        <select v-model="routeRecord.type">
          <option value="Митап">Митап</option>
          <option value="Менторинг">Менторинг</option>
          <option value="Ивент">Ивент</option>
        </select>
      </div>
      <div class="record__field">
        <h5>Заголовок</h5>
        <textarea cols="30" rows="10" v-model="routeRecord.title"></textarea>
      </div>
      <div class="record__field">
        <h5>Описание</h5>
        <textarea cols="30" rows="10" v-model="routeRecord.description"></textarea>
      </div>
      <div class="record__field">
        <h5>Вознаграждение</h5>
        <input type="text" v-maska="'#*.#* ₽'" v-model="routeRecord.reward">
      </div>
      <div class="record__field">
        <h5>Дата проведения</h5>
        <input type="date" v-model="routeRecord.date_event">
      </div>
    </div>

    <div class="record__action">
      <Button v-if="isValidRecord" data-variant="secondary">Сохранить</Button>
      <Button v-else data-variant="secondary">Создать</Button>
    </div>
  </Surface>
</template>

<script lang="ts">
import { computed, defineComponent, reactive, ref } from 'vue'

import Surface from '@/components/SurfaceComp.vue'
import Button from '@/components/ButtonComp.vue'
import { useRoute } from 'vue-router'

import { Event } from '@/utilities/types'

export default defineComponent({
  components: {
    Surface,
    Button
  },
  setup() {
    const date_pattern = /(\d{2})\.(\d{2})\.(\d{4})/;
    const route = useRoute()

    const routeRecord = reactive<Event>({
      title: '',
      description: "",
      date_publication: new Date(),
      date_event: new Date(),
      creator: 0,
      type: 'Митап',
      reward: 0
    })

    try {
      Object.assign(routeRecord, JSON.parse(decodeURIComponent(escape(atob(route.params.record.toString())))))
    } catch(e) {
      console.log('create');
      
    }

    return {
      isValidRecord: computed(() => routeRecord.type),
      routeRecord
    }
  }
})
</script>

<style lang="scss" scoped>
.record__wrapper {
  display: flex;
  flex-flow: column;
  gap: 24px;
  padding: 32px 24pxs;

  h2 {
    font-weight: 600;
    font-size: 28px;
    line-height: 34px;
    letter-spacing: -0.32px;
    color: rgb(var(--text-secondary));
  }

  .record__fields {
    display: flex;
    flex-flow: column;
    gap: 16px;
    max-width: 90%;

    .record__field {
      display: flex;
      flex-flow: column;
      gap: 12px;

      h5 {
        font-weight: 500;
        font-size: 16px;
        line-height: 19px;
        letter-spacing: -0.06px;
        color: rgb(var(--text-secondary) / .4);
      }

      input, textarea, select {
        padding: 16px 12px;
        border: 1px solid rgb(var(--divider-primary));
        border-radius: 8px;

        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 18px;
        line-height: 150%;
        color: #1D1D1D;
      }
    }
  }

  .record__action {
    padding-top: 16px;
    border-top: 1px solid rgb(var(--divider-primary));
  }
}
</style>
