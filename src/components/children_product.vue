<template>
<div class="row">
	<div class="col-md-3">
		<div class="block product">
			<div class="block-image">
				<router-link to="product-info">
				<img src="../images/album_1.jpg" alt="" />
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
				<img src="../images/album_2.jpg" alt="" />
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
				<img src="../images/album_3.jpg" alt="" />
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
				<img src="../images/album_1.jpg" alt="" />
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
</template>
<script>
  export default {
  data(){
    return{
      dayetime: "2021/11/24"
    }
  },
    setup() {
      const producttitle = '夏日和服享受清涼(單衣)';
      return { producttitle};
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

</style>
