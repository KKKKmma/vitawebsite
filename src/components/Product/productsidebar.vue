<template>
<section class="panel"> <!--sidebar-->
    <div class="panel-heading mb-4 pb-4">
       全部商品
    </div>
    <div class="panel-body">
        <ul class="prod-cat">
            <li  class="title women_clothing">
                <router-link to="/productcatalogue/women_clothing"><i class="fa fa-angle-right"></i>{{ women_clothing }}</router-link>
            </li>
            <li  class="title men_clothing">
                <router-link to="/productcatalogue/men_clothing"><i class="fa fa-angle-right"></i>{{ men_clothing }}</router-link>
            </li>
            <li  class="title kid_clothing">
                <router-link to="/productcatalogue/kid_clothing"><i class="fa fa-angle-right"></i>{{ kid_clothing }}</router-link>
            </li>
            <li  class="title accessories_clothing"><span class="arrow"></span>
                <router-link to="/productcatalogue/accessories_clothing"><i class="fa fa-angle-right"></i>{{ accessories_clothing }}</router-link>
                <ul class="in-sidebar">
                    <li class="shoe"><a href="#">- {{ shoe }}</a></li>
                    <li class="bag"><a href="#">- {{ bag }}</a></li>
                    <li class="acc"><a href="#">- {{ acc }}</a></li>
                </ul>
            </li>
        </ul>
    </div>
</section>
</template>
<script>
      export default {
  name: 'productinfo',
    setup() {
      const women_clothing = '女士浴衣';
      const men_clothing = '男士浴衣';
      const kid_clothing = '兒童浴衣';
      const accessories_clothing = '配件';
      const shoe = '鞋子';
      const bag = '包包';
      const acc = '配飾';
      return { women_clothing, men_clothing,kid_clothing,accessories_clothing,shoe,bag,acc };
    },
  };
</script>
<style>
    li.title a:hover:after {
       background-image: url();
    }
    li.title a.router-link-active.router-link-exact-active:after{
       background-image: url();
       line-height: 0px;
    }
</style>

