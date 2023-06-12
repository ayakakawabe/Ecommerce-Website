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
  {
    path:"/item/:id",
    name:"Item",
    component:()=>{
      return import("@/views/Item.vue")
    }
  },
  {
    path:"/allnews",
    name:"AllNews",
    component:()=>{
      return import("@/views/AllNews.vue")
    }
  },{
    path:"/news/:id",
    name:"News",
    component:()=>{
      return import("@/views/News.vue")
    }
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routerSetting,
  scrollBehavior(to,from,savedPosition){
    return {top:0}
  },
});

export default router;
