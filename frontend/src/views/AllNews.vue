<script setup lang="ts">
import type { NewsType } from '@/interfaces';
const newsList=new Map<number,NewsType>();
newsList.set(1,{date:"2023-06-12",title:"【お知らせ】ホームページをリニューアルしました",description:"aaaaa"});
newsList.set(2,{date:"2023-01-01",title:"old news",description:"hogehoge"});
newsList.set(3,{date:"2024-01-01",title:"new news",description:"hogehoge"});
</script>
<template>
    <h1 class="categoryTitle">NEWS</h1>
    <section>
        <div class="news" v-for="[id,news] in newsList">
            <p class="date">{{ news.date }}</p>
            <RouterLink v-bind:to="{name:'News',params:{id:id}}">{{ news.title }}</RouterLink>
        </div>
    </section>
</template>

<style scoped>
section{
    margin: 40px;
    display: flex;
    flex-direction: column-reverse;
}
.news{
    padding: 20px 40px 20px 40px;
}
.news a{
    padding: 10px 20px 10px 20px;
    color: #cc7714;
    font-size: 20px;
}
.date{
    color: #9c9c9c;
}
</style>