import { utilitiesModuleState } from "./state"; 
import { utilitiesModuleGetters } from "./getters";
import { utilitiesModuleMutations } from "./mutations";
import { utilitiesModuleActions } from "./actions";

const utilitiesModule = {
  namespaced: true,

  state: utilitiesModuleState,
  getters: utilitiesModuleGetters,
  mutations: utilitiesModuleMutations,
  actions: utilitiesModuleActions
}

export { utilitiesModule }