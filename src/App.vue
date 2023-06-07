<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';

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
      <div class="nav_close"><img src="./assets/icon/close_icon.png" alt="閉じる" @click="navClose"></div>
      <div class="nav_category">
        <p>CATEGORY</p>
        <ul>
          <li><a href="#">レース・布</a></li>
          <li><a href="#">アクセサリー</a></li>
          <li><a href="#">アクセサリーパーツ</a></li>
          <li><a href="#">ボタン</a></li>
          <li><a href="#">ペーパー（ポストカード・雑誌）</a></li>
          <li><a href="#">ドール</a></li>
          <li><a href="#">インテリア雑貨</a></li>
          <li><a href="#">キッチン雑貨</a></li>
          <li><a href="#">Ivyオリジナル</a></li>
          <li><a href="#">その他</a></li>
        </ul>
      </div>
      <div class="nav_other">
        <P>OTHER</P>
        <ul>
          <li><a href="#">ご利用ガイド</a></li>
          <li><a href="#">お問い合わせ</a></li>
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
    <div class="links">
      <h2>CATEGORY</h2>
      <div class="footer_caregory">
        <RouterLink v-bind:to="{name:'AllItems'}">全商品一覧</RouterLink>
        <p><a href="#">レース・布</a></p>
        <p><a href="#">アクセサリー</a></p>
        <p><a href="#">アクセサリーパーツ</a></p>
        <p><a href="#">ボタン</a></p>
        <p><a href="#">ペーパー（ポストカード・雑誌）</a></p>
        <p><a href="#">ドール</a></p>
        <p><a href="#">インテリア雑貨</a></p>
        <p><a href="#">キッチン雑貨</a></p>
        <p><a href="#">Ivyオリジナル</a></p>
        <p><a href="#">その他</a></p>
      </div>
      <h2>SHOPPING GUIDE</h2>
      <div class="footer_guide">
        <p><a href="#">ご利用ガイド</a></p>
        <p><a href="#">セキュリティポリシー</a></p>
        <p><a href="#">お問い合わせ</a></p>
      </div>
      <h2>ONLINE STORE</h2>
      <div class="footer_online_">
        <p><a href="#">STORES</a></p>
        <p><a href="#">mercari</a></p>
      </div>
    </div>
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
    width: 350px;
    background-color: #323232;
    position: fixed;
    top: 0;
    right: -350px;
    padding-left: 30px;
}
.nav p,.nav ul li a{
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
    transform: translate3d(-350px,0,0);
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
footer div p :hover{
    color:#898989;
}
.line_add_button a:hover{
    color:#dedede;
}

</style>
