
### 📝 路由 Props 配置笔记 (进阶篇)

#### 1. 什么时候用哪种写法？(场景指南)

|**写法**|**适用场景**|**核心特点**|
|---|---|---|
|**布尔值写法**|仅传递 `params` 参数|最简单。只需设为 `true`，路径里的 `/:id` 自动变 props。|
|**函数写法**|传递 `query` 参数 或 参数需处理|最灵活。可以接收 `route`，自行解析 `query`，或把参数类型转换后再传。|
|**对象写法**|传递静态死数据|较少用。通常用于通用组件在不同路由下表现不同标题等。|

---

#### 2. TypeScript 中的写法 (接收参数)

由于文档是基于 **Vue3 + TypeScript**，在组件接收路由 Props 时，推荐使用 TS 的泛型写法来声明类型。

- **场景**：路由传递了 `id` (string) 和 `title` (string)。
    
- **组件内写法 (`Detail.vue`)**：
    

TypeScript

```
<script setup lang="ts" name="Detail">
  // 1. 定义接口限制类型 (规范)
  interface Props {
    id: string
    title: string
    content?: string // 可选参数
  }

  // 2. 接收 props (使用泛型写法，无需引入 PropType)
  const props = defineProps<Props>()

  // 3. 直接使用
  console.log(props.id) 
</script>
```

(参考 3.12 章节的 TS defineProps 写法)

---

#### 3. 完整代码对比 (Before vs After)

通过对比，一眼看清配置 `props` 的好处：**组件更纯粹，不再依赖路由。**

🔴 优化前 (组件依赖 useRoute)

组件必须引入 vue-router，无法作为独立组件复用。

TypeScript

```
// Detail.vue
import { useRoute } from 'vue-router'
const route = useRoute()

// 必须带着 .query 或 .params 到处跑
console.log(route.params.id) 
```

🟢 优化后 (组件仅依赖 props)

组件不知道自己被路由管理，数据来源解耦，方便测试和复用。

**Step 1: 路由配置 (`router/index.ts`)**

TypeScript

```
{
  path: 'detail',
  component: Detail,
  // 使用函数写法将 query 转为 props
  props(route){
    return route.query
  }
}
```

**Step 2: 组件接收 (`Detail.vue`)**

TypeScript

```
// 不需要引入 vue-router
defineProps(['id', 'title'])
```

---

**💡 总结**

- 能用 `props` 就用 `props`，让组件和路由**解耦**。
    
- 传 `params` 用 **布尔模式** (`props: true`)。
    
- 传 `query` 用 **函数模式** (`props: route => route.query`)。