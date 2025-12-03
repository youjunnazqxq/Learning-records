

### 场景一：针对 Params 参数（路径里带 `/123`）

这是最常用的方式，只需要开启一个布尔值开关。

#### 1. 路由配置 (`router/index.js`)

JavaScript

```
{
  path: '/detail/:id/:title', // 路径里占了位
  component: Detail,
  // 【重点】设置为 true
  // 效果：Vue 会自动把路径里的 id 和 title 拿出来，作为 props 传给组件
  props: true 
}
```

#### 2. 组件接收 (`Detail.vue`)

HTML

```
<template>
  <div>
    <h3>商品ID: {{ id }}</h3>
    <h3>标题: {{ title }}</h3>
  </div>
</template>

<script>
export default {
  // 【重点】像接收父组件数据一样声明 props
  props: ['id', 'title']
}
</script>
```

---

### 场景二：针对 Query 参数（路径里带 `?id=123`）

因为 `props: true` 默认只支持 params，如果你用的是 query (`?`后面带参数)，就需要写成**函数形式**。

#### 1. 路由配置 (`router/index.js`)

JavaScript

```
{
  path: '/detail', // 注意：这里没有 :id 占位，因为是 query 参数
  component: Detail,
  
  // 【重点】写成函数，接收 route 对象
  // 返回什么对象，组件就能收到什么 props
  props($route) {
    return {
      id: $route.query.id,
      title: $route.query.title
    }
  }
  
  // 简写方式 (ES6):
  // props: ({ query }) => ({ id: query.id, title: query.title })
}
```

#### 2. 组件接收 (`Detail.vue`)

**你看，组件的代码完全不用改！和上面一模一样！**

HTML

```
<template>
  <div>
    <h3>商品ID: {{ id }}</h3>
    <h3>标题: {{ title }}</h3>
  </div>
</template>

<script>
export default {
  props: ['id', 'title']
}
</script>
```

---

### 核心总结

1. **`props: true`**： 适用于 **Params** 参数（最简单）。
    
2. **`props: 函数`**： 适用于 **Query** 参数（自定义能力强）。
    

使用这两种方法，你的组件（`Detail.vue`）就变得非常纯粹，它不需要知道“路由”的存在，只管收数据就行。

---

你可以让我：

现在路由的基本增删改查你都掌握了。需要我为你介绍一下 Vue Router 的“编程式导航” (push vs replace) 吗？ (这是控制浏览器“后退”按钮能不能用的关键)。