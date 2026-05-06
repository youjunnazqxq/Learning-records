`SortableJS` 的核心接口非常简洁，主要是通过调用 **`Sortable.create()`** 方法来实现拖拽功能。

它的基本语法如下：

JavaScript

```
Sortable.create(el, options);
```

你需要传入两个核心参数：**容器元素 (`el`)** 和 **配置对象 (`options`)**。

---

### 第一个参数：`el` (拖拽容器 DOM 元素)

这是必须要传入的参数。你需要告诉 SortableJS，到底**哪一个父盒子**里面的子元素是可以互相拖拽换位的。

- **传入要求**：必须是一个真实的 DOM 节点（通常通过 `document.querySelector` 或者 Vue 的 `ref` 获取）。
    
- **示例**：在 Element Plus 的 Tabs 中，这个容器通常是包裹所有标签的 `.el-tabs__nav`。
    
    JavaScript
    
    ```
    const wrapper = document.querySelector(".el-tabs__nav");
    ```
    

---

### 第二个参数：`options` (配置对象)

这是一个包含各种开关和回调函数的对象，用来高度定制你的拖拽行为。对于后台标签页（Tabs）来说，最常用的配置项有以下几个：

#### 1. 基础视觉交互

- **`animation` (Number)**：动画时间（单位：毫秒）。设置后，拖拽时其他元素会自动平滑移动让出位置，不会生硬地闪烁。通常设置为 `150` 到 `300`。
    
- **`ghostClass` (String)**：占位符类名。当你拖起一个标签时，原来位置会留下一个“影子”（占位符）。你可以指定一个 CSS 类名，用来给这个影子设置背景色或透明度。
    

#### 2. 行为控制（精细化定制）

- **`filter` (String)**：不可拖拽的元素。传入一个 CSS 选择器（比如类名）。这在后台 Tabs 中非常有用，比如你给“首页”标签加了一个 `.is-affix` 类名，然后设置 `filter: ".is-affix"`，首页就永远钉在最前面，不允许被拖走。
    
- **`handle` (String)**：拖拽把手。如果你不想让整个标签都可以拖拽，只希望用户按住标签上的某个小图标（比如 ≡）才能拖，就可以传入那个图标的类名。
    

#### 3. 核心回调函数：`onEnd`

这是你在 Vue/Pinia 中**必须要写**的函数。由于 Vue 是数据驱动的，DOM 拖拽完后，你必须在这个函数里同步修改仓库里的数据。

- 它接收一个事件对象 `evt`，里面包含了拖拽前后的关键信息：
    
    - **`evt.oldIndex`**：该元素被拖拽前的原始索引（从 0 开始算）。
        
    - **`evt.newIndex`**：该元素被拖拽后放下的新索引。
        

---

### 完整的配置模板示例

结合你在 `Tab.vue` 中的实际需求，你需要传入的内容大概是这样：

JavaScript

```
Sortable.create(wrapper, {
  // 1. 视觉配置
  animation: 300, 
  ghostClass: "sortable-ghost", // 拖拽时的影子样式（需自己在 CSS 中定义）

  // 2. 行为控制
  filter: ".is-affix", // 假设固定标签有这个类名，过滤掉不让拖

  // 3. 拖拽结束回调
  onEnd: (evt) => {
    // 获取拖拽前后的索引
    const { oldIndex, newIndex } = evt;
    
    // 如果原地放下，什么都不做
    if (oldIndex === undefined || newIndex === undefined || oldIndex === newIndex) return;

    // TODO: 拿着 oldIndex 和 newIndex 去 Pinia 的 tabsMenuList 数组里执行 splice 换位
  }
});
```