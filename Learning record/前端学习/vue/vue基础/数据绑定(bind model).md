
# 📝 Vue 数据绑定核心笔记

在 Vue 中，数据绑定是连接 **Data (数据源)** 和 **View (页面展示)** 的桥梁。主要分为“单向”和“双向”两种模式。

## 1. 单向绑定 (One-Way Binding)

- **指令名称**：`v-bind`
    
- **简写方式**：**`:`** (英文冒号)
    
- **数据流向**：`Data` $\rightarrow$ `Page`
    
    - 数据变了，页面会自动更新。
        
    - 但在页面上修改（如强行改 DOM），不会影响 Data。
        
- **适用场景**：**通用属性设置**。
    
    - 凡是用户**“只看不能改”**的地方。
        
    - 例如：标签的 `href`、`src`、`class`、`style`、`id` 等。
        
- **代码示例**：
    
    HTML
    
    ```
    <a v-bind:href="school.url">去学习</a>
    
    <a :href="school.url">去学习</a>
    ```
    

---

## 2. 双向绑定 (Two-Way Binding)

- **指令名称**：`v-model`
    
- **简写方式**：`v-model` (通常直接写，不需要冒号)
    
    - _注：`v-model:value` 等价于 `v-model`。_
        
- **数据流向**：`Data` $\leftrightarrow$ `Page`
    
    - **去程**：Data 里的初始值会填入输入框。
        
    - **回程**：用户在输入框**打字修改**，Data 里的值也会**同步变化**。
        
- **适用场景**：**表单交互元素**。
    
    - 凡是需要**“收集用户输入”**的地方。
        
    - 必须用在表单类元素上：`<input>`, `<select>`, `<textarea>`。
        
- **底层原理**：
    
    - 它操作的是元素的 **`value` 属性**（针对大多数输入框）。
        
    - 它监听的是元素的 **`input` 事件**（一旦有输入就触发更新）。
        
- **代码示例**：
    
    HTML
    
    ```
    <input type="text" v-model="username">
    ```
    

---

## ⚖️ 核心对比表 (重点背诵)

|**维度**|**v-bind (单向)**|**v-model (双向)**|
|---|---|---|
|**简写**|**`:`**|`v-model`|
|**箭头示意**|Data $\rightarrow$ Page|Data $\leftrightarrow$ Page|
|**核心作用**|**展示**数据|**收集**数据|
|**适用标签**|所有 HTML 标签|**仅限表单元素** (`input` 等)|
|**操作属性**|你指定的任何属性 (href, src...)|默认操作 `value` 属性|
|**生活比喻**|就像**广播** (只能听)|就像**打电话** (有来有回)|

---

## 💡 避坑指南

1. **不要乱用 v-model**：如果你写 `<div v-model="x">` 是会报错的，因为 `div` 没法输入，没有 `value` 属性让 Vue 去绑定。
    
2. **区分引号内容**：
    
    - `v-model="name"` $\rightarrow$ 去 data 里找叫 `name` 的变量。
        
    - `value="name"` $\rightarrow$ 这个输入框里的字就是 "name" (普通字符串)。
        
3. **优先级**：如果一个标签同时写了 `:value="x"` 和 `v-model="y"`，`v-model` 的优先级通常更高，因为它负责接管 `value`。