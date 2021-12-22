<template>
  <div>
    <h1>App</h1>
    <p>App的count：{{ count }}</p>
    <p>App的用户名：{{ userInfo.username }}</p>
    // 子孙组件
    <Child />
  </div>
</template>

<script>
// 先引入provide
import { provide } from 'vue'

  setup() {

    // 建议把provide的状态转换为响应式（ref / reactive）
    const count = ref(100);

    const userInfo = reactive({
      username: "kyrie",
      email: "123@qq.com",
    });

    // 如果需要修改provide里面的状态 推荐在父组件注入修改状态的方法
    const changeCount = () => {
      count.value++;
    };

    const changeUsername = () => {
      userInfo.username = "wen";
    };

    // 为了避免inject组件修改provide的状态 使用readonly确保数据不被inject组件修改
    provide("count", readonly(count));
    provide("userInfo", readonly(userInfo));

    provide("changeCount", changeCount);
    provide("changeUsername", changeUsername);
  }
</script>