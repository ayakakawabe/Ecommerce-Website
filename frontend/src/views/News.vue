<script setup lang="ts">
import { useRoute } from 'vue-router';
import type { NewsType } from '@/interfaces';
import { fetchData } from '@/api';
import {ref} from 'vue';
import { API_RootUrl } from '@/server_config';


const route=useRoute();
const id=Number(route.params.id);

const newsData=ref<NewsType>({date:"",title:"",detail:""});
(async()=>{
    const response=await fetchData(`${API_RootUrl}/NewsData/`+id);
    if(response.data){
        const data=JSON.parse(response.data);
        newsData.value=data;
    }else if(response.error){
        console.log(response.error);
    }
})();

const formatText=(text:string):string=>{
    return text.split("\\r\\n").join("<br>");
}

</script>

<template>
    <h1 class="categoryTitle">NEWS</h1>
    <section>
        <p class="date">{{ newsData.date }}</p>
        <h2 class="title">{{ newsData.title }}</h2>
        <p class="detail" v-html="formatText(newsData.detail)"></p>
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
    margin: 30px 0 60px 0;
}
.detail{
    margin: 30px;
}
</style>