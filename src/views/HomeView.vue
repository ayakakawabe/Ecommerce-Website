<script setup lang="ts">
import { onMounted,watch,ref,inject } from 'vue';
import { RouterLink } from 'vue-router';
import type {ItemType,NewsType,CategoryType} from "@/interfaces";

const slideShowImages=["http://placehold.jp/3d4070/ffffff/1920x1200.png","http://placehold.jp/703e3e/ffffff/1920x1200.png","http://placehold.jp/70673e/ffffff/1920x1200.png"];
let slideShowNumber=ref(0);
const changeSlideNumber=(slideNumber:number,num:number,Images:string[]):number=>{
    let result=slideNumber;
    if(slideNumber+num>=0 && slideNumber+num<Images.length){
        result=slideNumber+num;        
    }else if(slideNumber+num===Images.length){
        result=0;
    }else if(slideNumber+num===-1){
        result=Images.length-1;
    }
    return result;
};
let elementSlideShowImg:HTMLImageElement;
let toolbar0:HTMLElement;
let toolbar1:HTMLElement;
let toolbar2:HTMLElement;

onMounted(
    ():void=>{
    elementSlideShowImg=document.getElementById("slideshow_img") as HTMLImageElement;
    toolbar0=document.getElementsByClassName("slideshow_0")[0].children[0] as HTMLElement;
    toolbar1=document.getElementsByClassName("slideshow_1")[0].children[0] as HTMLElement;
    toolbar2=document.getElementsByClassName("slideshow_2")[0].children[0] as HTMLElement;
    toolbar0.style.color="#3a3838";
    setInterval(():void=>{
        slideShowNumber.value=changeSlideNumber(slideShowNumber.value,1,slideShowImages);
        },6000);
    }
);

const slideShowToolbarClick_0=():void=>{
    slideShowNumber.value=0;
};
const slideShowToolbarClick_1=():void=>{
    slideShowNumber.value=1;
};
const slideShowToolbarClick_2=():void=>{
    slideShowNumber.value=2;
};

watch(slideShowNumber,
():void=>{
    elementSlideShowImg.src=slideShowImages[slideShowNumber.value];
    if(slideShowNumber.value==0){
        toolbar0.style.color="#3a3838";
        toolbar1.style.color="#e3e3e3";
        toolbar2.style.color="#e3e3e3";
    }else if(slideShowNumber.value==1){
        toolbar0.style.color="#e3e3e3";
        toolbar1.style.color="#3a3838";
        toolbar2.style.color="#e3e3e3";
    }else{
        toolbar0.style.color="#e3e3e3";
        toolbar1.style.color="#e3e3e3";
        toolbar2.style.color="#3a3838";
    }
})

const newsList=new Map<number,NewsType>();
newsList.set(1,{date:"2023-01-01",title:"old news",description:"hogehoge"});
newsList.set(2,{date:"2024-1-1",title:"new news",description:"hogehoge"});

const newItems=new Map<number,ItemType>();
newItems.set(1,{id:1,name:"p1",price:1000,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
newItems.set(2,{id:2,name:"p2",price:1100,imgUrl:"http://placehold.jp/400x400.png",description:"hogehoge"});
newItems.set(3,{id:3,name:"p3",price:1200,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
newItems.set(4,{id:4,name:"p4",price:1300,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
newItems.set(5,{id:5,name:"p5",price:1400,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});
newItems.set(6,{id:6,name:"p6",price:1500,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhogr"});

const categoryList=inject("categoryList") as Map<string,CategoryType>;

</script>

<template>

    <div class="slideshow">
        <div class="slideshow_imgbox">
            <img id="slideshow_img" src="http://placehold.jp/3d4070/ffffff/1920x1200.png">
        </div>
        <div class="slideshow_toolbar">
            <div class="slideshow_0"><p v-on:click="slideShowToolbarClick_0">・</p></div>
            <div class="slideshow_1"><p v-on:click="slideShowToolbarClick_1">・</p></div>
            <div class="slideshow_2"><p v-on:click="slideShowToolbarClick_2">・</p></div>
        </div>
    </div>
    <section class="news_sec">
        <h1>NEWS</h1>
        <div class="news_box">
            <div class="news" v-for="[id,news] in newsList">
                <p>{{ news.date }}</p>
                <a href="#">{{ news.title }}</a>
            </div>
        </div>
        <p class="news_all"><a href="#">ニュース一覧を見る</a></p>
    </section>
    <section class="newitems">
        <h1>NEW ITEMS</h1>
        <div class="newitems_slide">
            <div class="item" v-for="[id,item] in newItems">
                <a href="#"><img v-bind:src=item.imgUrl><div class="item_description"><p class="name">{{ item.name }}</p><p class="price">￥{{ item.price }}</p></div></a>
            </div>
        </div>
    </section>
    <section>
        <h1>CATEGORY</h1>
        <ul class="category">
            <li v-for="[id,list] in categoryList" v-bind:key="id">
                <RouterLink v-bind:to="{name:'CategoryItems',params:{category:list.title}}"><img v-bind:src="list.imgUrl">{{ list.titleJP }}</RouterLink>
            </li>
        </ul>
    </section>    
</template>

<style scoped>
h1{
    padding-left: 25px;
}
/*slide show image*/
.slideshow{
    text-align: center;
}
.slideshow_imgbox img{
    width: 100%;
}
.slideshow_toolbar{
    display: flex;
    height: 50px;
    justify-content:center;
    position: relative;
    bottom: 5.5em;
}
.slideshow_toolbar *{
    margin: 0;
    padding: 0;
    color:#e3e3e3;
    font-weight: bold;
    font-size: 2.0em;
    cursor: pointer;
}

/*news*/
.news_sec{
    padding-bottom: 30px;
}
.news_box{
    display: flex;
    flex-direction: column-reverse;
}
.news{
    padding: 20px 40px 20px 40px;
}
.news a{
    padding: 10px 20px 10px 20px;
    color: #f25042;
}
.news_all{
    text-align: center;
}
.news_all a{
    border: solid #898989;
    border-radius: 5%;
    padding: 10px 20% 10px 20%;
    text-decoration: none;
    color: #3a3838;
}

/*new items*/
.newitems_slide{
    background-color: #eeeeee;
    width: 100%;
    display: flex;
    overflow-x: scroll;
}
.newitems_slide .item{
    background-color: #fbfbfb;
    margin: 15px;
    text-align: center;
    flex-shrink: 0;
}
.item a img{
    width: 400px;
    height: 400px;
}
.item a{
    display: block;
    text-decoration: none;
}
.item a .item_description{
    text-align: left;
    width: 400px;
    height: 320px;
}
.item_description .name{
    padding-top: 20px;
    padding-left: 30px;
} 
.item_description .price{
    padding-top: 190px;
    padding-left: 290px;
}

/*category*/
.category{
    margin-top: 50px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 0;
}
.category *{
    margin: 10px 10px 30px 10px;
    width: 40%;
    text-align: center;
}
.category li{
    list-style: none;

}
.category a{
    display: block;
    width: 80%;
    margin: auto;
    text-decoration: none;
}
.category img{
    width: 100%;
    margin: 0;
}
</style>