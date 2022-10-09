import { ActionTree } from "vuex";
import { Utilities } from "@/utilities/types";
import { instance_user } from "@/utilities/config";

const utilitiesModuleActions = <ActionTree<Utilities, null>>{
  init(context) {
    instance_user({
      method: 'GET',
      url: '/api/events/get_events/',
      params: {
        left: 0,
        right: 10
      }
    }).then((res) => {
      context.commit('setState', {
        key: 'events',
        value: res.data.series
      })
    })
    .catch((e) => console.log(e))
  }
};

export { utilitiesModuleActions };