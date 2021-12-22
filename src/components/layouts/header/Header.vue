<template>
  <div>
  <div class="header-top fixed-top">
  <div class="container">
    <div class="row">
      <div class="col">
      <ul>
      <li class="nav-item"><router-link to="/" class="nav-link link-dark px-2 active" aria-current="page"><p style="color:#333;"><i class="fas fa-home"></i>回首頁</p></router-link></li>
      </ul>
      </div>
      <div class="col-md-auto ml-4 pt-2">
        <div class="row">
          <div class="col">
            <ul class="header-top-link">
            <li class="nav-item  mr-4">Vita微光心靈塔羅</li>
            <li class="nav-item"><a href="#" class="px-2"><i class="fab fa-facebook-square"></i></a></li>
            <li class="nav-item"><a href="#" class="px-2"><i class="fab fa-instagram"></i></a></li>
            </ul>
          </div>
          <div class="col">
            <ul class="header-top-link">
            <li class="nav-item">微光文創工作室</li>
            <li class="nav-item"><i class="fab fa-facebook-square"></i></li>
            <li class="nav-item"><a href="#" class="px-2"><i class="fab fa-instagram"></i></a></li>
          </ul>
          </div>
        </div>
      </div>
      <div class="col col-lg-2">
      <router-link to="/booking"><h4 class="booking-icon">立即預約</h4></router-link>
      </div>
    </div>
  </div>
</div>
   <!-- <div class="banner-block">
      
    </div>-->
  <div class="topnav border-bottom pt-4">
  <div class="container">
    <a href="/" class="logo">
      <img src="../../../img/logo-wh.png" width="38">
    </a>
    <div class="container">
      <nav class="mb-4">
        <div class="container">
           <ul class="nav header-menu">
            <li class="nav-item"><router-link to="/">首頁</router-link></li>
            <li class="nav-item"><router-link to="/about">關於微光</router-link></li>
            <li class="nav-item"><router-link to="/product-catalogue">商品頁面</router-link></li>
            <li class="nav-item"><router-link to="/rent">租賃方案</router-link></li>
            <li class="nav-item"><router-link to="/creative">文創商品</router-link></li>
            <li class="nav-item"><router-link to="/course">手作課程</router-link></li>
            <li class="nav-item"><router-link to="/news">歷年活動</router-link></li>
            <li class="nav-item"><router-link to="/cart"><i class="fas fa-shopping-cart"></i></router-link></li>
          </ul>
        </div>
      </nav>
    </div>
  </div>
  </div>
</div>
</template>

<script>
export default {
  name: "Header",
};


</script>
<style scoped>
  .header-top-link ul,.header-top-link li {
  margin: 0;
  padding: 0;
  justify-content: center;
  display: table-cell;
  vertical-align: middle;

}
</style>
