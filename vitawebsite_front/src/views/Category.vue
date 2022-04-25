<template>
  <div class="page-category">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import ProductList from "@/products/ProductList.vue";

export default {
  name: "Category",
  data() {
    return {
      category: {
        product: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;
      this.$store.commit("setIsLoading", true);
      axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then((response) => {
          this.category = response.data;
          document.title = this.category.name + " | Djackets";
        })
        .catch((error) => {
          console.log(error);
          toast({
            message: "Something went wrong. Please try again.",
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
