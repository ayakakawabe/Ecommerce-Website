import { createRouter, createWebHistory } from 'vue-router';
import type { RouteRecordRaw } from 'vue-router';
import HomeView from '@/views/HomeView.vue';

const routerSetting:RouteRecordRaw[]=[
  {
    path:"/",
    name:"Home",
    component:HomeView
  },
  {
    path:"/allItems",
    name:"AllItems",
    component:()=>{
      return import("@/views/AllItems.vue");
    }
  },
  {
    path:"/category/:category",
    name:"CategoryItems",
    component:()=>{
      return import("@/views/CategoryItems.vue");
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routerSetting
});

export default router;
