这是一个为你准备的 Markdown 格式笔记，你可以直接复制到你的 Obsidian 或其他笔记软件中。
它采用了 “原理 + 模板 + 避坑” 的结构，方便复习和直接复制代码。
# Vue 3: `<script setup>` 核心机制速查

## 1. 核心定位 (Mental Model)
* **本质**：组件逻辑的**初始化构造块** (Initialization Block)。
* **时机**：在 `beforeCreate` 之前执行，是整个组件生命周期的**起点**。
* **机制**：基于 **JavaScript 闭包 (Closure)** 和 **词法作用域**。
    * 顶层定义的变量/函数，都在同一个作用域内，互相可见。
    * **没有 `this`**：不要试图访问组件实例。
* **语法糖**：`<script setup>` 自动将顶层变量 **expose** (暴露) 给 `<template>` 使用，无需手动 `return`。

---

## 2. 标准代码模板 (Copy-Paste Ready)

### 2.1 基础状态与交互 (State & Methods)
> **核心规则**：JS 中修改 `ref` 需加 `.value`，模板中不需要。


```vue
<script setup>
import { ref, reactive } from 'vue'

// --- 1. 定义状态 ---
// 基本类型 (Number, String, Boolean) -> 用 ref
const count = ref(0)

// 对象类型 (Object, Array) -> 用 reactive (也可以用 ref)
const state = reactive({
  name: 'Alex',
  tags: ['CS', 'Vue']
})

// --- 2. 定义方法 ---
// 直接定义函数，它自动通过闭包访问上面的变量
const handleAction = () => {
  // 【注意】ref 在 script 中必须加 .value
  count.value++
  
  // reactive 不需要 .value
  state.tags.push('New')
  console.log('当前计数:', count.value)
}
</script>

<template>
  <div @click="handleAction">
    <p>计数: {{ count }}</p>
    <p>用户: {{ state.name }}</p>
  </div>
</template>

2.2 父子通信 (Props & Emits)
> 注意：defineProps 和 defineEmits 是编译器宏，无需 import。
> 
<script setup>
// --- 1. 接收父组件参数 ---
const props = defineProps({
  title: { type: String, default: '默认标题' },
  uid: Number
})

// --- 2. 声明触发事件 ---
const emit = defineEmits(['submit', 'close'])

const saveData = () => {
  // 在 script 中使用 props 需要通过变量访问
  console.log('Save ID:', props.uid)
  
  // 触发事件
  emit('submit', { id: props.uid, status: 'ok' })
}
</script>

2.3 生命周期 (Lifecycle)
> 映射关系：created -> setup() 本身；其他钩子加 on 前缀。
> 
<script setup>
import { onMounted, onUnmounted } from 'vue'

// 等同于 created / beforeCreate
console.log('1. 组件初始化')

// 等同于 mounted (DOM 渲染完毕)
onMounted(() => {
  console.log('2. DOM 已就绪，可以发请求或操作元素')
})

// 等同于 unmounted (组件销毁)
onUnmounted(() => {
  console.log('3. 清理定时器或监听器')
})
</script>

3. 常见痛点与避坑 (Troubleshooting)
| 场景 | 错误直觉 (Vue 2习惯) | 正确做法 (Vue 3 Setup) | 备注 |
|---|---|---|---|
| 访问变量 | this.count | count.value | Setup 里没有 this |
| 修改 ref | count = 1 | count.value = 1 | 只有在 <template> 里才不用加 .value |
| 解构 Props | const { title } = props | const { title } = toRefs(props) | 直接解构会丢失响应性 |
| 外部访问 | 父组件直接拿子组件数据 | 子组件需 defineExpose({ ... }) | <script setup> 默认是封闭的 |
4. 计算机视角理解 (Deep Dive)
为什么 setup 里的方法能直接访问变量？
这利用了 JS 的词法作用域链：
 * <script setup> 编译后相当于一个大的函数作用域。
 * count (变量) 和 handleAction (函数) 定义在同一层级。
 * handleAction 内部通过闭包 (Closure) 机制，向上查找并在内存中持有了 count 的引用。
<!-- end list -->

***

**我可以为你做的下一步：**
在笔记的 2.1 章节中，我们同时使用了 `ref` 和 `reactive`。在实际的大型项目中，对于**数组**和**深层嵌套对象**，应该优先选哪一个？需要我为你补充一段关于 **“Ref vs Reactive 选型指南”** 的内容吗？




