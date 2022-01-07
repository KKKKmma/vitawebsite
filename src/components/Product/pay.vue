<template>
	<div class="container-fluid">
    <div class="titlestyles d-flex py-4 my-4">
      <h1 class="titile-style"><img src="../../img/titleicon.png">訂單結果</h1>
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
      <div class="step">
        <span class="badge"><span class="text">3</span></span>
        <span>訂單明細</span>
      </div>
      <div class="step active">
        <span class="badge"><span class="text">4</span></span>
        <span>付款結果</span>
      </div>
    </div>
    <div class="information-card">
		<div class="row form-group">
            <div class="col-6 title-strong">訂單狀態</div>
            <div class="col-6 text-muted "><div class="paycheck">您已成功完成付款</div></div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">訂單編號</div>
			<div class="col-6 text-muted ">U211192808</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">預訂時間</div>
			<div class="col-6 text-muted ">2021-11-21</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">預訂商品</div>
			<div class="col-6 text-muted ">
				<div class="row">
					<div>夏日和服享受清涼(單衣)</div>
					<div>夏日和服享受清涼(單衣)</div>
					<div>夏日和服享受清涼(單衣)</div>
					<div>夏日和服享受清涼(單衣)</div>
					<div>夏日和服享受清涼(單衣)</div>
				</div>
			</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">付款金額</div>
			<div class="col-6 text-muted ">1000元</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">付款方式</div>
			<div class="col-6 text-muted ">LINE Pay</div>
		</div>
		<div class="row form-group">
			<div class="col-6 title-strong">Email通知</div>
			<div class="col-6 text-muted ">owensiisyl@gmail.com</div>  		
		</div>
	</div>
</div>
<div>
	<h1>貼心提醒</h1>
	<p>訂單成立後無法自己修改,有關訂單的疑問請聯絡我們</p>
</div>

</template>
<style scoped>
.paycheck{
	color: #f58958;
	font-weight: 600;
}
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