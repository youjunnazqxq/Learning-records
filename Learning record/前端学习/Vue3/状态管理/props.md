
### 📝 Vue3 组件通信：Props

#### 1. 核心规则

- **通信方向**：主要用于 **父 ↔ 子**。
    
- **传递原则**：
    
    - **父传子**：属性值是**非函数**（普通数据）。
        
    - **子传父**：属性值是**函数**（父组件把函数传给子组件，子组件调用该函数并将数据作为参数传回）。
        

#### 2. 父组件写法 (传递方)

在子组件标签上通过属性绑定的方式传递数据。

代码段

```
<template>
  <div class="father">
    <Child :car="car" :getToy="getToy"/>
  </div>
</template>

<script setup lang="ts">
  import { ref } from "vue";
  // 数据
  const car = ref('奔驰')
  // 定义一个接收数据的函数
  function getToy(value:string){
    console.log('收到子组件的玩具：', value)
  }
</script>
```

#### 3. 子组件写法 (接收方)

使用 `defineProps` 宏来接收父组件传递的数据。

方式一：简单接收 (数组写法)

适用于不需要限制类型的简单场景。

TypeScript

```
const props = defineProps(['car', 'getToy'])
// JS中直接使用 props.car
```

方式二：限制类型 (TS 泛型写法)

适用于 TypeScript 环境，可以进行类型检查。

TypeScript

```
// 仅接收 + 限制类型
defineProps<{car: string, getToy: Function}>()
```

方式三：限制类型 + 默认值 (withDefaults) ✨ (推荐)

适用于需要指定默认值的情况。

TypeScript

```
// 引入 withDefaults
import { withDefaults } from 'vue'
import { type Persons } from '@/types'

// 接收 + 限制类型 + 指定默认值
withDefaults(defineProps<{list?: Persons}>(), {
  // 默认值函数
  list: () => [{id: '001', name: '默认用户', age: 18}]
})
```

---

**💡 总结：**

- **父给子传东西**：直接写属性 `:a="数据"`。
    
- **子给父传东西**：父给子一个函数 `:fn="函数"`，子调用 `props.fn(数据)`。
    
- **TS 最佳实践**：用 `withDefaults` + `defineProps<{...}>()`。