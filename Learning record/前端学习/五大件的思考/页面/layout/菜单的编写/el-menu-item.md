

### 📒 Element Plus `<el-menu-item>` 核心使用笔记

#### 1. `index` 属性的“双重身份”

和 `<el-sub-menu>` 一样，`index` 是必传且唯一的。但在 `<el-menu-item>` 这里，它有着更关键的实战意义：

- **路由导航的“目的地”：** 如果你在最外层的 `<el-menu>` 标签上开启了 `router` 属性（例如 `<el-menu router>`），那么 Element Plus 就会把你传入的 `index` 视作跳转的 `path`。你点击这个菜单项，系统就会自动执行 `router.push(它的index值)`。
    
- **高亮匹配的“接头暗号”：** 外层 `<el-menu>` 的 `default-active` 属性决定了哪个菜单会高亮。只要当前页面的路由路径和这个 `<el-menu-item>` 的 `index` 完美匹配，它就会自动获得 `.is-active` 的高亮样式。
    

#### 2. 折叠菜单的“防穿帮”机制（具名插槽 `#title`）

如果你直接把文字写在 `<el-menu-item>` 里面，平时看着没问题，但在**侧边栏收起/折叠 (collapse)** 的时候，文字很可能会溢出或者排版错乱。

- **最佳实践：** 必须把图标写在外面，把文字严严实实地包裹在 `<template #title>` 插槽里。Element Plus 内部对这个插槽做了特殊处理，当菜单折叠时，它会自动把 `#title` 里的内容隐藏掉。
    
- **代码规范：**
    
    代码段
    
    ```
    <el-menu-item index="/home">
      <el-icon><House /></el-icon>
      <template #title>
        <span>首页主控台</span>
      </template>
    </el-menu-item>
    ```
    

#### 3. 内部路由与外部链接的“分水岭”

`<el-menu-item>` 默认的设计初衷是**系统内部的单页面跳转**。

如果你需要通过它点击跳转到一个外部网址（比如点击打开你们公司的官网主页），自带的路由模式就失效了。这时候你就必须像你之前提供的那段代码一样：

- **手动拦截：** 绑定 `@click="handleClick"` 事件。
    
- **逻辑判断：** 在点击事件里判断，如果是外链，就用 `window.open(url, "_blank")` 去新开页签；如果不是，再让 Vue Router 去执行 `push`。
    

---

现在侧边栏的核心子组件逻辑我们都已经理清了，接下来你是想先在系统里用假数据把这个菜单栏渲染出来跑跑看效果，还是想一鼓作气把顶栏（Header）的布局架构也给搭出来？