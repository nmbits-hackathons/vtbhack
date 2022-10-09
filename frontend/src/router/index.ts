import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/profile/:id",
    name: "Profile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ProfileView.vue"),
  },
  {
    path: "/market",
    name: "Marketplace",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/MarketplaceView.vue"),
  },
  {
    path: "/collection",
    name: "Collections",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CollectionsView.vue"),
  },
  {
    path: "/rating",
    name: "Rating",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/RatingView.vue"),
  },
  {
    path: "/record/:record",
    name: "Record",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/RecordView.vue"),
  },
  {
    path: "/exchange/:id",
    name: "Exchange",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/SwapView.vue"),
  },
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
