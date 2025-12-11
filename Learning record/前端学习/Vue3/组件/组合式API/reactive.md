

# ⚡ Vue 3: Reactive 核心机制与用法速查

## 1. 🧠 核心心智模型 (Mental Model)

作为 CS 学生，请从 **Proxy 设计模式** 的角度理解 `reactive`：

- **定义**：它是 ES6 **`Proxy`** 的直接封装。
    
- **内存模型**：
    
    - `const state = reactive(target)`
        
    - 变量 `state` 指向的是 **Proxy 实例的内存地址**，而不是原始对象 `target` 的地址。
        
    - **拦截器 (Interceptor)**：所有对 `state` 的操作（读、写、删除、遍历）都会先经过 Proxy 的 Handler。
        
- **深层响应 (Deep Reactivity)**：Proxy 默认是深层的。当你访问 `state.nested.count` 时，Vue 会在访问的那一刻（Lazy）将嵌套对象也包装成 Proxy。
    

---

## 2. 📋 标准代码模板 (Copy-Paste Ready)

### 2.1 基础定义与交互

> **🔥 核心优势**：语法最接近原生 JS 对象，**不需要 `.value`**。

代码段

```
<script setup>
import { reactive } from 'vue'

// 1. 定义复杂对象 (仅限 Object, Array, Map, Set)
const user = reactive({
  name: 'Alex',
  stats: {             // 嵌套对象自动被 Proxy 包裹
    hp: 100,
    mp: 50
  }
})

// 2. 修改数据
const takeDamage = () => {
  // ✅ 直接修改属性，Proxy 的 Setter 会拦截并触发更新
  user.stats.hp -= 10
  console.log('当前血量:', user.stats.hp)
}
</script>

<template>
  <div @click="takeDamage">
    玩家: {{ user.name }} (HP: {{ user.stats.hp }})
  </div>
</template>
```

---

## 3. 💣 核心痛点与避坑 (Critical Pitfalls)

`reactive` 的局限性主要源于 **JavaScript 的引用机制**。

| **❌ 错误场景** | **📝 代码示例**                                                              | **🧠 CS 原理解析**                                             | **🔧 修正方案**                                               |
| ---------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- | --------------------------------------------------------- |
| **基础类型**   | `reactive(0)`                                                            | **Proxy 只能代理对象**。基础类型通过值传递，无法挂载 Handler。                   | 改用 `ref(0)`                                               |
| **直接解构**   | `let { hp } = user.stats`                                                | **值拷贝 (Value Copy)**。解构出的 `hp` 只是一个纯数字，切断了与 Proxy 的联系。     | 使用 `toRefs` (见下文)                                         |
| **整体替换**   | `let state = reactive({...})`<br><br>  <br><br>`state = reactive({...})` | **指针丢失**。你把变量 `state` 指向了一个全新的内存地址，但 Vue 组件还监听着旧地址的 Proxy。 | `Object.assign(state, newObj)`<br><br>  <br><br>或改用 `ref` |

---

## 4. ⚖️ Ref vs Reactive 选型指南 (Decision Matrix)

在实际架构中，如何选择？

|**维度**|**Ref 🏆 (官方更推荐)**|**Reactive**|
|---|---|---|
|**适用类型**|全能 (Primitives + Objects)|仅限对象 (Objects / Arrays)|
|**访问语法**|JS 中需 `.value` (显式解包)|直接访问 (隐式自动)|
|**数据替换**|✅ `data.value = [...]` (安全)|❌ 不可直接 `data = [...]`|
|**解构能力**|❌ (解构 `.value` 也会丢)|❌ (解构属性会丢)|
|**心智负担**|低 (只需记住 `.value`)|高 (需时刻警惕引用丢失)|

---

## 5. 🔬 原理深挖 (Deep Dive)

**Reactive 的伪代码实现 (基于 ES6 Proxy):**

JavaScript

```
// 简化的 reactive 实现
function reactive(target) {
  // 1. 限制：如果不是对象，直接返回
  if (typeof target !== 'object' || target === null) {
    return target
  }

  // 2. 核心：返回 Proxy 实例
  return new Proxy(target, {
    // 拦截读取操作
    get(target, key, receiver) {
      // 📥 依赖收集 (Track)
      track(target, key)
      
      // ✨ 惰性递归：如果属性是对象，才继续 wrap 成 reactive
      const res = Reflect.get(target, key, receiver)
      if (isObject(res)) {
        return reactive(res)
      }
      return res
    },
    
    // 拦截写入操作
    set(target, key, value, receiver) {
      const oldValue = target[key]
      const result = Reflect.set(target, key, value, receiver)
      
      // 📤 触发更新 (Trigger)
      // 只有值真正变化了才触发
      if (value !== oldValue) {
        trigger(target, key)
      }
      return result
    }
  })
}
```
