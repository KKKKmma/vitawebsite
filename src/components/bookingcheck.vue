<template>
<div class="container-fluid">
    <div class="titlestyles d-flex py-4 my-4">
      <h1 class="titile-style"><img src="../img/titleicon.png">訂單明細</h1>
    </div>
	<div class="checkout-nav pb-4">
		<div class="step">
			<span class="badge"><span class="text">1</span></span>
			<span>選定商品</span>
		</div>
		<div class="step">
			<span class="badge"><span class="text">2</span></span>
			<span>填寫資料</span>
		</div>
		<div class="step active">
			<span class="badge"><span class="text">3</span></span>
			<span>訂單明細</span>
		</div>
		<div class="step">
			<span class="badge"><span class="text">4</span></span>
			<span>付款結果</span>
		</div>
	</div>
    <div class="information-card">
    <div>訂購人資料</div>
		<div class="row form-group">
			<div class="col-6 title-strong">姓名</div>
			<div class="col-6 text-muted ">test</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">電話</div>
			<div class="col-6 text-muted ">0912345678</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">訂單編號</div>
			<div class="col-6 text-muted ">U211192808</div>
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
        <div class="cart-item-label">價格</div><span class="text-xl font-weight-medium">$1,450</span>
    </div>
</div>
    <div class="container-fluid text-center">
      <div class="row">
        <div class="col-lg-6"></div>
        <div class="col-lg-3">總計 NT1000</div>
        <div class="col-lg-3">訂金預付NT300</div>
      </div>
    </div>
<div class="container-fluid text-center col"><router-link to="pay"><button  type="button" class="btn btn-lg more-btn">下一步確認付款</button></router-link></div>
</div>
</template>
<style scoped>
	.information-card {
    background-color: #fff;
    -webkit-box-shadow: 0 0 50px rgb(0 0 0 / 30%);
    box-shadow: 0 0 50px rgb(0 0 0 / 30%);
    padding: 2em 4em;
    margin-bottom: 4em;
}
.information-card >.row {
    border-bottom: 1px solid #ccc;
    padding: 0 0 1em 0;
}
.form-group {
    margin-bottom: 1em;
}
.title-strong {
	font-weight: 600;
}
.text-muted {
    color: #636c72;
}
</style>