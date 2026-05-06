在 Element UI / Element Plus 框架中，**`el-input`** 是最基础、也是最常用的**输入框组件**。

简单来说，它就是 HTML 原生 `<input>` 或 `<textarea>` 的“加强版”。它不仅美化了外观，还集成了许多实用的功能（如一键清空、密码显示、前缀/后缀图标等）。

---

### 1. 基础用法

它通过 `v-model` 实现数据的双向绑定。

HTML

```
<el-input v-model="userName" placeholder="请输入用户名"></el-input>
```

---

### 2. 核心特性

`el-input` 相比原生输入框，多了很多开箱即用的功能：

- **各种类型 (`type`)**：通过修改 `type` 属性，可以变成文本框 (`text`)、密码框 (`password`) 或文本域 (`textarea`)。
    
- **一键清空 (`clearable`)**：加上这个属性后，输入框右侧会出现一个 “X”，点击即可清空内容。
    
- **密码切换 (`show-password`)**：针对密码类型，可以点击“小眼睛”图标切换明文/密文显示。
    
- **带图标的输入框**：支持在输入框的前部 (`prefix`) 或后部 (`suffix`) 添加图标。
    
- **复合型输入框**：可以在输入框的前面或后面追加固定的标签或按钮（比如用来输入 URL 的 `http://`）。
    

---

### 3. 不同形态展示

|**功能**|**代码示例**|**效果说明**|
|---|---|---|
|**密码框**|`<el-input type="password" show-password />`|隐藏输入内容，可点击图标查看。|
|**文本域**|`<el-input type="textarea" :rows="3" />`|多行输入，可调整高度。|
|**计数器**|`<el-input maxlength="10" show-word-limit />`|右下角实时显示已输入的字数。|
|**尺寸控制**|`size="large" / "small"`|调整输入框的大小以适应 UI 风格。|

---

### 4. 配合 `el-form` 使用

正如你之前问到的 `el-form`，`el-input` 通常是作为 `el-form-item` 的子组件出现的。

HTML

```
<el-form-item label="密码" prop="pass">
  <el-input 
    v-model="formData.password" 
    type="password" 
    prefix-icon="Lock"
    show-password 
  />
</el-form-item>
```

### 总结

`el-input` 是你和用户进行**文本交互**的首选工具。如果你需要用户输入一段文字、一个数字或一份说明，都会用到它。

**需要我演示一下如何给 `el-input` 增加自定义的前缀图标或者搜索按钮吗？**