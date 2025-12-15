

### 📝 Vue3 学习笔记：Pinia 快速入门

#### 1. 环境搭建 (Setup)

**第一步：安装**

PowerShell

```
npm install pinia
```

**第二步：在 `main.ts` 中引入并使用**

TypeScript

```
import { createApp } from 'vue'
import App from './App.vue'
/* 1. 引入 createPinia */
import { createPinia } from 'pinia'

const pinia = createPinia() // 2. 创建 pinia 实例
const app = createApp(App)

app.use(pinia) // 3. 挂载 pinia
app.mount('#app')
```

---

#### 2. 定义 Store (核心概念)

Store 是一个保存状态和业务逻辑的实体。它有三个核心概念，对应组件的三大属性：

|**Pinia 概念**|**对应组件概念**|**作用**|
|---|---|---|
|**state**|`data`|存储数据 (状态)|
|**getters**|`computed`|计算属性 (对数据进行加工)|
|**actions**|`methods`|动作 (修改数据、业务逻辑)|

**代码示例 (`src/store/count.ts`)：**

TypeScript

```
import { defineStore } from 'pinia'

// defineStore('唯一ID', 配置对象)
export const useCountStore = defineStore('count', {
  // 1. 状态
  state() {
    return {
      sum: 6,
      school: 'atguigu'
    }
  },
  // 2. 动作 (支持同步和异步)
  actions: {
    increment(value: number) {
      this.sum += value // 使用 this 直接访问 state
    }
  },
  // 3. 计算
  getters: {
    bigSum: (state): number => state.sum * 10
  }
})
```

---

#### 3. 组件中使用与修改数据

在组件中引入并调用 `useXxxStore()` 即可得到 store 实例。

**A. 读取数据**

TypeScript

```
import { useCountStore } from '@/store/count'
const countStore = useCountStore()

// 直接读取
console.log(countStore.sum)
console.log(countStore.bigSum)
```

**B. 修改数据 (三种方式)**

1. **直接修改** (最简单)：
    
    TypeScript
    
    ```
    countStore.sum = 666
    ```
    
2. **批量修改** (`$patch`)：
    
    TypeScript
    
    ```
    countStore.$patch({
      sum: 999,
      school: 'hello'
    })
    ```
    
3. **通过 Actions 修改** (推荐，适合复杂逻辑)：
    
    TypeScript
    
    ```
    // 调用 store 中定义的 increment 方法
    countStore.increment(10)
    ```
    

---

#### 4. 优雅解构：storeToRefs (重点)

问题：如果直接解构 store (const { sum } = countStore)，数据会丢失响应式。

解决：使用 storeToRefs 进行包裹。

TypeScript

```
import { storeToRefs } from 'pinia'

const countStore = useCountStore()

// ❌ 错误做法：sum 丢失响应式
// const { sum } = countStore 

// ✅ 正确做法：sum 依然是响应式的 ref 对象
const { sum, school } = storeToRefs(countStore)
```

**注意**：`storeToRefs` 只负责处理 **State** 和 **Getters**，不要用它解构 Actions（Actions 直接从 store 解构即可）。

---

**💡 总结**

1. **安装挂载**：`createPinia()` -> `app.use(pinia)`。
    
2. **定义**：`defineStore` + `state/actions/getters`。
    
3. **使用**：`useXxxStore()`。
    
4. **解构**：State 用 `storeToRefs`，Actions 直接解构。