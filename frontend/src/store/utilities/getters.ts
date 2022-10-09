import { GetterTree } from "vuex";
import { Utilities } from "@/utilities/types";  

const utilitiesModuleGetters = <GetterTree<Utilities, any>>{
  getState: (context) => (key: keyof Utilities) => {
    return context[key];
  },
};

export { utilitiesModuleGetters };