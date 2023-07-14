<script setup lang="ts">
import type { NewsType } from '@/interfaces';
import { fetchData } from "@/api";
import { ref } from "vue";
import { API_RootUrl } from '@/server_config';

const newsList=ref(new Map<number,NewsType>());
(async()=>{
    const response=await fetchData(`${API_RootUrl}/NewsList/`);
    if(response.data){
        const data=JSON.parse(response.data)["news"];
        for(let i=0;i<data.length;i++){
            newsList.value.set(Number(data[i]["id"]),{date:String(data[i]["date"]),title:String(data[i]["title"]),detail:String(data[i]["detail"])});
        }
    }else if(response.error){
        console.log(response.error);//エラー時の処理
    }
})();
</script>
<template>
    <img src="@/assets/image/news.png" class="topImg">
    <h1 class="categoryTitle">NEWS</h1>
    <section>
        <div class="news" v-for="[id,news] in newsList">
            <p class="date">{{ news.date }}</p>
            <RouterLink v-bind:to="{name:'News',params:{id:id}}">{{ news.title }}</RouterLink>
        </div>
    </section>
</template>

<style scoped>
.topImg{
    width: 100%;
}
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