在 Vue Router 4 中，`history` 属性是整个路由系统的“引擎”，它决定了你的应用将以何种方式管理 URL 的变化以及浏览器的历史记录栈。

你在截图中看到的 `history: routerMode[mode]()`，实际上是在根据环境变量动态选择路由的运行模式。Vue Router 主要提供了三种历史记录模式，最常用的是前两种：

### 1. Hash 模式 (`createWebHashHistory`)

这是单页应用（SPA）最传统的路由模式。

- **URL 外观**：带有井号 `#`，例如 `http://localhost:3000/#/dashboard` 或 `http://localhost:3000/#/user/profile`。
    
- **工作原理**：它利用了 URL 中的 hash（即 `#` 及其后面的内容）。**hash 的改变不会触发浏览器向服务器发送全新的请求**，但会触发浏览器的 `hashchange` 事件。Vue Router 就是通过监听这个事件来获知 URL 的变化，并据此进行组件的切换和渲染。
    
- **优点**：**部署极其简单，不需要后端或服务器做任何额外配置。** 无论你怎么刷新页面，浏览器只会把 `#` 之前的基础 URL 发送给服务器，服务器只要始终返回 `index.html` 即可。
    
- **缺点**：URL 带有 `#`，看起来不够美观；在某些特定的第三方 App 内嵌授权（如微信公众号开发、部分支付回调）时，带有 `#` 的 URL 可能会被截断或引发识别问题。
    

### 2. HTML5 模式 (`createWebHistory`)

也常被称为 History 模式，是目前中大型前端项目（如后台管理系统）的主流选择。

- **URL 外观**：干净、标准的 URL，例如 `http://localhost:3000/dashboard`。
    
- **工作原理**：它依赖 HTML5 提供的 History API（主要是 `history.pushState` 和 `history.replaceState`）。这两个 API 可以在不重新加载页面的情况下，直接修改浏览器的 URL 地址栏，并将状态推入历史记录栈。
    
- **优点**：URL 非常干净美观，和传统的网站路径一样，对 SEO（搜索引擎优化）更加友好。
    
- **致命痛点（需要服务器配合）**：**如果不配置服务器，刷新页面会报 404 错误。**
    
    - _为什么会这样？_ 因为当你处于 `http://localhost:3000/dashboard` 时按下刷新键，浏览器会真的向服务器发送一个对 `/dashboard` 路径的 GET 请求。如果你的后端（比如 Nginx 或 Tomcat）没有针对这个路径配置对应的资源，它自然会返回 404 Not Found。
        
    - _怎么解决？_ 需要在服务器（通常是 Nginx）上配置“回退路由”。即：如果匹配不到任何静态资源，就把请求全部重定向回你的 `index.html`。一旦前端拿到了 `index.html`，Vue Router 就会接管接下来的路由解析，展示正确的 `/dashboard` 组件。
        

### 3. Memory 模式 (`createMemoryHistory`)

- **工作原理**：它不会与浏览器的 URL 产生任何交互，所有的路由状态都保存在内存中。
    
- **使用场景**：通常不会在普通的浏览器环境下使用。它主要用于 **Node.js 环境下的服务器端渲染 (SSR)**，或者在进行前端单元测试时使用。
    

---

### 回到你的截图代码

在很多优秀的开源后台管理系统模板中（这类项目通常对工程化要求较高），开发者通常不会把 `history` 写死。截图中 `routerMode[mode]()` 的底层逻辑通常是这样的：

TypeScript

```
// 类似这样的一个映射表
const routerMode = {
  hash: () => createWebHashHistory(),
  history: () => createWebHistory(),
  memory: () => createMemoryHistory()
};

// mode 变量通常来自于 Vite 或 Webpack 的环境变量 (如 import.meta.env.VITE_ROUTER_MODE)
```

这样做的好处是，你可以直接在 `.env` 环境配置文件中修改一个变量，就能一键切换整个项目的路由模式，而不需要深入到路由配置代码中去修改。比如，开发阶段或者部署到静态服务器（如 GitHub Pages）时用 `hash`，正式部署到配置好 Nginx 的生产环境时用 `history`。

你想了解如果使用 HTML5 模式，Nginx 服务器端的伪静态（重定向）配置具体应该怎么写吗？