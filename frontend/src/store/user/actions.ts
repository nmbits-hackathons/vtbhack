import { ActionTree } from "vuex";
import { User } from "@/utilities/types";
import { instance_user } from "@/utilities/config";

const userModuleActions = <ActionTree<User, null>>{
  init(context) {
    return new Promise((resolve, reject) => {
      instance_user({
        method: 'GET',
        url: '/api/users/get_user_by_id/',
        params: {
          user_id: '6'
        }
      }).then((res) => {
        Object.entries(res.data).forEach(([key, field]) => {
          context.commit('setState', {
            key: key,
            value: field
          })
        });
        resolve(res)
      })
      .catch((e) => reject(e))
    })
  }
};

export { userModuleActions };