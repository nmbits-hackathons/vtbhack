import { MutationTree } from "vuex";
import { initialState } from "./state";
import { Wallet } from "@/utilities/types";

const walletModuleMutations = <MutationTree<Wallet>>{
  setState(context, { key, value }) {
    //TODO: fix
    (context as any)[key as keyof Wallet] = value;
  },
  flushState(state) {
    Object.assign(state, initialState());
  },
}

export { walletModuleMutations }