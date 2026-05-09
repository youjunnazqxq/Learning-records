### 一、是什么 (BOM 概念解析)

**BOM (Browser Object Model)**，即浏览器对象模型。它提供了独立于网页内容，专门用于**与浏览器窗口进行交互**的对象。

如果说 DOM（文档对象模型）是为了操作 HTML 文档的内容而生，那么 BOM 则是为了控制浏览器的行为而生。BOM 缺乏像 DOM 那样严格的 W3C 官方标准（早期主要是各大浏览器厂商自行实现），但随着 HTML5 的普及，大部分 BOM 核心规范已经被纳入 HTML5 标准中，现代浏览器的兼容性已经非常好。

---

### 二、window (核心对象)

`window` 是 BOM 的**最核心对象**，它扮演着双重角色：

1. **浏览器窗口的接口**：它代表了浏览器的一个实例（一个标签页或一个 iframe）。
    
2. **全局对象 (Global Object)**：在全局作用域中声明的变量、函数，都会自动变成 `window` 对象的属性和方法（例如声明了 `var a = 1;`，就可以通过 `window.a` 访问）。
    

**常见操作与属性：**

- **关联其他 BOM 对象**：像 `document` (DOM 的入口)、`location`、`history` 等其实都是 `window` 的属性（通常省略 `window.` 前缀调用）。
    
- **弹窗方法**：`alert()`、`confirm()`、`prompt()`。
    
- **定时器**：`setTimeout()`、`clearTimeout()`、`setInterval()`、`clearInterval()`。
    
- **窗口控制**：`window.open()` (打开新窗口)、`window.close()` (关闭当前窗口)、`window.scrollTo()` (滚动窗口)。
    

---

### 三、location (URL 操作)

`location` 对象提供了与**当前窗口加载的 URL** 相关的信息，并且提供了一些导航功能。它既是 `window` 的属性，也是 `document` 的属性。

**核心属性 (用于解析 URL 各个部分)：**

- `location.href`：完整的 URL 字符串（最常用，修改它会导致页面跳转）。
    
- `location.protocol`：协议类型（如 `http:`、`https:`）。
    
- `location.host`：服务器名称和端口号。
    
- `location.pathname`：URL 中的目录和文件名。
    
- `location.search`：URL 中的查询字符串（通常是 `?` 后面的内容，常用于获取参数）。
    
- `location.hash`：URL 中的哈希值（`#` 后面的内容，常用于前端锚点或早期 SPA 路由）。
    

**核心方法：**

- `location.assign(url)`：跳转到新页面，**会**在历史记录中生成新条目（等同于修改 `href`）。
    
- `location.replace(url)`：跳转到新页面，但**不会**在历史记录中生成新条目（用户点击后退按钮无法回到前一个页面）。
    
- `location.reload()`：重新加载当前页面。
    

---

### 四、navigator (浏览器与系统信息)

`navigator` 对象主要用于获取**当前浏览器的状态和用户的操作系统环境信息**。

**常见属性：**

- `navigator.userAgent`：返回由客户机发送服务器的 User-Agent 头部的值（包含浏览器版本、操作系统等信息）。早期常用于判断浏览器类型来做兼容处理，但由于该字符串容易被伪造，现在更推荐使用“特性检测”。
    
- `navigator.platform`：返回运行浏览器的操作系统平台。
    
- `navigator.language`：返回浏览器的首选语言。
    
- `navigator.onLine`：返回布尔值，表示设备是否连网。
    
- `navigator.geolocation`：用于获取设备的地理位置信息（需要用户授权）。
    

---

### 五、screen (屏幕信息)

`screen` 对象包含有关**客户端显示屏幕**的信息。在现代响应式开发中直接使用的频率相对较低，偶尔用于数据统计或特定弹窗尺寸计算。

**常见属性：**

- `screen.width` / `screen.height`：屏幕的完整分辨率宽度和高度。
    
- `screen.availWidth` / `screen.availHeight`：屏幕的**可用**宽度和高度（通常等于完整尺寸减去系统任务栏占用的空间）。
    
- `screen.colorDepth`：屏幕的颜色深度（多少位）。
    

---

### 六、history (历史记录控制)

`history` 对象保存了用户在当前浏览器窗口或标签页中**访问过的 URL 历史记录**。出于隐私安全考虑，开发者无法通过该对象获取用户具体的历史浏览 URL 列表，只能进行前进、后退等操作。

**核心属性与方法（传统）：**

- `history.length`：历史记录栈中的条目数量。
    
- `history.back()`：后退一页（等同于点击浏览器的后退按钮）。
    
- `history.forward()`：前进一页。
    
- `history.go(n)`：跳转到历史记录中的特定页面。`n` 为正数表示前进，负数表示后退（如 `history.go(-1)` 等同于 `back()`）。
    

**HTML5 新增 API（现代前端路由的核心）：**

现代单页面应用（SPA，如你熟悉的项目中使用的 Vue 路由）主要依赖以下两个方法来实现“改变 URL 但不向服务器发送请求，且不刷新页面”：

- `history.pushState(state, title, url)`：在历史记录栈中添加一个新状态/记录。
    
- `history.replaceState(state, title, url)`：修改历史记录栈中当前的状态/记录，不新增。