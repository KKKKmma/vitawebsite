<template>
  <tr>
    <td>
      <router-link :to="item.product.get_absolute_url">{{
        item.product.name
      }}</router-link>
    </td>
    <td>
      ${{ item.product.price }}
      <a @click="decreamentQuantity(item)">-</a>
      <a @click="increamentQuantity(item)">+</a>
    </td>
    <td>
      {{ item.quantity }}
    </td>
    <td>${{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete" @click="removeFromCart(item)"></button></td>
  </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decreamentQuantity(item) {
      item.quantity -= 1;
      // 若購物車中的商品數量為0，則將商品刪除
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }

      this.updateCart();
    },
    increamentQuantity(item) {
      item.quantity += 1;

      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);

      this.updateCart();
    },
  },
};
</script>
