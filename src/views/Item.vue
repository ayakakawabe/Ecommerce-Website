<script setup lang="ts">
import type { ItemTypeLong } from '@/interfaces';
import { useRoute } from 'vue-router';

const route=useRoute();
const itemName=Number(route.params.id);

const item=new Map<number,ItemTypeLong>();
item.set(1,{id:1,name:"p1",price:1000,imgUrl:["http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png","http://placehold.jp/700x700.png"],description:"hogrhoge"});
const itemData=item.get(1) as ItemTypeLong;
const imgUrl:string[]=itemData.imgUrl.filter((url):url is string=>typeof url=="string");
</script>
<template>
    <div class="img_slide">
        <img v-bind:src="imgUrl[0]">
    </div>
    <div class="img_toolbar">
        <ul>
            <li v-for="smallImg in imgUrl">
                <img v-bind:src="smallImg">
            </li>
        </ul>
    </div>
    <p class="item_id">{{ itemData.id }}</p>
    <p class="name">{{ itemData.name }}</p>
    <p class="price_tag">PRICE</p>
    <p class="price">￥{{ itemData.price }}</p>
    <p class="question"><a href="#">この商品について問い合わせる</a></p>
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
    margin:30px 20px 20px 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.img_toolbar li{
    text-align: center;
}
.img_toolbar img{
    width: 100px;
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