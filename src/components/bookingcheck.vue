<template>
<div class="container-fluid">
    <div class="titlestyles d-flex py-4 my-4">
      <h1 class="titile-style"><img src="../img/titleicon.png">預訂成功</h1>
    </div>
    <div class="information-card">
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
<div class="container-fluid text-center col"><router-link to="/"><button  type="button" class="btn btn-lg more-btn">回到首頁</button></router-link></div>
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