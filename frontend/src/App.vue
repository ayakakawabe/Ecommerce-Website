<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
import {reactive,provide,ref} from "vue";
import type { CategoryType,ItemType,ItemTypeAll } from './interfaces';
import { fetchData } from './api';


const itemList=new Map<number,ItemTypeAll>();
itemList.set(1,{id:1,name:"p1",price:1000,category:"lace",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(2,{id:2,name:"p1",price:1000,category:"accessories",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(3,{id:3,name:"p1",price:1000,category:"parts",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(4,{id:4,name:"p1",price:1000,category:"button",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(5,{id:5,name:"p1",price:1000,category:"paper",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(6,{id:6,name:"p1",price:1000,category:"doll",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(7,{id:7,name:"p1",price:1000,category:"interior",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(8,{id:8,name:"p1",price:1000,category:"original",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(9,{id:9,name:"p1",price:1000,category:"others",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});
itemList.set(10,{id:10,name:"p1",price:1000,category:"kitchen",imgUrl:["http://placehold.jp/8c3636/fffff/700x700.png","http://placehold.jp/8c3671/fffff/700x700.png","http://placehold.jp/75368c/fffff/700x700.png","http://placehold.jp/44368c/fffff/700x700.png","http://placehold.jp/366b8c/fffff/700x700.png","http://placehold.jp/368c7d/fffff/700x700.png","http://placehold.jp/368c50/fffff/700x700.png","http://placehold.jp/658c36/fffff/700x700.png","http://placehold.jp/8c7d36/fffff/700x700.png","http://placehold.jp/8c5436/fffff/700x700.png"],description:"hogrhoge"});

provide("itemList",reactive(itemList));

const newItems=new Map<number,ItemType>();
newItems.set(1,{id:1,name:"p1",price:1000,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhoge"});
newItems.set(2,{id:2,name:"p2",price:1100,imgUrl:"http://placehold.jp/400x400.png",description:"hogehoge"});
newItems.set(3,{id:3,name:"p3",price:1200,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhoge"});
newItems.set(4,{id:4,name:"p4",price:1300,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhoge"});
newItems.set(5,{id:5,name:"p5",price:1400,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhoge"});
newItems.set(6,{id:6,name:"p6",price:1500,imgUrl:"http://placehold.jp/400x400.png",description:"hogrhoge"});


const categoryList=ref(new Map<number,CategoryType>());

(async()=>{
  const response=await fetchData("http://127.0.0.1:8000/Category");
  if(response.data){
    const data=JSON.parse(response.data)["category"];
    console.log(data);
    for(let i=0;i<data.length;i++){
      let imgUrl= new URL(`./assets/image/category/${data[i]["imgpath"]}`,import.meta.url).href
      categoryList.value.set(data[i]["id"],{title:data[i]["title"],titleJP:data[i]["titlejp"],imgUrl:imgUrl})
    }
  }else if(response.error){
    console.log(response.error)
  }
})();

provide("categoryList",categoryList.value);

const navOpen=():void=>{
  document.getElementsByTagName("nav")[0].classList.add("nav_show");
}
const navClose=():void=>{
  document.getElementsByTagName("nav")[0].classList.remove("nav_show");
}

</script>

<template>
  <header>
    <div class="inner">
      <div class="header_logo">
          <RouterLink v-bind:to="{name:'Home'}" class="header_home"><span>Ivy</span></RouterLink>
      </div>
      <div class="header_link">
          <a href="Instagramのリンク" class="SNS_link"><img src="./assets/icon/Instagram_Glyph_Black.png" alt="Instagram"></a>
          <a href="Facebookのリンク" class="SNS_link"><img src="./assets/icon/f_logo_RGB-Black_58.png" alt="Facebook"></a>    
      </div>
      <div class="humburger">
          <img src="./assets/icon/hamburger.png" alt="menu" @click="navOpen">
      </div>
    </div>
    <nav class="nav">
      <div class="nav_close"><img src="./assets/icon/close_icon.png" alt="閉じる" v-on:click="navClose"></div>
      <div class="nav_category">
        <h1>CATEGORY</h1>
        <ul>
          <li v-for="[id,list] in categoryList" v-bind:key="id">
            <RouterLink v-bind:to="{name:'CategoryItems',params:{categoryId:id}}" v-on:click="navClose">{{ list.titleJP }}</RouterLink>
          </li>
        </ul>
      </div>
      <div class="nav_other">
        <h1>OTHER</h1>
        <ul>
          <li><RouterLink v-bind:to="{name:'AllNews'}" v-on:click="navClose">お知らせ</RouterLink></li>
          <li><RouterLink v-bind:to="{name:'Guide'}" v-on:click="navClose">ご利用ガイド</RouterLink></li>
          <li><RouterLink v-bind:to="{name:'Inquiry'}" v-on:click="navClose">お問い合わせ</RouterLink></li>
        </ul>
      </div>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
  <footer>
    <div class="line_friend">
        <h1>LINEでお知らせを受け取る</h1>
        <p class="line_add_button"><a href="#">LINEでお友達登録</a></p>
    </div>
    <nav>
    <div class="links">
      <h2>CATEGORY</h2>
      <div class="footer_caregory">
        <ul>
          <li>
            <RouterLink v-bind:to="{name:'AllItems'}">全商品一覧</RouterLink>
          </li>
          <li v-for="[id,list] in categoryList" v-bind:key="id">
            <RouterLink v-bind:to="{name:'CategoryItems',params:{categoryId:id}}">{{ list.titleJP }}</RouterLink>>
          </li>
        </ul>
      </div>
      <h2>SHOPPING GUIDE</h2>
      <div class="footer_guide">
        <ul>
          <li key="newsLink"><RouterLink v-bind:to="{name:'AllNews'}">お知らせ</RouterLink></li>
          <li><RouterLink v-bind:to="{name:'Guide'}">ご利用ガイド</RouterLink></li>
          <li><RouterLink v-bind:to="{name:'Inquiry'}">お問い合わせ</RouterLink></li>
        </ul>  
      </div>
      <h2>ONLINE STORE</h2>
      <div class="footer_online_">
        <ul>
          <li><a href="#">STORES</a></li>
          <li><a href="#">mercari</a></li>
        </ul>
      </div>
    </div>
    </nav>
    <div class="footer_card_info">
      <img src="./assets/icon/st_payments_docs_site_sticker_card_full_260x60.png">
    </div>
    <div class="footer_marks">
      <small>&copy; Ivy</small>
      <div class="footer_sns_link">
        <a href="Facebookのリンク"><img src="./assets/icon/f_logo_RGB-White_58.png"></a>
        <a href="Instagramのリンク"><img src="./assets/icon/Instagram_Glyph_White.png"></a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
h1{
    padding-left: 20px;
}
section{
    margin: 10% 0 10% 0;
}
/*header*/ 
header{
    padding: 0;
    margin: 0;
    height: 110px;
}
.header_home{
    text-decoration: none;
    display: block;
    margin-left: 2.5em;
}
.inner .header_home span{
    font-family: 'Lora', serif;
    text-decoration: none;
    font-size: 4em;
    letter-spacing: 0.4em;
    font-weight: 900;
}
.inner{
    position: fixed;
    background-color: #ffffff;
    width: 100%;
    height: 110px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.inner >:first-of-type{
    margin-right: auto;
}
.header_link img{
    width: 55px;
    padding-left: 9px;
}
.humburger img{
    width: 65px;
    cursor: pointer;
}
.nav_close img{
    width: 50px;
    cursor: pointer;
}

/*nav*/
.nav{
    height: 100vh;
    width: 370px;
    background-color: #323232;
    position: fixed;
    top: 0;
    right: -370px;
    padding-left: 30px;
}
.nav h1,.nav ul li a{
    color: #dedede;
    text-decoration: none;
}
.nav a:hover{
  color:#898989;
}
.nav_close{
    padding-top: 20px;
}
.nav ul li{
    list-style: none;
}

.nav_show{
    transform: translate3d(-370px,0,0);
}
.nav{
    transition: transform 0.3s;
}

/*footer*/
footer{
    background-color: #3a3838;
    color: #dedede;
}
.line_friend{
    text-align: center;
    padding-bottom: 60px;
    padding-top: 10px;
}
.line_friend a{
    text-decoration: none;
    padding: 10px;
    color: #dedede;
    background-color: #898989;
    border-radius: 5%;
}
.line_add_button{
    padding-top: 15px;
}
.links{
    padding: 0 40px 0 40px; 
    /*border-top: 1px solid #dedede;*/
}
.links h2::before{
    content:"";
    display: block;
    width: 100%;
    height: 1px;
    background-color: #dedede;
    margin-bottom: 20px;    
}
.links h2,.links div{
    padding-left: 40px;
}
.links a{
    color: #dedede;
    text-decoration: none;
}
.links li{
  list-style: none;
}
footer h1,footer h2{
    color: #dedede;
}
.footer_card_info{
    text-align: center;
    padding: 20px;
}
.footer_card_info img{
    width: 30%;
}
.footer_marks{
    display: flex;
    justify-content: center;
    text-align: right;
}
.footer_marks small{
    color: #dedede;
    padding: 0 20px 15px 20px;
}
.footer_sns_link{
    display: flex;
}
.footer_sns_link a{
    display: block;

}
.footer_sns_link img,.footer_sns_link a{
    width: 35px;
    padding-right: 10px;
}
footer div li :hover{
    color:#898989;
}
.line_add_button a:hover{
    color:#dedede;
}

</style>
