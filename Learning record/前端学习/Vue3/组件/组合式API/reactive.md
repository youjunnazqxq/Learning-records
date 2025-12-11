这份笔记专为你整理，重点结合 Proxy 原理 和 内存引用 的概念，方便你放入 Obsidian 知识库。
# Vue 3: Reactive 核心机制与用法总结

## 1. Reactive 的本质 (The Essence)

作为 CS 学生，你可以这样理解 `reactive`：

* **定义**：它是 **Proxy 的直接封装**。
* **作用**：用于定义 **对象类型**（Object, Array, Map, Set）的响应式状态。
* **机制**：
    * 它创建一个 **代理对象 (Proxy Instance)** 包裹住原始对象。
    * 你拿到的变量是一个指向 **Proxy** 的引用（指针），而不是原始数据的引用。
    * **Deep Reactivity (深层响应)**：无论对象嵌套多少层，访问深层属性时，Vue 都会确保它是响应式的。

---

## 2. 基本用法 (Basic Usage)

### 2.1 定义与读写
与 `ref` 不同，`reactive` **不需要** `.value`。因为 Proxy 会自动拦截属性的读取 (Getter) 和修改 (Setter)。

```vue
<script setup>
import { reactive } from 'vue'

// 1. 定义复杂对象
const user = reactive({
  name: 'Alex',
  level: 108,
  equipment: { // 嵌套对象自动响应式
    weapon: 'Sword',
    armor: 'Shield'
  }
})

// 2. 修改数据
const levelUp = () => {
  // ✅ 直接修改属性，Proxy 会拦截并触发更新
  user.level++ 
  user.equipment.weapon = 'Excalibur'
}
</script>

<template>
  <div>等级: {{ user.level }}</div>
</template>

3. 核心限制与避坑 (Critical Pitfalls)
这是 reactive 最容易出 Bug 的地方，请务必注意 引用丢失 的问题。
❌ 限制 1：不支持基本类型
Proxy 的目标必须是对象。
const count = reactive(0) // ⚠️ 错误：value cannot be made reactive

❌ 限制 2：解构丢失响应性 (Destructuring)
这是最高频的陷阱。
JavaScript 中基本类型的赋值是 值拷贝 (Pass by Value)。当你把属性解构出来时，它就切断了与 Proxy 的联系。
const state = reactive({ count: 0 })

// ❌ 错误：count 变成了普通的数字 0
let { count } = state 

count++ // state.count 不会变，视图也不会更新

> 解决办法：使用 toRefs (后续笔记会讲)。
> 
❌ 限制 3：直接替换对象导致连接断开
Vue 的响应式系统依赖于由于 setup 初始化时创建的那个特定的 Proxy 引用。如果你把变量指向一个新的对象，Vue 就“跟丢”了。
let state = reactive({ count: 0 })

// ❌ 错误：这就相当于 state 指向了一个新的内存地址
// 之前的 DOM 绑定还在监听旧的那个 Proxy
state = reactive({ count: 1 }) 

> 解决办法：
>  * 修改属性：Object.assign(state, { count: 1 })
>  * 或者改用 ref 定义对象：state.value = { count: 1 }
> 
4. Ref vs Reactive 选型指南 (Decision Matrix)
在实际开发中，如果不确定用哪个，请参考此表：
| 维度 | ref | reactive |
|---|---|---|
| 数据类型 | 全能 (基本类型 + 对象) | 仅限对象 (Object/Array) |
| 访问方式 | JS 中需 .value | 直接访问属性 |
| 重新赋值 | ✅ 可以直接 state.value = {} | ❌ 不可直接替换变量引用 |
| 解构支持 | ❌ (解构 .value 也会丢失) | ❌ (解构属性会丢失) |
| 官方推荐 | 首选 (更灵活，不易出错) | 用于层级很深且明确不需替换的对象 |
5. 计算机底层视角总结
// reactive 的伪代码逻辑
function reactive(target) {
  // 如果不是对象，直接返回（限制1）
  if (typeof target !== 'object') return target;

  // 返回一个新的 Proxy 实例
  return new Proxy(target, {
    get(target, key, receiver) {
      track(); // 收集依赖
      return Reflect.get(target, key, receiver);
    },
    set(target, key, value, receiver) {
      trigger(); // 触发视图更新
      return Reflect.set(target, key, value, receiver);
    }
  });
}


