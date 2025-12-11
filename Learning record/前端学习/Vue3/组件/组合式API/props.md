

# 🧩 Vue 3: Props 组件通信 (TypeScript 版)

## 1. 🧠 核心心智模型 (Mental Model)

- **单向数据流**：数据只能从 **父 ➡️ 子** 流动。子组件严禁修改 Props 数据。
    
- **编译器宏 (Compiler Macro)**：`defineProps` 和 `withDefaults` 是 Vue 编译时的宏指令，**不需要手动 import** 即可在 `<script setup>` 中使用。
    
- **TS 优势**：结合 TS 泛型，可以实现构建时的类型检查和 IDE 智能提示。
    

---

## 2. 📋 前置准备：类型定义 (Best Practice)

在实际开发中，建议将类型定义提取到单独的 `.ts` 文件中，方便复用。

**📄 src/types/index.ts**

TypeScript

```
// 1. 定义单个对象接口
export interface PersonInter {
  id: string,
  name: string,
  age: number
}

// 2. 定义数组类型
export type Persons = Array<PersonInter>
```

---

## 3. ⚡ 父组件写法 (传递数据)

在父组件中引入类型，并使用泛型约束 `reactive` 数据。

**📄 Parent.vue**

代码段

```
<script lang="ts" setup>
import { reactive } from 'vue'
import Person from './components/Person.vue'
import { type Persons } from '@/types'

// 使用泛型 <Persons> 确保数据格式准确
let persons = reactive<Persons>([
  { id: 'e98219e12', name: '张三', age: 18 },
  { id: 'e98219e13', name: '李四', age: 19 },
  { id: 'e98219e14', name: '王五', age: 20 }
])
</script>

<template>
  <Person :list="persons"/>
</template>
```

---

## 4. 📥 子组件写法 (接收数据 - 三种进阶)

在 `<script setup>` 中，接收 Props 有从简单到严谨的三种写法。

### 🥉 写法 1：运行时声明 (JS 风格)

最简单，但失去了 TS 的类型检查优势。

TypeScript

```
// 仅接收，无类型提示
const props = defineProps(['list'])
```

### 🥈 写法 2：基于类型的声明 (TS 泛型)

Vue 3 推荐写法。利用 TS 泛型自动推断 Props 类型。

TypeScript

```
import { defineProps } from 'vue'
import { type Persons } from '@/types'

// 接收 + 限制类型
// 优点：父组件传错类型会报错
const props = defineProps<{
  list: Persons
}>()
```

### 🥇 写法 3：类型声明 + 默认值 (withDefaults)

**这是最完美的生产环境写法**。解决了 TS 泛型无法定义默认值的问题。

> **注意**：对象/数组类型的默认值必须通过**工厂函数**返回。

**📄 Child.vue (最终形态)**

代码段

```
<script lang="ts" setup>
import { withDefaults, defineProps } from 'vue'
import { type Persons } from '@/types'

// 接收 + 限制类型 + 指定默认值 + 限制必要性 (?)
const props = withDefaults(defineProps<{
  // 1. list?: 表示非必传
  // 2. Persons: 类型约束
  list?: Persons
}>(), {
  // 3. 第二个参数配置默认值
  // 数组/对象必须用函数返回
  list: () => [{ id: 'asdasg01', name: '小猪佩奇', age: 18 }]
})

// 在 JS 中使用 props
console.log(props.list)
</script>

<template>
  <div class="person">
    <ul>
      <li v-for="item in list" :key="item.id">
        {{ item.name }} -- {{ item.age }}
      </li>
    宏</ul>
  </div>
</template>
```

---

## 5. 🛑 避坑指南 (Troubleshooting)

|**场景**|**❌ 错误做法**|**✅ 正确做法**|**📝 原因**|
|---|---|---|---|
|**修改 Props**|`props.list = []`|`emit('update', [])`|违反单向数据流，会导致控制台警告。|
|**默认值引用**|`list: []`|`list: () => []`|对象/数组是引用类型，必须用工厂函数返回新对象，防止组件间状态污染。|
|**解构 Props**|`const { list } = props`|`const { list } = toRefs(props)`|直接解构会丢失 Props 的响应性 (Vue 3.5+ 的解构新特性除外)。|
|**Macro 引入**|`import { defineProps } ...`|**无需引入**|`defineProps` 是编译器宏，直接用即可 (虽然引入了也不报错，但多余)。|

---

**我可以为你做的下一步：**

Props 解决了父传子的问题，但子组件如何**修改父组件的数据**或**通知父组件**呢？

需要我为你整理 **“Vue 3 组件通信：Emits 与 v-model 核心机制”** 的笔记吗？我会重点讲解如何在 `<script setup>` 中使用 `defineEmits`。