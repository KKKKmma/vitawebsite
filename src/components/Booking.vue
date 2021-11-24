<template>
<div class="container pb-5 mb-2">
  <div class="container-fluid">
    <div class="titlestyles d-flex py-4 my-4">
      <h1 class="titile-style"><img src="../img/titleicon.png">商品預訂清單</h1>
    </div>
    <div class="checkout-nav pb-4">
        <div class="step active">
          <span class="badge"><span class="text">1</span></span>
          <span>選定商品</span>
        </div>
        <div class="step">
          <span class="badge"><span class="text">2</span></span>
          <span>填寫資料</span>
        </div>
        <div class="step">
          <span class="badge"><span class="text">3</span></span>
          <span>訂單確認</span>
        </div>
    </div>
     <!-- Cart Item-->
    <div class="cart-item d-md-flex justify-content-between">
        <div class="px-3 my-3">
            <a class="cart-item-product" href="#">
                <div class="cart-item-product-thumb"><img src="../images/album_1.jpg" alt="Product"></div>
                <div class="cart-item-product-info">
                    <h4 class="cart-item-product-title">{{producttitle}}</h4><span><strong>編號:</strong> ASK123</span><span><strong>租期:</strong> 2021/11/24</span>
                </div>
            </a>
        </div>
        <div class="px-3 my-3 text-center">
            <div class="cart-item-label">數量</div>
            <div class="count-input">1</div>
        </div>
        <div class="px-3 my-3 text-center">
            <div class="cart-item-label">價格</div><span class="text-xl font-weight-medium">$1,450.00</span>
        </div>
    </div>
    <!-- Cart Item-->
    <div class="cart-item d-md-flex justify-content-between">
        <div class="px-3 my-3">
            <a class="cart-item-product" href="#">
                <div class="cart-item-product-thumb"><img src="../images/album_1.jpg" alt="Product"></div>
                <div class="cart-item-product-info">
                    <h4 class="cart-item-product-title">{{producttitle}}</h4><span><strong>編號:</strong> ASK123</span><span><strong>租期:</strong> 2021/11/24</span>
                </div>
            </a>
        </div>
        <div class="px-3 my-3 text-center">
            <div class="cart-item-label">數量</div>
            <div class="count-input">1</div>
        </div>
        <div class="px-3 my-3 text-center">
            <div class="cart-item-label">價格</div><span class="text-xl font-weight-medium">$1,450.00</span>
        </div>
    </div>
    <div class="container-fluid text-center">
      <div class="row">
        <div class="col-lg-6"></div>
        <div class="col-lg-3">總計 NT1000</div>
        <div class="col-lg-3">訂金預付NT300</div>
      </div>
    </div>
    <div class="container productotice py-4 mt-4">
      <p>透過線上表單填寫登記，同時可以幫您保留喜歡的服飾與配件，</p>
      <p>需要取消預約的顧客請您務必在預定的72小時前來電告知，否則無法取消訂單並且無法退還押金。</p>
      <p>取消成立後7天內幫您處理退還定金的手續。</p>
      <p>預約當天下雨取消預約是無法退還押金。因天氣預報顯示預約當天下雨而更改日期或者時間也無法退還押金。</p>
      <p>TEL:080-9759-5005</p>
      <p>為了其他客戶的權益，取消請盡早聯絡我們，謝謝！</p>
    </div>
    <div class="row pt-4">
      <div class="container-fluid text-center col"><router-link to="/product-catalogue"><button  type="button" class="btn btn-lg check-btn">繼續選擇</button></router-link></div>
      <div class="container-fluid text-center col"><button  type="button" class="btn btn-lg more-btn">下一步填寫資料</button></div>
    </div>
  </div>
  <section>
      <h1>顯示測試</h1>
      <Search v-model:inputText="searchText" />
      {{ searchText }}
  </section>
</div>
</template>
<script>
import Search from "../components/Search.vue";
import { ref } from "vue";
export default {
  name: 'Booking',
  components: {
  Search,
  },
  setup() {
    const producttitle = '夏日和服享受清涼(單衣)';
    const searchText = ref("");
    return { 
      searchText,
      producttitle
    };
  },
};
</script>

<style scoped>
.productotice{
  background-color: #E0E0E0;
  padding: 40px;
  padding-top: 70px;
}
h4.cart-item-product-title{
  letter-spacing: 3px;
}
.checkout-nav {
    text-align: center;
    margin-top: 30px;
    margin-bottom: 30px;
}
.checkout-nav .step {
    display: inline-block;
    vertical-align: top;
    width: 240px;
    max-width: 33%;
    margin-left: -2px;
    margin-right: -2px;
    color: black;
}

