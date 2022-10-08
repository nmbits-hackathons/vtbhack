import { MutationTree } from "vuex";
import { initialState } from "./state";
import { User } from "@/utilities/types";

const userModuleMutations = <MutationTree<User>>{
  setState(context, { key, value }) {
    context[key as keyof User] = value;
  },
  flushState(state) {
    Object.assign(state, initialState());
  },
}

export { userModuleMutations }