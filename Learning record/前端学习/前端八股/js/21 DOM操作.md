在 JavaScript 中，DOM（文档对象模型）操作是前端开发的核心基础。常见的 DOM 操作可以主要分为以下几个大类：

### 1. 获取（查询）元素

这是进行任何 DOM 操作的第一步，你需要先找到目标元素。

- **`document.getElementById('id')`**: 通过元素的 ID 获取单个元素。最常用且性能最好。
    
- **`document.querySelector('selector')`**: 使用 CSS 选择器（如 `.class`, `#id`, `div > p`）获取匹配的**第一个**元素。非常灵活。
    
- **`document.querySelectorAll('selector')`**: 使用 CSS 选择器获取所有匹配的元素，返回一个 NodeList（类似数组）。
    
- **`document.getElementsByClassName('class')`**: 通过类名获取所有元素集合（HTMLCollection）。
    
- **`document.getElementsByTagName('tag')`**: 通过标签名（如 `div`, `span`）获取所有元素集合。
    

### 2. 修改元素内容

获取元素后，经常需要更改其显示的文本或内部 HTML 结构。

- **`element.innerHTML`**: 获取或设置元素内部的 HTML 结构。会解析 HTML 标签。
    
- **`element.textContent`**: 获取或设置元素及其所有子节点的纯文本内容。不会解析 HTML 标签，性能比 `innerHTML` 更好且更安全（防 XSS）。
    
- **`element.innerText`**: 类似 `textContent`，但受 CSS 样式影响（例如，不会获取被 `display: none` 隐藏的文本）。
    

### 3. 操作节点属性与属性节点

用于修改元素的特征，如 `src`、`href` 或自定义属性。

- **`element.setAttribute('name', 'value')`**: 设置或更新属性值。
    
- **`element.getAttribute('name')`**: 获取指定的属性值。
    
- **`element.removeAttribute('name')`**: 移除指定的属性。
    
- **`element.hasAttribute('name')`**: 检查元素是否包含某属性，返回布尔值。
    

### 4. 操作样式和类名 (CSS)

动态改变元素的视觉表现。

- **操作 Class (推荐):**
    
    - `element.classList.add('className')`: 添加类名。
        
    - `element.classList.remove('className')`: 移除类名。
        
    - `element.classList.toggle('className')`: 切换类名（有则移除，无则添加）。
        
    - `element.classList.contains('className')`: 判断是否包含某类名。
        
- **直接操作 Style:**
    
    - `element.style.propertyName = 'value'`: 直接修改内联样式（例如：`element.style.backgroundColor = 'red'`）。注意带连字符的 CSS 属性在 JS 中要写成小驼峰命名（如 `fontSize`）。
        

### 5. 创建、添加与插入节点

用于动态构建页面结构。

- **`document.createElement('tagName')`**: 创建一个新的 HTML 元素节点（如 `div`）。
    
- **`parentNode.appendChild(newChild)`**: 将新节点添加到父节点的子节点列表末尾。
    
- **`parentNode.insertBefore(newNode, referenceNode)`**: 在父节点中的某个参考节点之前插入新节点。
    
- **`document.createTextNode('text')`**: 创建一个纯文本节点。
    

### 6. 删除与替换节点

清理或更新不再需要的元素。

- **`element.remove()`**: 直接从 DOM 中移除元素自身（现代浏览器支持）。
    
- **`parentNode.removeChild(childNode)`**: 通过父节点来移除特定的子节点（兼容性更好的传统写法）。
    
- **`parentNode.replaceChild(newChild, oldChild)`**: 将父节点中的某个旧子节点替换为新节点。
    

### 7. 节点遍历（关系查找）

根据当前元素的位置，查找其周围的相关元素。

- **父节点**: `element.parentNode` 或 `element.parentElement`。
    
- **子节点**:
    
    - `element.children`: 获取所有子元素节点（只包含标签，不含文本节点，最常用）。
        
    - `element.childNodes`: 获取所有子节点（包含元素、文本节点、注释等）。
        
    - `element.firstElementChild` / `element.lastElementChild`: 获取第一个/最后一个子元素。
        
- **兄弟节点**:
    
    - `element.nextElementSibling`: 获取紧邻的下一个兄弟元素。
        
    - `element.previousElementSibling`: 获取紧邻的上一个兄弟元素。




**第一，在“查”（获取与遍历节点）方面：**

现代前端开发中，我最常用的是 `querySelector` 和 `querySelectorAll`，因为它们完全支持 CSS 选择器语法，使用起来非常灵活。如果是对性能要求极高的单体查询，我会使用 `getElementById`。在处理节点间的关系时，我会使用 `parentNode` 查找父节点，使用 `children` 来获取纯元素子节点集合。

**第二，在“改”（修改节点内容、属性和样式）方面：**

- **处理内容时**，我会优先使用 `textContent` 而不是 `innerHTML`。因为 `textContent` 不仅性能更好，而且不会解析 HTML 标签，能有效防范 XSS 跨站脚本攻击。
    
- **处理样式时**，为了保持样式与逻辑的分离，我通常不会直接操作 `element.style`，而是通过 `classList.add()` 或 `toggle()` 等方法去动态切换元素的类名。
    
- **处理属性时**，主要使用 `setAttribute` 和 `getAttribute` 进行标准或自定义属性的操作。
    

**第三，在“增”和“删”（节点的创建、插入与移除）方面：**

- **增加节点**：主要通过 `createElement` 在内存中创建新元素，然后利用 `appendChild` 追加到父节点末尾，或者用 `insertBefore` 精确插入到某个参考节点之前。
    
- **删除节点**：在现代浏览器中我习惯直接调用目标元素的 `remove()` 方法，如果考虑到旧版浏览器的兼容性，则会通过 `parentNode.removeChild()` 来实现。
    

**最后，我想补充一点关于 DOM 操作的性能考量（加分项）：**

频繁的 DOM 操作会触发浏览器的重排（Reflow）和重绘（Repaint），非常消耗性能。因此，如果遇到需要一次性动态生成并插入大量 DOM 节点的场景，我一定会先创建一个 `DocumentFragment`（文档碎片），把所有新节点组装到碎片中，最后再一次性挂载到 DOM 树上，这样可以把重排次数降到最低。

当然，虽然扎实的原生 DOM 基础很重要，但在我们实际开发企业级项目（例如复杂的后台管理系统）时，通常会采用数据驱动视图的理念。我们会交由底层的虚拟 DOM 和响应式系统来计算并最小化真实的 DOM 操作开销。”

---

**面试小贴士：**

- 回答时语速保持平稳，把加粗的关键词（**XSS防御、重排重绘、DocumentFragment、数据驱动**）重音突出，这些都是面试官喜欢听到的“踩分点”。
    
- 最后一段巧妙地从原生基础过渡到了现代框架的思维，非常适合正在寻找前端实习或初级/中级前端开发的候选人。