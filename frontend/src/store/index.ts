import { createStore } from "vuex";
import { userModule } from "./user";
import { walletModule } from "./wallet";

export default createStore({
  modules: {
    user: userModule,
    wallet: walletModule
  },
});
