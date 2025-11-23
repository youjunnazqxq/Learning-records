
## Vue 中 `ref` 属性使用总结

### 1. 核心作用

`ref` 被用来给元素或子组件注册引用信息。

- **通俗理解：** 它是 Vue 中专门用来替代 `id` 和 `document.getElementById` 的“身份证系统”。
    
- **目的：** 为了在 JavaScript 代码中直接操作 **DOM 元素** 或 **组件实例**。
    

### 2. “ref 在哪里，得到的就在哪里”（核心区别）

这是最重要的考点，根据 `ref` 加的标签类型不同，拿到的东西截然不同：

|**加在什么标签上**|**也就是**|**this.$refs.xxx 获取到的内容**|**备注**|
|---|---|---|---|
|**HTML 标签**|`<h1 ref="title">`|**真实 DOM 元素**|等同于 `document.getElementById`，可以直接操作样式、焦点等。|
|**组件标签**|`<School ref="sch">`|**组件实例对象 (vc)**|可以访问该子组件的 `data`、调用子组件的 `methods`。|

### 3. 语法格式 (Options API)

- **第一步（打标识）：** 在模板中添加 `ref` 属性。
    
    HTML
    
    ```
    <h1 ref="myTitle">你好</h1>
    <School ref="mySchool"/>
    ```
    
- **第二步（找标识）：** 在 JS 中通过 `this.$refs` 获取。
    
    JavaScript
    
    ```
    console.log(this.$refs.myTitle);  // 拿到 h1 的 DOM
    console.log(this.$refs.mySchool); // 拿到 School 组件的实例
    ```
    

### 4. 重要注意事项

1. **唯一性：** 虽然 Vue 不会强制报错，但尽量保证 `ref` 的名字在当前组件内是唯一的，避免获取时冲突。
    
2. **时机问题：** `ref` 只有在组件 **挂载完成 (mounted)** 之后才能访问。
    
    - 如果在 `created` 生命周期里打印 `this.$refs.xxx`，通常是 `undefined`，因为这时候 DOM 还没生成。
        
3. **过度使用：** Vue 提倡“数据驱动视图”。如果只是为了修改文字内容，应该优先用 `{{ msg }}` 或 `v-model`，而不是用 `ref` 去手动改 `innerHTML`。`ref` 应主要用于必须操作 DOM 的场景（如：输入框聚焦、视频播放、集成第三方图表库）。
    

---

我可以为你做下一步：

如果你在做笔记时需要 “Vue 2 的 this.$refs 和 Vue 3 的 ref 变量有什么区别” 的对比表，我可以为你整理一份。