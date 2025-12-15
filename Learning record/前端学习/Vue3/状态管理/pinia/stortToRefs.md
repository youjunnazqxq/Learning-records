
### 📝 Pinia 核心工具：storeToRefs

#### 1. 为什么需要它？(核心痛点)

当我们想从 store 中解构出数据（State 或 Getters）直接在模板中使用时，如果直接解构，数据会**失去响应式**。

- **❌ 错误写法 (丢失响应式)**：
    
    TypeScript
    
    ```
    const countStore = useCountStore()
    // 这样解构出来的 sum 只是一个普通的数值，store 变了它不会变
    const { sum } = countStore
    ```
    
- ✅ 正确写法 (保持响应式)：
    
    我们需要一种机制，把解构出来的数据自动包裹成 ref 对象，这就是 storeToRefs 的作用。
    

#### 2. 基本用法

借助 `storeToRefs` 将 store 中的数据转为 `ref` 对象。

- **引入**：
    
    TypeScript
    
    ```
    import { storeToRefs } from 'pinia'
    ```
    
- **使用**：
    
    TypeScript
    
    ```
    const countStore = useCountStore()
    
    // 使用 storeToRefs 包裹 store，然后再解构
    // 此时 sum 和 school 都是响应式的 ref 对象
    const { sum, school } = storeToRefs(countStore)
    ```
    

#### 3. ⚠️ 重要注意点 (避坑指南)

1. 只转换数据 (State & Getters)：
    
    storeToRefs 只会关注 store 中的状态（State）和计算属性（Getters）。
    
2. 不转换方法 (Actions)：
    
    不要用 storeToRefs 去解构 Actions（方法）。Actions 本身就是函数，不需要响应式，直接解构即可。
    
    TypeScript
    
    ```
    // ✅ Actions 直接解构
    const { increment } = countStore 
    
    // ❌ 不要这样写，不仅多余还可能报错
    // const { increment } = storeToRefs(countStore)
    ```
    
3. **与 Vue `toRefs` 的区别**：
    
    - Pinia 的 `storeToRefs`：专门为 Pinia 设计，只转换 State/Getters，忽略 Actions。
        
    - Vue 的 `toRefs`：会将对象中所有属性都转为 ref，可能会把 store 中的一些内部属性或方法也强行转换，不推荐直接对 store 使用。
        

---

💡 总结口诀：

"数据解构用 storeToRefs，方法解构直接拿。"