.checkout-nav .step .badge {
    position: relative;
    background-color: transparent;
    height: 50px;
    line-height: 50px;
    padding: 0;
}
.checkout-nav .step:first-child .badge::before {
    width: 50%;
    left: 50%;
}
.checkout-nav .step .badge::before {
    content: " ";
    background-color: #CCCCCC;
    height: 2px;
    width: 100%;
    position: absolute;
    left: 0;
    top: 50%;
    margin-top: -1px;
    z-index: 0;
}
.checkout-nav .step.visited .badge::after, .checkout-nav .step.active .badge::after {
    background-color: #9DAAB2;
}
.checkout-nav .step .badge .text {
    position: absolute;
    width: 100%;
    z-index: 1;
}
.checkout-nav .step .badge::after {
    -webkit-border-radius: 15px;
    -moz-border-radius: 15px;
    -ms-border-radius: 15px;
    border-radius: 15px;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    content: " ";
    background-color: #CCCCCC;
    height: 30px;
    width: 30px;
    left: 50%;
    top: 50%;
    position: absolute;
    z-index: 0;
}
.checkout-nav .step .badge {
    position: relative;
    background-color: transparent;
    height: 50px;
    line-height: 50px;
    padding: 0;
}
.checkout-nav .step span {
    display: block;
    padding: 0 5px;
}
.checkout-nav .step {
    display: inline-block;
    vertical-align: top;
    width: 240px;
    max-width: 33%;
    margin-left: -2px;
    margin-right: -2px;
    color: black;
}

