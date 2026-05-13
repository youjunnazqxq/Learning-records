

### 一、 核心心智模型 (Grid 是什么？)

记住**二维布局**和**网格线**：

- **二维布局**：与 Flex 只能处理一维不同，Grid 能够同时处理行与列，是一个二维的框架性布局结构。
    
- **核心角色与概念**：
    
    - **容器 (Container)**：设置了 `display: grid`（块级）或 `display: inline-grid`（行内）的外层元素，会触发网格布局算法。
        
    - **项目 (Item)**：容器的顶层子元素（注意：仅限顶层子元素，孙子元素不是）。
        
    - **网格线 (Grid Line)**：纵横相交划分网格的线条，用来给项目精确定位。
        

---

### 二、 容器属性 (Container) —— 划分与控制全局

作用于外层父元素，用于“画出网格”并定义内部元素的“整体排布”。可以分为 **4 组**来记忆：

|**分组**|**属性名**|**作用**|**核心要点 / 常用值**|
|---|---|---|---|
|**1. 画网格**|`grid-template-columns`<br><br>  <br><br>`grid-template-rows`|声明列宽和行高|决定有几行几列。支持 px, %, 以及专属函数。|
||`grid-auto-columns`<br><br>  <br><br>`grid-auto-rows`|设置隐式网格的宽高|处理被挤到现有网格外部的项目尺寸。|
|**2. 画间距**|`grid-gap` (及行列细分)|设置行间距 (`row-gap`) 和列间距 (`column-gap`)|`grid-gap` 是两者的简写形式。|
|**3. 划区域**|`grid-template-areas`|将多个单元格合并、划分并命名区域|不需要利用的区域用点 (`.`) 表示。|
||`grid-auto-flow`|划分网格后，子元素的自动放置顺序|默认 `row` (先行后列)。改为 `column` 则是先列后行。|
|**4. 全局对齐**|`justify-items`<br><br>  <br><br>`align-items`<br><br>  <br><br>`place-items`|单元格**内部内容**的水平/垂直对齐|start, end, center, **stretch (默认拉伸)**。place-items 为合并简写。|
||`justify-content`<br><br>  <br><br>`align-content`<br><br>  <br><br>`place-content`|**整个网格区域**在容器内的水平/垂直对齐|start, end, center, stretch, space-around, space-between, space-evenly。|

---

### 三、 项目属性 (Item) —— 定位个体

作用于子元素，控制自身“放在哪个格子”、“跨越几个格子”以及“自身如何对齐”。分为 **2 组**记忆：

|**分组**|**属性名**|**作用**|**核心要点 / 常用值**|
|---|---|---|---|
|**1. 找位置**|`grid-column-start` / `end`<br><br>  <br><br>`grid-row-start` / `end`|基于“网格线”精确定位项目的四个边框|填入网格线的序号（如 `grid-column-start: 2` 表示左边框在第二根垂直线）。|
||`grid-area`|将项目直接放在指定的命名区域|需配合父容器的 `grid-template-areas` 使用。|
|**2. 个体对齐**|`justify-self`<br><br>  <br><br>`align-self`<br><br>  <br><br>`place-self`|单个项目在其单元格内的水平/垂直对齐|与 items 系列一致 (start, end, center, stretch)，但仅覆盖并作用于自身。|

---

### 四、 重点取值函数与关键字 (网格排版利器)

定义网格轨道（`grid-template-columns/rows`）时，除了写死像素，这些专属关键字非常关键：

- **`repeat(次数, 值)`**：简写重复的值，避免冗余代码。
    
- **`auto-fill`**：自动填充功能，只要浏览器容纳得下，就在一行/列中尽可能多放置单元格。
    
- **`fr` (fraction片段)**：用于表示比例关系，按比例瓜分剩余空间。
    
- **`minmax(最小值, 最大值)`**：设定长度的弹性范围，保证网格项目在合理的区间内自适应。
    
- **`auto`**：长度由浏览器自身决定。
    

---

### 五、 适用场景与兼容性

1. **应用场景**：擅长将页面划分为几个主要区域并处理层次关系。如居中、两列布局、三列布局等复杂结构，用 Grid 实现非常容易。
    
2. **兼容性提示**：总体兼容性不错，但在 IE 10 以下不支持。此外，目前在手机端的支持还不算太友好（移动端当前仍更推荐 Flexbox）。