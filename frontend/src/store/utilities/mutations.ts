import { MutationTree } from "vuex";
import { initialState } from "./state";
import { Utilities } from "@/utilities/types";

const utilitiesModuleMutations = <MutationTree<Utilities>>{
  setState(context, { key, value }) {
    context[key as keyof Utilities] = value;
  },
  flushState(state) {
    Object.assign(state, initialState());
  },
}

export { utilitiesModuleMutations }