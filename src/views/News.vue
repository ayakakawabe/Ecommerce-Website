<script setup lang="ts">
import { useRoute } from 'vue-router';
import type { NewsType } from '@/interfaces';

const route=useRoute();
const id=Number(route.params.id);

const newsList=new Map<number,NewsType>();
newsList.set(1,{date:"2023-06-12",title:"【お知らせ】ホームページをリニューアルしました",description:"aaaaa"});
const newsData=newsList.get(1) as NewsType;
</script>

<template>
    <h1 class="categoryTitle">NEWS</h1>
    <section>
        <p class="date">{{ newsData.date }}</p>
        <h2 class="title">{{ newsData.title }}</h2>
        <p class="description">{{ newsData.description }}</p>
    </section>
</template>

<style scoped>
section{
    margin: 40px;
}
.date{
    color: #9c9c9c;
}
.title{
    font-size: x-large;
}
.description{
    margin: 30px;
}
</style>