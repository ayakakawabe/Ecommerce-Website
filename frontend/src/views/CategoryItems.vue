<script setup lang="ts">
import type { ItemType,CategoryType } from '@/interfaces';
import { watch,inject, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route=useRoute();
const categoryList=inject("categoryList") as Map<number,CategoryType>;

let categoryId:number;

let nowCategoryData:CategoryType;
let categoryTitle:string;
let categoryImgUrl:string;

const changeCategoryData=(nowCategoryId:number):void=>{
    nowCategoryData=categoryList.get(nowCategoryId) as CategoryType;
    categoryTitle=nowCategoryData["title"];
    categoryImgUrl=nowCategoryData["imgUrl"];
};

categoryId=Number(route.params.categoryId);
changeCategoryData(categoryId);

const allItemList=new Map<number,ItemType>();
allItemList.set(1,{id:1,name:"p1",price:1000,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(2,{id:2,name:"p2",price:1100,imgUrl:"http://placehold.jp/400x400.png",description:"hogehoge"});
allItemList.set(3,{id:3,name:"p3",price:1200,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(4,{id:4,name:"p4",price:1300,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(5,{id:5,name:"p5",price:1400,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
allItemList.set(6,{id:6,name:"p6",price:1500,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
let topImgElement:HTMLImageElement;
onMounted(()=>{
    topImgElement=document.getElementsByClassName("topImage")[0].firstElementChild as HTMLImageElement;
});

watch(route,():void=>{
    categoryId=Number(route.params.categoryId);
    console.log(categoryId);
    changeCategoryData(categoryId);
    //商品データの変更も追加する   
});

</script>

<template>
    <div class="topImage">
        <img v-bind:src="categoryImgUrl">
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
a{
    text-decoration: none;
}
</style>