<template>
  <SurfaceComp class="record__wrapper">
    <div class="record__text" @click="isCollapsed = !isCollapsed">
      <h3>{{ record.type }}</h3>
      <h2>{{ record.title }}</h2>

      <div
        class="record__description-wrapper"
        :style="{ 
          'max-height': (isCollapsed ? 24 : descriptionHeight) + 'px',
          'white-space': isWhiteSpace ? 'nowrap' : undefined
        }"
      >
        <p ref="description">{{ record.description }}</p>
      </div>
    </div>

    <div class="record__actions">
      <div class="record__award">
        <h5>Вознаграждение</h5>
        <h2 class="record__currency">{{ record.award }}</h2>
      </div>
      <div class="record__dates">
        <h5>Даты</h5>
        <span class="record__date">{{ record.date?.toLocaleDateString('ru-RU', { month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' }) }}</span>
      </div>

      <div class="record__part">
        <Checkbox v-model="isParticipated" :label="
          isParticipated ? 'Участвую' : 'Участвовать'
        "/>
      </div>
    </div>
  </SurfaceComp>
</template>

<script lang="ts">
import { computed, defineComponent, nextTick, onMounted, ref, watch } from 'vue'

import SurfaceComp from '@/components/SurfaceComp.vue'
import Checkbox from '@/components/CheckboxComp.vue'
import { NewsRecord, User } from '@/utilities/types'
import { useStore } from 'vuex'

export default defineComponent({
  components: {
    SurfaceComp,
    Checkbox
  },
  props: {
    record: {
      type: Object as () => NewsRecord,
      required: true
    }
  },
  setup() {
    const store = useStore()

    const { value: user } = computed<User>(() => store.state.user)

    const isCollapsed = ref(true);
    const isWhiteSpace = ref(isCollapsed.value)
    const isParticipated = ref(false);

    const description = ref<null | HTMLElement>(null);
    const descriptionHeight = ref(24);

    const calculateHeight = () => {
          let totalHeight = 24;
          if (
            description.value
          ) {
            totalHeight += description.value.clientHeight

            descriptionHeight.value = Number(description.value.style.lineHeight.replace('px',''))
          }
          descriptionHeight.value = totalHeight;
    };

    watch(isCollapsed, () => {
      if (isCollapsed.value) {
        setTimeout(() => isWhiteSpace.value = isCollapsed.value, 200)
        calculateHeight()
      } 
      else {
        isWhiteSpace.value = isCollapsed.value
        nextTick(() => calculateHeight())
      }
    });

    onMounted(() => {
      calculateHeight();
    });

    return {
      user,
      isCollapsed,
      isParticipated,
      isWhiteSpace,
      description,
      descriptionHeight
    }
  },
})
</script>

<style lang="scss" scoped>
.record__wrapper {
  display: flex;
  flex-flow: column;
  gap: 16px;

  @media (min-width: 768px) {
    gap: 24px;
  }

  .record__text {
    cursor: pointer;
    max-width: 600px;

    h3 {
      font-style: normal;
      font-weight: 500;
      font-size: 16px;
      line-height: 150%;
      color: rgb(var(--text-primary--hover)); 
      margin-bottom: 8px;
    }

    h2 {
      font-weight: 600;
      font-size: 24px;
      line-height: 30px;
      letter-spacing: -0.32px;
      margin-bottom: 16px;

      @media (min-width: 768px) {
        font-size: 28px;
        line-height: 34px;
      }
    }

    .record__description-wrapper {
      overflow: hidden;
      transition: var(--transition);
      
      p {
        font-weight: 400;
        font-size: 18px;
        line-height: 150%;
        
        color: rgb(var(--text-secondary) / .8);
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
  }

  .record__actions {
    padding-top: 16px;
    border-top: 1px solid rgb(var(--divider--primary));

    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 16px 24px;

    @media (min-width: 768px) {
      gap: 16px 64px;
    }

    .record__award, .record__dates {
      display: flex;
      flex-flow: column;
      gap: 10px;
      justify-content: space-between;

      h5 {
        font-weight: 500;
        font-size: 14px;
        line-height: 17px;
        letter-spacing: -0.06px;
        color: var(--text-secondary / .4);

        @media (min-width: 768px) {
          font-size: 16px;
        }
      }
    }

    .record__award {
      .record__currency {
        font-weight: 600;
        font-size: 24px;
        line-height: 29px;
        letter-spacing: -0.02em;
        color: rgb(var(--text-primary--hover));

        @media (min-width: 768px) {
          font-size: 32px;
          line-height: 39px;
        }
      }
    }

    .record__dates {
      margin-right: auto;

      .record__date {
        font-weight: 500;
        font-size: 22px;
        line-height: 27px;
        letter-spacing: -0.02em;
        color: rgb(var(--text-primary));
      }
    }

    .record__part {
      margin-top: auto;
      background: rgb(var(--surface));
      border: 1px solid rgb(var(--divider-primary));
      padding: 14px 24px 16px 16px;
      border-radius: 16px;

      display: grid;
      place-items: center;
    }
  }
}
</style>
