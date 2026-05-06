

### 1. 传入的参数是什么？

它标准语法接收三个参数，但在日常开发中绝大多数情况只用前两个：

JavaScript

```
element.style.setProperty(propertyName, value, priority);
```

- **参数一：`propertyName` (必填)**
    
    - **类型**：字符串。
        
    - **含义**：你要修改的 CSS 属性名。可以是常规属性（如 `'background-color'`），也可以是 CSS 自定义变量（如 `'--el-color-primary'`）。
        
- **参数二：`value` (可选/常用)**
    
    - **类型**：字符串。
        
    - **含义**：你要赋给这个属性的新值。比如 `'red'`、`'#409eff'` 或者 `'16px'`。
        
- **参数三：`priority` (可选)**
    
    - **类型**：字符串。
        
    - **含义**：CSS 优先级。如果你想强制覆盖其他样式，可以传入 `'important'`（不需要加 `!`）。
        

**在你项目中的实际体现：**

传入了属性名 `"--el-color-primary"` 和变量 `val`（比如 `"#ff0000"`）。

### 2. 这个方法的作用是什么？

它的核心作用是**直接修改该 DOM 元素的内联样式（Inline Style）**。

在主题切换的场景中，它的作用被放大了，产生了“一呼百应”的魔法效果：

1. **精准打击根节点**：`document.documentElement` 获取到的是网页的最高级元素：`<html>` 标签（在 CSS 中对应 `:root` 伪类）。
    
2. **全局变量覆盖**：当你用 `setProperty` 把根节点上的 `--el-color-primary` 替换成新颜色时，由于 CSS 变量具有**继承性**，网页中成百上千个使用 `var(--el-color-primary)` 的 Element Plus 组件（按钮、边框、文字等），会瞬间读取到这个新值。
    
3. **触发浏览器极速重绘**：这完全是原生浏览器的行为，不需要 Vue 参与数据的 Diff 计算，性能极高，实现了真正的“无刷新秒换肤”。
    

### 3. 为什么非要用它？不能直接“点”出来吗？

你可能会问：平时写 JS 修改样式，不都是直接 `element.style.color = "red"` 这样用点（`.`）语法吗？为什么要搞个这么长的方法？

这正是 `setProperty` 最不可替代的地方：

**原生 JS 的点语法不支持带横杠（`-`）的属性名，更不支持带有双横杠（`--`）的 CSS 变量！**

- **错误写法**：`document.documentElement.style.--el-color-primary = "#ff0000";` （JS 语法直接报错）
    
- **错误写法**：`document.documentElement.style['--el-color-primary'] = "#ff0000";` （虽然不报错，但在某些浏览器中无法正确应用到 CSS 变量系统里）
    
- **唯一标准写法**：`document.documentElement.style.setProperty("--el-color-primary", "#ff0000");`
    

简单来说，`setProperty` 就是前端用来操控 CSS 变量的“唯一正规且合法的遥控器”。