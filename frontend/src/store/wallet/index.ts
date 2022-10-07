import { walletModuleActions } from "./actions";
import { walletModuleGetters } from "./getters";
import { walletModuleMutations } from "./mutations";
import { walletModuleState } from "./state";

const walletModule = {
  namespaced: true,

  state: walletModuleState,
  getters: walletModuleGetters,
  mutations: walletModuleMutations,
  actions: walletModuleActions
}

export { walletModule }