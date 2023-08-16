<script setup lang="ts">
import type { ItemTypeLong } from '@/interfaces';
import { useRoute } from 'vue-router';
import { ref } from 'vue';

const route=useRoute();
const itemName=Number(route.params.id);

const item=new Map<number,ItemTypeLong>();
item.set(1,{id:1,name:"p1",price:1000,imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge",quantity:1});
const itemData=item.get(1) as ItemTypeLong;
const imgUrl:string[]=itemData.imgUrl.filter((url):url is string=>typeof url=="string");
const nowImgIndex=ref(0);
const changeImg=(index:number):void=>{
    nowImgIndex.value=index;
}
</script>
<template>
    <div class="img_slide">
        <img v-bind:src="imgUrl[nowImgIndex]">
    </div>
    <div class="img_toolbar">
        <ul>
            <li v-for="(smallImg,index) in imgUrl" v-bind:key="index">
                <img v-bind:src="smallImg" v-on:click="changeImg(index)">
            </li>
        </ul>
    </div>
    <p class="item_id">{{ itemData.id }}</p>
    <p class="name">{{ itemData.name }}</p>
    <p class="price_tag">PRICE</p>
    <p class="price">￥{{ itemData.price }}</p>
    <p class="question"><RouterLink v-bind:to="{name:'Inquiry'}">この商品について問い合わせる</RouterLink></p>
    <p class="buy_button"><button>buy</button></p>
    <p calss="description">{{ itemData.description }}</p>
</template>
<style scoped>
.img_slide{
    text-align: center;
    margin-top: 30px;
}

.img_slide img{
    width: 70%;
}
@media (min-width: 1280px) {
    .img_slide img{
        width: 45%;
    }
}

.img_toolbar ul{
    list-style: none;
    padding-left: 0;
    margin:30px 50px 20px 50px;
    display: flex;
    overflow: scroll;
}
.img_toolbar li{
    width:100px;
    margin: 7px;
}

.img_toolbar img{
    width: 100px;
}
.img_toolbar img:hover{
    cursor: pointer;
    opacity: 0.6;
}
p{
    margin: 40px;
}
.item_id{
    color: #9c9c9c;
}
.name{
    font-size: 40px;
}
.price_tag{
    margin-bottom: 0;
    color: #9c9c9c;
}
.price{
    font-size:30px;
    margin-top: 0;;
}
.question{
    text-align: right;
}
.buy_button{
    text-align: center;
}
button{
    width: 300px;
    height: 50px;
    background-color: #212121;
    color: #dedede;
    font-size: 20px;
}

</style>