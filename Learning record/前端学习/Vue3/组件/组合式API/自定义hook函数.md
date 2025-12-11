Vue3 Hook 核心总结（作用+实例）
 
Vue3 的 Hook（自定义钩子） 是基于 Composition API 封装的可复用响应式逻辑函数（命名需以 use 开头），核心解决 Options API 中逻辑复用难、代码分散的问题。
 
一、Hook 核心作用
 
- 逻辑复用：抽取计数器、数据请求等重复响应式逻辑，多组件直接调用，避免重复编码。
- 逻辑聚合：将组件内分散的关联逻辑（如请求数据+加载状态+错误处理）聚合到单个 Hook，提升可读性。
- 替代 mixins：解决 mixins 命名冲突、逻辑来源模糊的问题，Hook 返回值明确，逻辑归属清晰。
 
二、实战实例（基于  <script setup>  语法）
 
实例 1：基础计数器 Hook -  useCounter 
 
1.1 编写 Hook（ src/hooks/useCounter.js ）
 
javascript
  
import { ref } from 'vue'

// 接收初始计数，返回响应式状态与操作方法
export function useCounter(initialValue = 0) {
  const count = ref(initialValue) // 响应式计数
  const increment = () => count.value++ // 递增
  const decrement = () => count.value > 0 && count.value-- // 递减（防负）
  const reset = () => count.value = initialValue // 重置

  return { count, increment, decrement, reset }
}
 
 
1.2 组件中使用
 
vue
  
<script setup>
import { useCounter } from '@/hooks/useCounter'
// 调用 Hook，传入初始值 10
const { count, increment, decrement, reset } = useCounter(10)
</script>

<template>
  <p>当前计数：{{ count }}</p>
  <button @click="increment">+1</button>
  <button @click="decrement">-1</button>
  <button @click="reset">重置</button>
</template>
 
 
实例 2：数据请求 Hook -  useFetch 
 
2.1 编写 Hook（ src/hooks/useFetch.js ）
 
javascript
  
import { ref, onMounted } from 'vue'

// 接收请求地址，返回数据、状态与请求方法
export function useFetch(url) {
  const data = ref(null)    // 响应数据
  const loading = ref(false)// 加载状态
  const error = ref(null)   // 错误信息

  // 核心请求逻辑
  const fetchData = async () => {
    loading.value = true
    try {
      const res = await fetch(url)
      if (!res.ok) throw new Error(`请求失败：${res.status}`)
      data.value = await res.json()
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  onMounted(() => fetchData()) // 组件挂载后自动请求

  return { data, loading, error, fetchData }
}
 
 
2.2 组件中使用
 
vue
  
<script setup>
import { useFetch } from '@/hooks/useFetch'
// 调用 Hook，重命名 data 为 userList（语义化）
const { data: userList, loading, error, fetchData } = useFetch('https://jsonplaceholder.typicode.com/users')
</script>

<template>
  <div v-if="loading">加载中...</div>
  <div v-else-if="error" style="color: red;">{{ error }}</div>
  <ul v-else>
    <li v-for="user in userList" :key="user.id">{{ user.name }}</li>
  </ul>
  <button @click="fetchData" style="margin-top: 12px;">刷新列表</button>
</template>
 
 
三、使用注意事项
 
- 命名规范：必须以 use 开头（如 useStorage 、 useWindowSize ），便于识别和 IDE 语法提示。
- 调用限制：仅能在  <script setup>  或其他自定义 Hook 中调用，不可在普通函数、模板内直接使用。
- 响应式依赖：Hook 内部需依赖 Vue 响应式 API（ ref / reactive ）和生命周期 API（ onMounted 等），确保逻辑响应式。