<template>
<h4>選擇日期</h4>
  <input v-model="dayetime">
  <div >{{dayetime}}</div>
<div class="themed-container">
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
    <li class="breadcrumb-item"><a href="/">Home</a></li>
    <li class="breadcrumb-item"><a href="/">商品頁面</a></li>
    <li class="breadcrumb-item active" aria-current="page">女士浴衣</li>
  </ol>
</nav>

<div class="">

<div class="row">
	<div class="col-md-3">
		<div class="block product">
			<div class="block-image">
				<router-link to="product-info">
				<img src="../../images/album_1.jpg" alt="" />
				</router-link>
				<span class="product-ribbon product-ribbon-right product-ribbon--style-1 bg-pink text-uppercase">New</span>
			</div>
			<div class="block-body text-center">
				<h2 class="heading heading-5 text-capitalize">
				<router-link to="product-info" >
				{{ producttitle }}
				</router-link>
				</h2>
				<div class="product-buttons mt-4">
					<div class="row align-items-center">
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink " data-toggle="tooltip" data-placement="top" title="" data-original-title="Compare">
							<i class="fa fa-share"></i>
							</button>
						</div>
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink  btn-circle btn-icon-left">
							<i class="fa fa-shopping-cart"></i>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="col-md-3">
		<div class="block product no-border z-depth-2-top z-depth-2--hover">
			<div class="block-image">
				<a href="#">
				<img src="../../images/album_2.jpg" alt="" />
				</a>
				<span class="product-ribbon product-ribbon-right product-ribbon--style-1 bg-pink  text-uppercase">New</span>
			</div>
			<div class="block-body text-center">
				<h2 class="heading heading-5 text-capitalize">
				<a href="#">{{ producttitle }}
				</a>
				</h2>
				<div class="product-buttons mt-4">
					<div class="row align-items-center">
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink " data-toggle="tooltip" data-placement="top" title="" data-original-title="Compare">
							<i class="fa fa-share"></i>
							</button>
						</div>
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink  btn-circle btn-icon-left">
							<i class="fa fa-shopping-cart"></i>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="col-md-3">
		<div class="block product no-border z-depth-2-top z-depth-2--hover">
			<div class="block-image">
				<a href="#">
				<img src="../../images/album_3.jpg" alt="" />
				</a>
				<span class="product-ribbon product-ribbon-right product-ribbon--style-1 bg-pink text-uppercase">New</span>
			</div>
			<div class="block-body text-center">
				<h2 class="heading heading-5 text-capitalize">
				<a href="#">
				{{ producttitle }}
				</a>
				</h2>
				<div class="product-buttons mt-4">
					<div class="row align-items-center">
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink " data-toggle="tooltip" data-placement="top" title="" data-original-title="Compare">
							<i class="fa fa-share"></i>
							</button>
						</div>
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink btn-circle btn-icon-left">
							<i class="fa fa-shopping-cart"></i>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="col-md-3">
		<div class="block product no-border z-depth-2-top z-depth-2--hover">
			<div class="block-image">
				<a href="#">
				<img src="../../images/album_1.jpg" alt="" />
				</a>
				<span class="product-ribbon product-ribbon-right product-ribbon--style-1 bg-pink text-uppercase">New</span>
			</div>
			<div class="block-body text-center">
				<h2 class="heading heading-5 text-capitalize">
				<a href="#">
				{{ producttitle }}
				</a>
				</h2>
				<div class="product-buttons mt-4">
					<div class="row align-items-center">
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink " data-toggle="tooltip" data-placement="top" title="" data-original-title="Compare">
							<i class="fa fa-share"></i>
							</button>
						</div>
						<div class="col-6">
							<button type="button" class="btn btn-block bg-pink  btn-circle btn-icon-left">
							<i class="fa fa-shopping-cart"></i>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
</div>
</div>
  </div>
</div>
 <!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  測試
</button>
     <div>
</div>
<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" >
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">選擇是否直接預定</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary closecart" data-bs-dismiss="modal">單純瀏覽</button>
        <button type="button" class="btn btn-primary">確認</button>
      </div>
    </div>
  </div>
</div>

</template>
<script>
  import productsidebar from '../../components/Product/productsidebar.vue';
  export default {
  name: 'product-catalogue',
  components: {
    productsidebar
  },
  data(){
    return{
      dayetime: "2021/11/24"
    }
  },
    setup() {
      const producttitle = '夏日和服享受清涼(單衣)';
      const handler = () => {
        alert(producttitle);

      };
      return { producttitle, handler };
    },

      props: ['modelValue'],
  emits: ['update:modelValue'],
  template: `
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    >
  `
  };
</script>
<style>
h5.modal-title{
	letter-spacing: 3px;
}
a.router-link-active.router-link-exact-active {
  color: #7c7c7c;

}
a.router-link-active.router-link-exact-active:after {
  background-image: url('../../img/linkicon.png');
  content: "1111";
  display: block;
  color: #ffffff00;
  background-position: 32px 180px;
  background-repeat: no-repeat;


}
</style>
