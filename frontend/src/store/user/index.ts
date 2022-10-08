import { userModuleState } from "./state"; 
import { userModuleGetters } from "./getters";
import { userModuleMutations } from "./mutations";
import { userModuleActions } from "./actions";

const userModule = {
  namespaced: true,

  state: userModuleState,
  getters: userModuleGetters,
  mutations: userModuleMutations,
  actions: userModuleActions
}

export { userModule }