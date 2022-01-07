<template>
<div class="container-fluid">
  <div class="titlestyles d-flex justify-content-center py-4 my-4">
    <h1 class="titlestyle"><span class="titleicon">&emsp;</span>預約 {{ searchText }}</h1>
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
        <span>訂單明細</span>
      </div>
      <div class="step">
        <span class="badge"><span class="text">4</span></span>
        <span>付款結果</span>
      </div>
  </div>
  <div class="container form-bg">
  <form name="my form" action="/" method="GET">
    <div class="row">
      <div class="col">
        <label for="exampleFormControlInput1">姓名</label>
        <input type="text" id="user_id" placeholder="姓名">
      </div>
      <div class="col">
         <label for="exampleFormControlInput1">人數</label>
        <input type="text" id="user_number" placeholder="人數">
      </div>
    </div>
    <div class="form-group">
      <label for="exampleFormControlInput1">電話</label>
      <input type="email" class="form-control" id="user_number" placeholder="電話">
    </div>
    <div class="form-group">
      <label for="exampleFormControlInput1">mail</label>
      <input type="email" class="form-control" id="user_mail" placeholder="mail">
    </div>
      <div class="form-group">
      <label for="exampleFormControlTextarea1">備註</label>
      <textarea class="form-control" id="user_note" rows="3"></textarea>
    </div>
  </form>
  </div>
  <div class="mb-4">
    <p>服務條款</p>
    <p>● 如需取消，請在前一天13:00前聯繫預訂店。請注意，在此之後取消預訂將收取 100% 的預訂費。</p>
    <p>● 當天返回的顧客請在17:30前返回預約門店。</p>
    <p>● 預約完成後，我們會向您發送預約完成郵件，請務必確認內容。</p>
    <p>我同意條款和條件</p>
  </div>
  <div class="container-fluid text-center col">
    <router-link to="/bookingcheck"><button  type="button" class="btn btn-lg more-btn">下一步訂單確認</button></router-link>
  </div>
</div>
</template>
<script>

</script>
<style scoped>
.form-bg{
  border:1px solid #ccc;
  border-radius: 4px;
  padding: 40px;
}
  
</style>