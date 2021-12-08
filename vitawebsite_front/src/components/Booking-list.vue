<template>
	<div class="container-fluid">

  <div class="titlestyles d-flex justify-content-center py-4 my-4">
    <h1 class="titlestyle"><span class="titleicon">&emsp;</span>預約</h1>
  </div>
  <div class="container">
  <form action=" ">

  <div class="row">
    <div class="col">
      <label for="exampleFormControlInput1">姓名</label>
      <input type="text" class="form-control" placeholder="姓名">
    </div>
    <div class="col">
       <label for="exampleFormControlInput1">人數</label>
      <input type="text" class="form-control" placeholder="人數">
    </div>
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput1">電話</label>
    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="電話">
  </div>
  <div class="form-group">
    <label for="exampleFormControlInput1">mail</label>
    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="mail">
  </div>
    <div class="form-group">
    <label for="exampleFormControlTextarea1">備註</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  

</form> 

<p>服務條款</p>
<p>● 如需取消，請在前一天13:00前聯繫預訂店。請注意，在此之後取消預訂將收取 100% 的預訂費。</p>
<p>● 當天返回的顧客請在17:30前返回預約門店。</p>
<p>● 預約完成後，我們會向您發送預約完成郵件，請務必確認內容。</p>
<p>我同意條款和條件</p>

    <div class="container-fluid text-center"><button  type="button" class="btn btn-lg more-btn"><input type="submit" value="下一步選擇日期"></button></div>
</div>

  <div class="content">
    
    <div class="container text-left">
      
      <div class="row justify-content-center">
        <div class="col-md-10 text-center">
          <h2 class="mb-5 text-center">Calendar #7 (Inline + Result)</h2>
          <input type="text" class="form-control w-25 mx-auto mb-3" id="result" placeholder="Select date" disabled="">
          <form action="#" class="row">
            <div class="col-md-12">
              <div id="inline_cal"></div>
            </div>
          </form>
        </div>
      </div>
          
    </div>
  </div>
</div>
</template>