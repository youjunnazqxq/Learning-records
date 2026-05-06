

### 一、 基本语法

`watch` 接收三个参数：

1. **监听源 (Source)：** 你想要监听的数据。
    
2. **回调函数 (Callback)：** 数据变化时执行的逻辑，接收 `newValue` (新值) 和 `oldValue` (旧值) 两个参数。
    
3. **配置选项 (Options)：** 可选对象，用于配置深度监听、立即执行等。
    

JavaScript

```
import { watch } from 'vue'

watch(
  监听源, 
  (newValue, oldValue) => {
    // 数据变化时执行的代码
  }, 
  { 
    deep: false,      // 是否深度监听
    immediate: false, // 是否在初始化时立刻执行一次
    flush: 'pre'      // 调整回调的执行时机
  }
)
```

---

### 二、 核心用法分类

根据你监听的数据类型不同，`watch` 的写法会有细节上的差异：

**1. 监听单个 `ref` 基本数据**

直接传入 `ref` 变量名即可。

JavaScript

```
const count = ref(0)

watch(count, (newVal, oldVal) => {
  console.log(`数字从 ${oldVal} 变成了 ${newVal}`)
})
```

**2. 监听 `reactive` 对象**

直接传入 `reactive` 对象，Vue 会隐式地开启深度监听。

JavaScript

```
const user = reactive({ name: '张三', age: 20 })

watch(user, (newVal, oldVal) => {
  console.log('用户信息发生了改变')
})
```

**3. 监听 `reactive` 对象中的某一个属性（最常用）**

**重点：** 不能直接传 `user.name`，必须使用**一的个返回该属性的 getter 函数**（即箭头函数）。

JavaScript

```
const user = reactive({ name: '张三', age: 20 })

// 错误写法：watch(user.name, ...) ❌
// 正确写法：使用 () => user.name ✅
watch(() => user.name, (newVal, oldVal) => {
  console.log(`名字改变了：${newVal}`)
})
```

**4. 监听多个数据源**

可以将多个源放在一个数组中进行监听。

JavaScript

```
const x = ref(0)
const y = ref(0)

watch([x, y], ([newX, newY], [oldX, oldY]) => {
  console.log(`x 变成 ${newX}, y 变成 ${newY}`)
})
```

---

### 三、 高频注意点与避坑指南

#### 1. `immediate: true` (立即执行)

默认情况下，`watch` 是**惰性的**，只有在数据真正发生改变时才会执行回调。

如果你希望在组件刚渲染时就立刻跑一次回调（比如刚才讲的 Tabs 组件一加载就要把当前路由加进数组），必须配置 `immediate: true`。

JavaScript

```
watch(route, () => { /* ... */ }, { immediate: true })
```

#### 2. `deep: true` (深度监听的坑)

- 当你直接监听一个 `reactive` 对象时，深度监听是默认开启的。
    
- 但是，如果你监听的是一个包含深层对象的 getter 函数，或者包含对象的 `ref`，你需要手动开启 `deep: true` 才能监听到内部属性的改变。
    

JavaScript

```
const state = ref({ user: { name: '张三' } })

watch(
  () => state.value.user, 
  (newVal) => { console.log('用户信息改变') },
  { deep: true } // 必须手动开启
)
```

#### 3. 新旧值相同的坑 (对象引用机制)

当你深度监听一个对象或数组，并改变了它内部的某个属性时，回调函数里的 `newValue` 和 `oldValue` **会指向同一个内存地址**。你会发现它们打印出来是一模一样的。

- **解决办法：** 如果你严格需要对比修改前后的旧状态，必须监听这个对象的深拷贝版本，通常是通过传入 getter 函数实现：`watch(() => ({...obj}), (new, old) => {})`。
    

#### 4. `flush: 'post'` (DOM 更新后的时机)

默认情况下，`watch` 回调会在 Vue 更新 DOM **之前**被调用。如果你的回调里需要获取更新后的 DOM 元素（比如获取列表渲染后最新的高度），你需要配置 `flush: 'post'`。

JavaScript

```
watch(list, () => {
  // 此时能拿到更新后的 DOM
}, { flush: 'post' })
```

#### 5. 手动停止监听

写在 `<script setup>` 里的同步 `watch` 会在组件销毁时自动停止，通常不需要你操心。但如果某些特殊场景你需要手动掐断监听，可以接收 `watch` 的返回值并调用它：

JavaScript

```
const stopWatch = watch(count, () => { ... })
// 在需要的时候调用
stopWatch() 
```

这套基本功对于处理 Vue 项目中各种复杂的数据联动至关重要。你目前在 `Tab.vue` 中，除了监听 `$route` 之外，还有打算监听其他数据源吗？