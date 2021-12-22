<template>
  <div class="search">
    <input v-model="text" type="text" />
  </div>
</template>
<script>
import { computed } from "vue";

export default {
  name: "Search",
  props: {
    inputText: {
      type: String,
      default: "",
    },
  },
  emits: ["update:inputText"],
  setup(props, { emit }) {
    const text = computed({
      get: () => props.inputText,
      set: val => emit("update:inputText", val),
    });
    return {
      text,
    };
  },
};
</script>