

# 📦 Vue 3: Ref 核心机制与底层原理速查

## 1. 🔬 底层原理 (Deep Dive)

为什么需要 Ref？

JS 的基础类型 (number, string, boolean) 是按值传递的，Proxy 无法代理它们。Vue 必须创建一个**“中间人对象”**来拦截读写。

### 1.1 内存结构：RefImpl

当你执行 `const count = ref(0)` 时，Vue 创建了一个 `RefImpl` (Reference Implementation) 类的实例。它利用 ES6 的 **Getter/Setter** 闭包特性实现响应式。

**核心伪代码 (CS 视角):**

JavaScript

```
class RefImpl {
  constructor(val) {
    this.__v_isRef = true // 1. 身份标记
    this._value = val     // 2. 内部私有变量 (实际存储)
    this.dep = new Set()  // 3. 依赖集合 (谁在用我?)
  }

  get value() {
    track() // 📥 依赖收集：记录当前的副作用函数
    return this._value
  }

  set value(newVal) {
    if (hasChanged(newVal, this._value)) {
      this._value = newVal
      trigger() // 📤 触发更新：通知视图重绘
    }
  }
}
```

### 1.2 心智模型

- **指针 (Pointer)**：`ref` 就像 C 语言的指针。变量持有的是**引用地址**，你需要解引用 (`.value`) 才能拿到真实数据。
    
- **装箱 (Boxing)**：就像 Java 的 `Integer` 包装了 `int`。
    

---

## 2. ⚡ 标准代码模板 (Copy-Paste Ready)

### 2.1 基础读写 (语法铁律)

> **🔥 核心口诀**：**“JS 中解包，HTML 中直连”**。

|**环境**|**语法**|**原理**|
|---|---|---|
|**Script (JS)**|`count.value`|访问对象的 getter/setter，必须手动解引用。|
|**Template (HTML)**|`{{ count }}`|编译器会在渲染函数中自动帮你解包 (Unwrap)。|

代码段

```
<script setup>
import { ref } from 'vue'

// 1. 定义：创建一个 RefImpl 实例
const count = ref(0) 

const update = () => {
  // ❌ 错误：count++ (count 是个对象，不能自增)
  // ✅ 正确：操作 .value
  count.value++ 
  console.log('JS中读取需加 .value:', count.value)
}
</script>

<template>
  <button @click="update">
    当前数值: {{ count }}
  </button>
</template>
```

### 2.2 DOM 引用 (Template Refs)

Vue 3 中不再使用 `this.$refs`，而是将 DOM 元素直接赋值给 ref 变量。

代码段

```
<script setup>
import { ref, onMounted } from 'vue'

// 1. 定义空容器 (必须与模板中的 ref 同名)
const inputRef = ref(null)

onMounted(() => {
  // 3. 挂载后，Vue 会自动把原生 DOM 塞进 .value
  inputRef.value?.focus()
})
</script>

<template>
  <input ref="inputRef" />
</template>
```

---

## 3. 🛑 避坑指南 (Troubleshooting)

### 3.1 为什么不能解构 Ref？

JavaScript

```
const count = ref(10)

// ❌ 错误做法
const { value } = count 
// 后果：变量 'value' 变成了纯数字 10。
// 它切断了与 RefImpl 实例 getter/setter 的联系，失去了响应性。
```

### 3.2 什么时候用 Ref？

- ✅ **基础数据类型**：`String`, `Number`, `Boolean`。
    
- ✅ **全量替换场景**：例如 `userList.value = newData` (后端接口返回)。
    
- ✅ **DOM 元素**：必用 ref。
    
