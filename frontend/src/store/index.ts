import { createStore } from "vuex";
import { userModule } from "./user";
import { utilitiesModule } from "./utilities";
import { walletModule } from "./wallet";

export default createStore({
  modules: {
    user: userModule,
    wallet: walletModule,
    utilities: utilitiesModule
  },
});
