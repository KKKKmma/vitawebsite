<template>
<div class="container-fluid">
<div class="titlestyles d-flex py-4 my-4">
	<h1 class="titile-style"><img src="../../img/titleicon.png">および</h1>
</div>
<div class="row">
<div class="col-lg-3  pr-4 mr-4">
	<productsidebar />
</div>
<div class="col-lg-9">
	<nav aria-label="breadcrumb">
	<ol class="breadcrumb">
	<li class="breadcrumb-item"><a href="#">Home</a></li>
	<li class="breadcrumb-item"> 商品 </li>
	<li class="breadcrumb-item active" aria-current="page">女士浴衣</li>
	</ol>
	</nav>
	<div class="row">
		<div class="col">
		<div class="pro-img-details">
		<img src="../../images/album_1.jpg"  width="500" alt="" />
		</div>
		<div class="pro-img-list">
		<a href="#">
		<img src="https://via.placeholder.com/115x100/87CEFA/000000" alt="">
		</a>
		<a href="#">
		<img src="https://via.placeholder.com/115x100/FF7F50/000000" alt="">
		</a>
		<a href="#">
		<img src="https://via.placeholder.com/115x100/20B2AA/000000" alt="">
		</a>
		</div>
		</div>
		<div class="col">
		<span>產品編號：akn-123</span>
		<h3 class="producttitle">{{ producttitle }}</h3>
		<span class="contenttitle">商品描述</span>
		<div>
			{{ productcontent }}
		</div>
		<p>材質：聚酯纖維</p>
		<p>對應高度：158cm-173cm</p>
		<p class="badge badge-secondary mb-4">{{ producttag }}</p>
		<p class="badge badge-primary">女人浴衣</p>
		<table class="py-4 my-4">
		<tr>
		<td>サイズ</td>
		</tr>
		<tr>
		<td>身丈</td>
		<td>160cm</td>
		</tr>
		<tr>
		<td>裄丈 </td>
		<td>69cm</td>
		</tr>
		<tr>
		<td>袖丈</td>
		<td>49cm</td>
		</tr>
		<tr>
		<td>モデル身長</td>
		<td>153cm</td>
		</tr>
		</table>
		<div class="container-fluid text-center mb-4">
			<a href="/Bookinglist">
				<button type="button" class="btn btn-md check-btn">立即預定</button>
			</a>
		</div>
		<div class="container-fluid text-center mb-4">
			<a href="/Booking">
				<button  type="button" class="btn btn-md more-btn">加入購物車</button>
			</a></div>
		</div>
	</div>
</div>
</div>
</div>
</template>
<style scoped>
h3.producttitle {
    letter-spacing: 3px;
}
.badge {
    background-color: #E58E9B;
    margin: 10px;
}
.contenttitle{
	color: #4d4d4d;
	font-weight: 600;
}
</style>
<script>
  import productsidebar from '../../components/Product/productsidebar.vue';
  export default {
  name: 'productinfo',
  components: {
    productsidebar
  },
    setup() {
      const producttitle = '夏日和服享受清涼(單衣)';
      const productcontent = '我是產品內容';
      const producttag = '女人浴衣';
      const handler = () => {
        alert(producttitle);
      };
      return { producttitle, handler,productcontent,producttag };
    },
  };
</script>