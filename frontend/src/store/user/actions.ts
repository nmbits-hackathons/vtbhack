import { ActionTree } from "vuex";
import { User } from "@/utilities/types";
import { instance_user } from "@/utilities/config";

const userModuleActions = <ActionTree<User, null>>{
  init(context) {
    instance_user({
      method: 'GET',
      url: '/api/users/get_user_by_id/',
      params: {
        user_id: '1'
      }
    }).then((res) => {
      console.log(res);
    })
    .catch((e) => console.log(e))
  }
};

export { userModuleActions };