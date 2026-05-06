
在传统的简单应用中，所有的路由（比如首页、关于页、登录页）都在初始化 `createRouter` 的 `routes` 数组里写死了。但是在你截图里的后台管理系统中，用户的权限不同，能看到的页面也不同，这时候就需要用到 `router.addRoute` 在程序运行过程中根据后端返回的数据，把属于该用户的页面“动态注入”到路由表中。

### `router.addRoute` 的语法

这个方法有两种常用的传参语法：

**1. 添加一条顶级路由**

直接传入一个路由对象，它将作为最外层的一级路由存在。

JavaScript

```
router.addRoute({
  path: '/about',
  name: 'About',
  component: () => import('@/views/About.vue')
})
```

**2. 添加一条子路由（嵌套路由）**

传入两个参数：第一个参数是**父级路由的 `name`（字符串）**，第二个参数是要添加的子路由对象。

JavaScript

```
// 假设之前已经存在一个 name 为 'Layout' 的顶级路由
router.addRoute('Layout', {
  path: 'user-manage',
  name: 'UserManage',
  component: () => import('@/views/UserManage.vue')
})
```

**结合你之前的截图看：**

在你截图的第 38-42 行，正是巧妙地运用了这两种语法：

- 如果 `item.meta.isFull` 为 true（比如大屏展示页），就直接 `router.addRoute(item)` 作为独立顶级页面。
    
- 否则，执行 `router.addRoute("layout", item)`，将其塞进整体的布局组件（Layout，包含侧边栏和顶栏）中作为子路由展示。
    

---

### 使用时的三大核心注意点（非常容易踩坑）

**1. 路由 `name` 冲突会发生覆盖**

如果你动态添加了一个路由，而它的 `name` 和路由表中已存在的某个路由完全一样，那么**旧的路由会被自动删除**，替换为你新加的这个。因此，在后台返回的动态路由数据中，保证每个页面的 `name` 唯一非常重要。

**2. 添加后不会立刻触发跳转（最常见的坑）**

假设用户访问 `/admin`，触发了动态获取路由的逻辑，你用 `addRoute` 把 `/admin` 注册进去了。**但这并不会让页面马上渲染出来！** 因为在拦截器进入的一瞬间，Vue Router 原本的路径匹配过程已经走完了（当时并没有找到 `/admin`）。因此，通常在全局守卫（`beforeEach`）里添加完路由后，必须手动重定向一次：

JavaScript

```
// 强制让路由重新匹配一次刚才添加的新路由
return { ...to, replace: true } 
```

**3. 如何删除已添加的路由？**

`router.addRoute()` 方法执行后，会**返回一个回调函数**。如果你调用这个回调函数，刚才添加的这条路由就会被从路由表中删掉。另外，你也可以直接使用 `router.removeRoute('路由名称')` 来删除指定的动态路由。

你在看动态路由这部分代码时，你想了解在实际开发中，动态添加路由后刷新页面经常出现的“白屏”或 404 问题，以及究竟如何在 `router.beforeEach` 守卫中用 `return { ...to, replace: true }` 彻底解决它吗？