
# 🧩 Vue 3: Composables (自定义 Hooks) 核心速查

## 1. 🧠 核心心智模型 (Mental Model)

- **定义**：本质是一个**函数**。它将 `setup` 中使用的 Composition API（Ref, Reactive, Computed, Watch, Lifecycle）封装在一起。
    
- **作用**：**逻辑复用**。
    
    - 将 UI (Template) 与 逻辑 (Script) 分离。
        
    - 解决 Vue 2 `Mixin` 的命名冲突和来源不清问题。
        
- **命名规范**：通常以 `use` 开头，例如 `useUser`, `useScroll`。
    

---

## 2. ⚡ 标准代码模板 (Copy-Paste Ready)

### 2.1 定义 Hook (封装逻辑)

> 场景：我们把“加法计算”和“获取狗狗图片”的逻辑分别提取出来。

**📂 hooks/useSum.ts (同步逻辑示例)**

TypeScript

```
import { ref, onMounted } from 'vue'

export default function() {
  // 1. 定义数据 (State)
  let sum = ref(0)

  // 2. 定义操作数据的方法 (Action)
  const increment = () => { sum.value += 1 }
  const decrement = () => { sum.value -= 1 }

  // 3. 使用生命周期钩子
  onMounted(() => {
    increment()
  })

  // 4. 【关键】向外部暴露数据和方法
  return { sum, increment, decrement }
}
```

**📂 hooks/useDog.ts (异步逻辑示例)**

TypeScript

```
import { reactive, onMounted } from 'vue'
import axios, { type AxiosError } from 'axios'

export default function() {
  // 1. 定义数据
  let dogList = reactive<string[]>([])

  // 2. 定义异步方法
  async function getDog() {
    try {
      // 发请求
      let { data } = await axios.get('https://dog.ceo/api/breed/pembroke/images/random')
      // 维护数据
      dogList.push(data.message)
    } catch (error) {
      const err = <AxiosError>error
      console.log(err.message)
    }
  }

  // 3. 挂载时自动调用
  onMounted(() => {
    getDog()
  })
  
  // 4. 暴露给组件
  return { dogList, getDog }
}
```

### 2.2 组件中使用 (复用逻辑)

在组件中，这看起来非常像 React 的 Hooks 写法。

**📄 App.vue**

代码段

```
<script setup lang="ts">
  // 1. 引入 Hooks
  import useSum from './hooks/useSum'
  import useDog from './hooks/useDog'
  
  // 2. 执行函数并解构返回值 (就像解构 ref 一样自然)
  const { sum, increment, decrement } = useSum()
  const { dogList, getDog } = useDog()
</script>

<template>
  <div>
    <h2>当前求和: {{ sum }}</h2>
    <button @click="increment">+1</button>
    <button @click="decrement">-1</button>
    
    <hr>
    
    <img v-for="(url, index) in dogList" :key="index" :src="url" style="height: 100px; margin-right: 10px;">
    <button @click="getDog">再来一只狗</button>
  </div>
</template>
```

---

## 3. ⚖️ 核心对比：Hook vs Mixin (Interview)

这是面试中关于“为什么升级 Vue 3”的高频考点。

|**维度**|**Vue 3 Composables (Hook) 🏆**|**Vue 2 Mixins**|
|---|---|---|
|**数据来源**|**清晰**。`const { x } = useX()`，一眼便知 `x` 来自哪里。|**模糊**。`this.x` 是来自组件本身还是哪个 Mixin？很难找。|
|**命名冲突**|**无**。可以在解构时重命名：`const { x: x1 } = useX()`。|**有**。如果两个 Mixin 都有 `data.x`，会发生覆盖冲突。|
|**逻辑复用**|极其灵活，可以传递参数给 Hook。|较僵硬，参数传递依赖约定的属性。|

---

## 4. 🛑 最佳实践 (Best Practices)

1. **单一职责**：一个 Hook 最好只做一件事（例如 `useLocalStorage`, `useMousePosition`）。
    
2. **返回值**：建议始终返回一个**对象**，以便使用方进行解构。
    
3. **Ref 解包**：Hook 返回的数据通常是 `ref` 或 `reactive`，组件拿到后保持响应性，可以像普通响应式数据一样传递给子组件或在模板使用。
    