/*購物車清單*/
.product-card {
  position: relative;
  max-width: 380px;
  padding-top: 12px;
  padding-bottom: 43px;
  transition: all 0.35s;
  border: 1px solid #e7e7e7;
}
.product-card .product-head {
  padding: 0 15px 8px;
}
.product-card .product-head .badge {
  margin: 0;
}
.product-card .product-thumb {
  display: block;
}
.product-card .product-thumb > img {
  display: block;
  width: 100%;
}
.product-card .product-card-body {
  padding: 0 20px;
  text-align: center;
}
.product-card .product-meta {
  display: block;
  padding: 12px 0 2px;
  transition: color 0.25s;
  color: rgba(140, 140, 140, .75);
  font-size: 12px;
  font-weight: 600;
  text-decoration: none;
}
.product-card .product-meta:hover {
  color: #8c8c8c;
}
.product-card .product-title {
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: bold;
}
.product-card .product-title > a {
  transition: color 0.3s;
  color: #343b43;
  text-decoration: none;
}
.product-card .product-title > a:hover {
  color: #ac32e4;
}
.product-card .product-price {
  display: block;
  color: #404040;
  font-family: 'Montserrat', sans-serif;
  font-weight: normal;
}
.product-card .product-price > del {
  margin-right: 6px;
  color: rgba(140, 140, 140, .75);
}
.product-card .product-buttons-wrap {
  position: absolute;
  bottom: -20px;
  left: 0;
  width: 100%;
}
.product-card .product-buttons {
  display: table;
  margin: auto;
  background-color: #fff;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .11);
}
.product-card .product-button {
  display: table-cell;
  position: relative;
  width: 50px;
  height: 40px;
  border-right: 1px solid rgba(231, 231, 231, .6);
}
.product-card .product-button:last-child {
  border-right: 0;
}
.product-card .product-button > a {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: all 0.3s;
  color: #404040;
  font-size: 16px;
  line-height: 40px;
  text-align: center;
  text-decoration: none;
}
.product-card .product-button > a:hover {
  background-color: #ac32e4;
  color: #fff;
}
.product-card:hover {
  border-color: transparent;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .09);
}
.product-category-card {
  display: block;
  max-width: 400px;
  text-align: center;
  text-decoration: none !important;
}
.product-category-card .product-category-card-thumb {
  display: table;
  width: 100%;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .09);
}
.product-category-card .product-category-card-body {
  padding: 20px;
  padding-bottom: 28px;
}
.product-category-card .main-img, .product-category-card .thumblist {
  display: table-cell;
  padding: 15px;
  vertical-align: middle;
}
.product-category-card .main-img > img, .product-category-card .thumblist > img {
  display: block;
  width: 100%;
}
.product-category-card .main-img {
  width: 65%;
  padding-right: 10px;
}
.product-category-card .thumblist {
  width: 35%;
  padding-left: 10px;
}
.product-category-card .thumblist > img:first-child {
  margin-bottom: 6px;
}
.product-category-card .product-category-card-meta {
  display: block;
  padding-bottom: 9px;
  color: rgba(140, 140, 140, .75);
  font-size: 11px;
  font-weight: 600;
}
.product-category-card .product-category-card-title {
  margin-bottom: 0;
  transition: color 0.3s;
  color: #343b43;
  font-size: 18px;
}
.product-category-card:hover .product-category-card-title {
  color: #ac32e4;
}
.product-gallery {
  position: relative;
  padding: 45px 15px 0;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .09);
}
.product-gallery .gallery-item::before {
  display: none !important;
}
.product-gallery .gallery-item::after {
  box-shadow: 0 8px 24px 0 rgba(0, 0, 0, .26);
}
.product-gallery .video-player-button, .product-gallery .badge {
  position: absolute;
  z-index: 5;
}
.product-gallery .badge {
  top: 15px;
  left: 15px;
  margin-left: 0;
}
.product-gallery .video-player-button {
  top: 0;
  right: 15px;
  width: 60px;
  height: 60px;
  line-height: 60px;
}
.product-gallery .product-thumbnails {
  display: block;
  margin: 0 -15px;
  padding: 12px;
  border-top: 1px solid #e7e7e7;
  list-style: none;
  text-align: center;
}
.product-gallery .product-thumbnails > li {
  display: inline-block;
  margin: 10px 3px;
}
.product-gallery .product-thumbnails > li > a {
  display: block;
  width: 94px;
  transition: all 0.25s;
  border: 1px solid transparent;
  background-color: #fff;
  opacity: 0.75;
}
.product-gallery .product-thumbnails > li:hover > a {
  opacity: 1;
}
.product-gallery .product-thumbnails > li.active > a {
  border-color: #ac32e4;
  cursor: default;
  opacity: 1;
}
.product-meta {
  padding-bottom: 10px;
}
.product-meta > a, .product-meta > i {
  display: inline-block;
  margin-right: 5px;
  color: rgba(140, 140, 140, .75);
  vertical-align: middle;
}
.product-meta > i {
  margin-top: 2px;
}
.product-meta > a {
  transition: color 0.25s;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
}
.product-meta > a:hover {
  color: #8c8c8c;
}
.cart-item {
  position: relative;
  margin-bottom: 30px;
  padding: 0 50px 0 10px;
  background-color: #fff;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .09);
}
.cart-item .cart-item-label {
  display: block;
  margin-bottom: 15px;
  color: #8c8c8c;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
}
.cart-item .cart-item-product {
  display: table;
  width: 420px;
  text-decoration: none;
}
.cart-item .cart-item-product-thumb, .cart-item .cart-item-product-info {
  display: table-cell;
  vertical-align: top;
}
.cart-item .cart-item-product-thumb {
  width: 110px;
}
.cart-item .cart-item-product-thumb > img {
  display: block;
  width: 100%;
}
.cart-item .cart-item-product-info {
  padding-top: 5px;
  padding-left: 15px;
}
.cart-item .cart-item-product-info > span {
  display: block;
  margin-bottom: 2px;
  color: #404040;
  font-size: 12px;
}
.cart-item .cart-item-product-title {
  margin-bottom: 8px;
  transition: color, 0.3s;
  color: #343b43;
  font-size: 16px;
  font-weight: bold;
}
.cart-item .cart-item-product:hover .cart-item-product-title {
  color: #ac32e4;
}
.cart-item .count-input {
  display: inline-block;
  width: 85px;
}
.cart-item .remove-item {
  right: -10px !important;
}
@media (max-width: 991px) {
  .cart-item {
    padding-right: 30px;
  }
  .cart-item .cart-item-product {
    width: auto;
  }
}
@media (max-width: 768px) {
  .cart-item {
    padding-right: 10px;
    padding-bottom: 15px;
  }
  .cart-item .cart-item-product {
    display: block;
    width: 100%;
    text-align: center;
  }
  .cart-item .cart-item-product-thumb, .cart-item .cart-item-product-info {
    display: block;
  }
  .cart-item .cart-item-product-thumb {
    margin: 0 auto 10px;
  }
  .cart-item .cart-item-product-info {
    padding-left: 0;
  }
  .cart-item .cart-item-label {
    margin-bottom: 8px;
  }
}
.comparison-table {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  -ms-overflow-style: -ms-autohiding-scrollbar;
}
.comparison-table table {
  min-width: 750px;
  table-layout: fixed;
}
.comparison-table .comparison-item {
  position: relative;
  margin-bottom: 10px;
  padding: 13px 12px 18px;
  background-color: #fff;
  text-align: center;
  box-shadow: 0 12px 20px 1px rgba(64, 64, 64, .09);
}
.comparison-table .comparison-item .comparison-item-thumb {
  display: block;
  width: 80px;
  margin-right: auto;
  margin-bottom: 12px;
  margin-left: auto;
}
.comparison-table .comparison-item .comparison-item-thumb > img {
  display: block;
  width: 100%;
}
.comparison-table .comparison-item .comparison-item-title {
  display: block;
  margin-bottom: 14px;
  transition: color 0.25s;
  color: #404040;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
}
.comparison-table .comparison-item .comparison-item-title:hover {
  color: #ac32e4;
}
.remove-item {
  display: block;
  position: absolute;
  top: -5px;
  right: -5px;
  width: 22px;
  height: 22px;
  padding-left: 1px;
  border-radius: 50%;
  background-color: #ff5252;
  color: #fff;
  line-height: 23px;
  text-align: center;
  box-shadow: 0 3px 12px 0 rgba(255, 82, 82, .5);
  cursor: pointer;
}
.card-wrapper {
  margin: 30px -15px;
}
@media (max-width: 576px) {
  .card-wrapper .jp-card-container {
    width: 260px !important;
  }
  .card-wrapper .jp-card {
    min-width: 250px !important;
  }
}
</style>