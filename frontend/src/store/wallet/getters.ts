import { GetterTree } from "vuex";
import { Wallet } from "@/utilities/types";  

const walletModuleGetters = <GetterTree<Wallet, any>>{
  getState: (context) => (key: keyof Wallet) => {
    return context[key];
  },
};

export { walletModuleGetters };