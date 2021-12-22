<template>
<div class="container-fluid">
  <div class="row icon-style">
    <div class="col d-flex justify-content-end move-img"><img src="../img/icon-r.svg" width="160px"></div>
  </div>
  <div class="row about-content">
    <div class="col-lg-7 about-left-bg">
      <div>
      <h3>微光文創</h3>
      </div>
      <div>
      <p>擁有幾百件浴衣，提供活動、手作教學、等租借使用。</p>
      <p>服務項目：和服體驗、販賣、着付教學、藝文活動、色彩教學等多項服務。</p>
      </div>
    </div>
    <div class="col-lg-5 about-right">
      <div class="about-right-pink"></div>
      <div class="about-right-img d-flex justify-content-end"><img class="d-flex justify-content-end" src="../img/image-2.png"></div>
    </div>
  </div>
  <div class="container">
  <p class="d-flex justify-content-center pt-4 text-style">穿上浴衣漫步。 <br>
  為了要夠讓更多的顧客能夠體會到和服之美，所以開始提供和服出租的服務。<br>
  我們精心挑選了許多適合古都京都美景的復古和服等待各位的光臨。<br></p>
  </div>
</div>
</template>
<script>

</script>
<style scoped>
a {
  color: #42b983;
}
.text-style{
  letter-spacing: 10px;
  line-height: 35px;
}
.about-content{
  padding-top: 00px;
}
.about-content > div{
  padding: 144px 0px 0px 60px;
}
.about-content h3{
  padding: 40px;
}
.about-left-bg{
  background-color: #F6D2C6;
  background-size: 609px 1087px;
}
.about-right{
  display: flex;
  justify-content: flex-end;
  right: 16%;
  top: 0;
  z-index: 1;
  position: relative;
}
.about-right-pink{
  background-color: #AF6363;
  width: 127px;
  height: 127px;
  max-width: 100%;
  float: left;
  z-index: 1;
  position: absolute;
  left: 0;
  bottom: 0;
}
about-right-img{
  z-index: 1;
}
.about-right-img img{
  max-width: 100%;
}

.icon-style{
  display: flex;
  flex-wrap: wrap-reverse;
}
.icon-style img{
  position:relative;
  top: 150px;
}

.booking-list h4{
  font-weight: 800px;
  letter-spacing: 4px;
  font-size: 48px;
  margin-bottom: 26px;
}
h4 i {
  padding-right: 24px;
}
.booking-list-left{
  padding-left: 60px;
}
.booking-bg{
  background-color: #F5F2EE;
  padding:40px 0 40px 0;
}
.booking-btn{
  background-color: #BB726B;
  color: #fff;
  border-radius: 4px;
  border:1px solid #BB726B;
  letter-spacing: 15px;
  text-align: center;
  padding:20px;
  margin-top: 30px;
}

.Attractions-title h4{
  background-color: #C5AF7F;
  color: #fff;
  padding: 20px;
  display: inline;
}
.Attractions-list{
  background-color: #F5F2EE;
  padding :40px;
  height: 45vh;
  width: 45vw;
  text-align: center;
}

.news-right{
  background-color: #F4F2EE;
}
</style>
