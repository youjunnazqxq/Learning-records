
### 📝 Vue3 核心笔记：自定义事件 (emit)

#### 1. 核心作用

- **场景**：用于 **子组件 => 父组件** 的通信。
    
- **机制**：子组件触发（emit）一个事件，父组件监听（on）这个事件并接收数据。
    

#### 2. 原生事件 vs 自定义事件 (重要区别)

在 Vue3 中，理解 `$event` 的区别非常关键：

|**特性**|**原生事件 (如 @click)**|**自定义事件 (如 @abc)**|
|---|---|---|
|**事件名**|固定 (click, mouseenter 等)|任意名称|
|**`$event` 的值**|**事件对象** (包含 `target`, `pageX` 等)|**触发时传递的数据** (可以是任意类型)|

---

#### 3. 子组件写法 (发送方)

在 `<script setup>` 中，需要使用 `defineEmits` 宏来声明并获取 `emit` 函数。

代码段

```
<script setup lang="ts">
  // 1. 声明事件：告诉 Vue 我有哪些自定义事件
  const emit = defineEmits(['send-toy', 'update-data'])

  function sendData() {
    // 2. 触发事件：emit('事件名', 传递的数据)
    emit('send-toy', '我是奥特曼')
  }
</script>
```

#### 4. 父组件写法 (接收方)

在父组件的模板中，使用 `@事件名` 进行监听。

**方式一：直接在模板中使用 `$event`**

代码段

```
<template>
  <Child @send-toy="toy = $event"/>
</template>
```

**方式二：使用回调函数接收**

代码段

```
<template>
  <Child @send-toy="getToy"/>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  
  const toy = ref('')
  // 回调函数的参数就是子组件传过来的数据
  function getToy(value: string) {
    console.log('收到数据：', value)
    toy.value = value
  }
</script>
```

---

**💡 总结：**

- **Props** 是父给子传值。
    
- **Emit** 是子给父传值（或者通知父组件做事）。
    
- **关键点**：自定义事件里的 `$event` 就是你传的具体数据，不是 DOM 事件对象！