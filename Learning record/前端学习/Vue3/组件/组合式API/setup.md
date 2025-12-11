


# ⚡ Vue 3 `<script setup>` 核心速查

## 1. 🧠 核心心智模型 (Mental Model)

- **本质**：组件的**初始化构造块** (Initialization Block)。
    
- **运行时机**：`beforeCreate` 之前执行，是生命周期的起点。
    
- **底层机制**：**JS 闭包 (Closure)**。顶层变量/函数在同一作用域，互相可见。
    
- **主要变化**：
    
    - 🚫 **无 `this`**：切勿尝试访问组件实例。
        
    - ✅ **自动 Expose**：顶层定义的变量可以直接在 `<template>` 中使用，无需 `return`。
        

---

## 2. 📋 标准代码模板 (Copy-Paste Ready)

### 2.1 基础状态与交互

> **⚠️ 核心铁律**：在 `<script>` 中修改 `ref` 必须加 `.value`，但在模板中不需要。

代码段

```
<script setup>
import { ref, reactive } from 'vue'

// --- 1. 定义状态 ---
const count = ref(0)             // 基本类型 (Number, String) -> 用 ref
const state = reactive({         // 对象类型 -> 用 reactive
  name: 'Alex',
  tags: ['CS', 'Vue']
})

// --- 2. 定义方法 ---
const handleAction = () => {
  // script 中修改 ref 需加 .value
  count.value++  
  
  // reactive 不需要 .value
  state.tags.push('New') 
}
</script>

<template>
  <div @click="handleAction">
    <p>计数: {{ count }}</p>
    <p>用户: {{ state.name }}</p>
  </div>
</template>
```

### 2.2 父子通信 (Props & Emits)

> **提示**：`defineProps` 和 `defineEmits` 是**编译器宏**，无需 import 即可直接使用。

代码段

```
<script setup>
// --- 1. 接收父组件参数 ---
const props = defineProps({
  title: { type: String, default: '默认标题' },
  uid: Number
})

// --- 2. 声明触发事件 ---
const emit = defineEmits(['submit', 'close'])

const saveData = () => {
  // 必须通过 props 变量访问属性
  console.log('ID:', props.uid)
  
  // 触发事件
  emit('submit', { id: props.uid, status: 'ok' })
}
</script>
```

### 2.3 生命周期映射 (Lifecycle)

代码段

```
<script setup>
import { onMounted, onUnmounted } from 'vue'

// 1. created / beforeCreate -> 直接写在 setup 顶层
console.log('组件初始化...')

// 2. mounted -> DOM 渲染完毕
onMounted(() => {
  console.log('DOM 就绪，可发起请求')
})

// 3. unmounted -> 组件销毁
onUnmounted(() => {
  console.log('清理定时器/监听器')
})
</script>
```

---

## 3. 🛑 避坑指南 (Troubleshooting)

| **场景**       | **❌ 错误直觉 (Vue 2 / 常犯错误)** | **✅ 正确做法 (Vue 3 Setup)**          | **📝 备注**                   |
| ------------ | ------------------------- | --------------------------------- | --------------------------- |
| **访问变量**     | `this.count`              | `count.value`                     | Setup 内部没有 `this`           |
| **修改 ref**   | `count = 1`               | `count.value = 1`                 | 仅在 template 中自动解包           |
| **解构 Props** | `const { title } = props` | `const { title } = toRefs(props)` | **直接解构会丢失响应性**              |
| **父调子方法**    | 父组件直接访问子组件实例              | 子组件需 `defineExpose({ ... })`      | `<script setup>` 默认是**封闭**的 |

---

## 4. 🔬 原理深挖 (Deep Dive)

为什么 setup 里的方法能直接访问变量？

这并非 Vue 的魔法，而是 JavaScript 词法作用域 的原生能力：

1. `<script setup>` 编译后变成一个巨大的 `setup()` 函数。
    
2. `count` (变量) 和 `handleAction` (函数) 定义在同一层级。
    
3. `handleAction` 通过 **闭包 (Closure)** 持有对 `count` 的引用，因此可以直接读取和修改。
    

---

**我可以为你做的下一步：**

针对 **3. 避坑指南** 中提到的 **“Props 解构丢失响应性”** 这个问题，Vue 3.5+ 推出了 Reactivity Transform (响应性语法糖) 的正式替代方案——**Props Destructuring (Props 解构)** 功能。

需要我为你补充一段 **“Vue 3.5+ 如何安全地解构 Props 且保持响应性”** 的最新写法吗？