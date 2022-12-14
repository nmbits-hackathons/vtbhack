import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import Maska from "maska";
import clickOutside from "./utilities/click-outside";


store.dispatch("user/init").finally(() => {
  createApp(App).use(store).use(router).use(Maska).directive("click-outside", clickOutside).mount("#app");
});