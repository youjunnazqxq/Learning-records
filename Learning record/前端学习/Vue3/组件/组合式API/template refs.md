

# 🔗 Vue 3: Template Refs (模板引用) 速查

## 1. 🧠 核心心智模型 (Mental Model)

- **作用**：Vue 的“逃生舱”。用于直接访问 **原生 DOM 元素** 或 **子组件实例**。
    
- **替代**：完全替代了原生的 `document.getElementById` 和 Vue 2 的 `this.$refs`。
    
- **机制**：
    
    - 在 HTML 中：使用 `ref="xxx"` 属性标记。
        
    - 在 Script 中：创建一个**同名的** `ref` 变量来接收它。
        
    - **挂载后生效**：只有在 DOM 渲染完毕 (`onMounted`) 后，变量的 `.value` 才会有值，初始通常为 `null`。
        

---

## 2. ⚡ 标准代码模板 (Copy-Paste Ready)

### 2.1 场景一：获取原生 DOM 元素

> **用途**：输入框聚焦、Canvas 绘图、获取元素宽高、集成第三方 DOM 库 (如 ECharts)。

代码段

```
<script setup lang="ts">
import { ref, onMounted } from 'vue'

// 1. 定义一个空 ref，名称必须与模板中 ref 属性一致
// TS建议：泛型指定类型，初始值设为 null
const inputRef = ref<HTMLInputElement | null>(null)

function handleFocus() {
  // 3. 访问 DOM (注意判空，因为挂载前是 null)
  inputRef.value?.focus()
  console.log('Input Value:', inputRef.value?.value)
}

onMounted(() => {
  console.log('DOM 已挂载:', inputRef.value)
})
</script>

<template>
  <div class="person">
    <input type="text" ref="inputRef" />
    <button @click="handleFocus">聚焦输入框</button>
  </div>
</template>
```

### 2.2 场景二：获取子组件实例 (父调子)

> **⚠️ 核心变化**：`<script setup>` 默认是**私有**的。父组件无法直接访问子组件的数据/方法，除非子组件通过 `defineExpose` 显式暴露。

**子组件 (Child.vue):**

代码段

```
<script setup lang="ts">
import { ref, defineExpose } from 'vue'

const count = ref(0)
const sayHello = () => console.log('Hello from Child')

// 🚫 默认情况下，父组件拿不到上面的 count 和 sayHello
// ✅ 必须显式暴露
defineExpose({
  count,
  sayHello
})
</script>

<template>
  <div>我是子组件</div>
</template>
```

**父组件 (Parent.vue):**

代码段

```
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import Child from './Child.vue'

// 1. 定义 ref 接收子组件实例
const childRef = ref(null)

const testChild = () => {
  // 2. 读取子组件暴露的数据或调用方法
  console.log(childRef.value?.count) // 0
  childRef.value?.sayHello()         // "Hello from Child"
}
</script>

<template>
  <Child ref="childRef" />
  <button @click="testChild">操作子组件</button>
</template>
```

---

## 3. 🛡️ 核心机制：`defineExpose`

为什么子组件必须写 `defineExpose`？

- **Vue 2 / Options API**：组件实例默认是“透明”的，父组件通过 `$refs` 可以随意访问子组件的所有 data 和 methods。这导致耦合度极高，且难以维护。
    
- **Vue 3 `<script setup>`**：默认是 **“封闭” (Closed by Default)** 的。为了保护组件内部逻辑，父组件只能访问子组件**愿意**公开的部分。
    

---

## 4. 🛑 避坑指南 (Troubleshooting)

| **场景**    | **❌ 常见错误**                                   | **✅ 正确做法**                               | **📝 原因**                                |
| --------- | -------------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| **访问时机**  | 在 `setup()` 顶层直接打印 `el.value`                | 在 `onMounted` 或点击事件中访问                   | `setup` 执行时 DOM 还没生成，此时 `ref` 还是 `null`。 |
| **组件数据**  | 父组件拿不到子组件数据，打印为 `undefined`                  | 子组件加 `defineExpose({...})`               | `<script setup>` 默认私有机制。                 |
| **变量命名**  | 模板写 `ref="box"`，JS 写 `const div = ref(null)` | 变量名必须叫 `box` (即 `const box = ref(null)`) | Vue 依赖**变量名匹配**来自动注入引用。                  |
| **v-for** | 在 `v-for` 中使用 `ref="items"`                  | 此时 `items.value` 会自动变成一个**数组**           | 循环绑定时，Ref 会自动收集该列表的所有元素。                 |

---

## 5. 🟦 TypeScript 技巧 (For TS Users)

如果你在使用 TS，为了获得良好的代码提示，建议显式标注类型：

TypeScript

```
// 1. 对于 DOM 元素
const btnRef = ref<HTMLButtonElement | null>(null)

// 2. 对于组件实例 (使用 InstanceType)
import Child from './Child.vue'
const childRef = ref<InstanceType<typeof Child> | null>(null)
```
