import { GetterTree } from "vuex";
import { User } from "@/utilities/types";  

const userModuleGetters = <GetterTree<User, any>>{
  getState: (context) => (key: keyof User) => {
    return context[key];
  },
  getFullName(context) {
    return `${context.first_name} ${context.last_name}`
  }
};

export { userModuleGetters };