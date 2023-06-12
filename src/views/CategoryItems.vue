<script setup lang="ts">
import type { ItemType } from '@/interfaces';
import { watch } from 'vue';
import { useRoute, type Router} from 'vue-router';

const route=useRoute();
let categoryTitle:string;
categoryTitle=route.params.category as string;

const allItemList=new Map<number,ItemType>();
allItemList.set(1,{id:1,name:"p1",price:1000,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(2,{id:2,name:"p2",price:1100,imgUrl:"http://placehold.jp/400x400.png",description:"hogehoge"});
allItemList.set(3,{id:3,name:"p3",price:1200,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(4,{id:4,name:"p4",price:1300,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(5,{id:5,name:"p5",price:1400,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(6,{id:6,name:"p6",price:1500,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});

watch(route,():void=>{
    categoryTitle=route.params.category as string; 
    //商品データの変更も追加する   
});

</script>

<template>
    <div class="topImage">
        <img src="http://placehold.jp/3d4070/ffffff/1920x1200.png">
    </div>
    <h1 class="categoryTitle">{{ categoryTitle }}</h1>
    <div>
        <ul class="itemList">
            <li v-for="[id,item] in allItemList">
                <RouterLink v-bind:to="{name:'Item',params:{id:item.id}}"><img v-bind:src="item.imgUrl"><div class="description"><p class="name">{{ item.name }}</p><p class="price">￥{{ item.price }}</p></div></RouterLink></li>
        </ul>
    </div>
</template>

<style scoped>
li{
    list-style: none;
    background-color: #ededed;
    margin: 20px;
}
ul{
    padding-left: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}
.description{
    width: 400px;
    height: 400px;
    display: flex;
    flex-direction: column;
}
.description *{
    margin: 0;
}
.description .name{
    padding: 60px 40px 40px 40px;
}
.description .price{
    text-align:right;
    margin-top: auto;
    padding: 40px 40px 60px 40px;
}
</style>