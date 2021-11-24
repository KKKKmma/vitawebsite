<template>

  <h2>Child</h2>
  <p>inject的count:{{ count }}</p>
  <p>inject的用户名：{{ userInfo.username }}</p>
  <p>inject的邮箱：{{ userInfo.email }}</p>
  
  // 调用inject的changeCount方法修改count
  <button @click="changeCount">count++</button> &nbsp;
  // 调用inject的changeUsername方法修改用户名
  <button @click="changeUsername">修改用户名</button>
  
</template>

<script>
import { inject } from "vue";
export default {
  setup(props, context) {
    // 注入count 并设置count的默认值为0
    const count = inject("count", 0);
    // 注入userInfo 并设置userInfo的默认值为0
    const userInfo = inject("userInfo", {});
    // 注入修改count的方法
    const changeCount = inject("changeCount");
    // 注入修改userInfo的方法
    const changeUsername = inject("changeUsername");
    return {
      count,
      userInfo,
      changeCount,
      changeUsername,
    };
  },
};
</script>