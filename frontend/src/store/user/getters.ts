import { GetterTree } from "vuex";
import { User } from "@/utilities/types";  

const userModuleGetters = <GetterTree<User, any>>{
  getState: (context) => (key: keyof User) => {
    return context[key];
  },
};

export { userModuleGetters };