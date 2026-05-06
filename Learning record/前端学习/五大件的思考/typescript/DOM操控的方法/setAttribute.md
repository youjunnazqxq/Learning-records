**`setAttribute`** 是 JavaScript 提供的一个原生的 DOM（文档对象模型）方法。它的核心作用是**为指定的 HTML 元素设置或更新属性的值**。

### 基本机制

它的基础语法结构为：

`element.setAttribute(name, value);`

- **name**：想要设置的属性名称（例如 `"class"`, `"id"`, `"src"`, `"href"` 等）。
    
- **value**：赋予该属性的具体值。如果该属性已经存在，它的值会被新值覆盖；如果不存在，则会创建这个新属性。
    

### 结合当前代码的实际作用

在截图的 `switchDark` 函数中，`setAttribute` 扮演了切换页面样式的“物理开关”角色：

- **`html.setAttribute("class", "dark");`**
    
    当变量 `isDark.value` 为真（开启暗黑模式）时，这行代码会找到网页的根元素 `<html>`，强行给它加上 `class="dark"` 的属性。DOM 结构会变成类似 `<html class="dark">` 的状态。
    
- **`html.setAttribute("class", "");`**
    
    当关闭暗黑模式时，这行代码会将 `<html>` 标签上的 `class` 属性值清空。
    

### 这种用法的意义

这是现代前端框架（如 Tailwind CSS、Element Plus 等）实现动态主题最经典的底层策略。通过 `setAttribute` 在最顶层的 `<html>` 节点上挂载或卸载 `"dark"` 这个类名，底层的 CSS 样式表就能通过后代选择器（例如 `.dark .my-component { background: black; }`）瞬间捕捉到状态变化，从而实现全局的一键换肤。