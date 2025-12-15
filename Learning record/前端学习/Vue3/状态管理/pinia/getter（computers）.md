
### 📝 Pinia Getters 核心总结

#### 1. 核心概念

- **作用**：当 `state` 中的数据需要经过**加工处理**后再使用时，可以使用 `getters`。
    
- **类比**：相当于组件中的 `computed` 属性。
    
- **特性**：具有缓存机制，只有依赖的数据发生变化时才会重新计算。
    

#### 2. 如何定义 (在 Store 中)

在 `defineStore` 的配置对象中添加 `getters` 选项。

- **写法技巧**：
    
    1. **接收 `state` 参数**（推荐箭头函数）：可以直接访问状态。
        
    2. **使用 `this`**（普通函数）：可以访问 store 里的其他 state 或 getters。
        

TypeScript

```
// src/store/count.ts
import { defineStore } from 'pinia'

export const useCountStore = defineStore('count', {
  state() {
    return {
      sum: 1,
      school: 'atguigu'
    }
  },
  // 👇 Getters 配置
  getters: {
    // 写法1：箭头函数，接收 state 参数 (最常用)
    bigSum: (state): number => state.sum * 10,

    // 写法2：普通函数，使用 this 访问 state
    upperSchool(): string {
      return this.school.toUpperCase()
    }
  }
})
```

#### 3. 如何使用 (在组件中)

使用方式与读取 `state` 完全一致。

- **方式一：直接读取**
    
    TypeScript
    
    ```
    const countStore = useCountStore()
    console.log(countStore.bigSum)
    ```
    
- 方式二：解构读取 (推荐)
    
    配合 storeToRefs 保持响应式。
    
    TypeScript
    
    ```
    import { storeToRefs } from 'pinia'
    
    const countStore = useCountStore()
    // 解构 getters，和解构 state 一样
    let { bigSum, upperSchool } = storeToRefs(countStore)
    ```
    

---

💡 总结：

"State 是数据源，Getters 是修饰器。想要数据自动加工，就用 Getters。"