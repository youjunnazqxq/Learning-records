这是一个为您准备的精简版 `scoped` 笔记，适合直接抄在笔记本上或作为快速复习要点：

---

## Vue 配置项：scoped 样式总结

### 1. 作用

让样式在**局部生效**，防止 CSS 类名重复导致的**全局样式污染**。

### 2. 语法

HTML

```
<style scoped>
  /* 这里的样式只对当前组件有效 */
  .demo {
    background-color: skyblue;
  }
</style>
```

### 3. 实现原理 (面试考点)

Vue 底层利用 **PostCSS** 进行处理：

1. **HTML 层面**：给当前组件的所有 DOM 元素添加一个独一无二的自定义属性（如 `data-v-55c83`）。
    
2. **CSS 层面**：给编写的样式选择器自动添加对应的属性选择器（如 `.demo[data-v-55c83]`）。
    

### 4. 特殊场景：样式穿透

问题：使用了 scoped 后，无法修改子组件（或第三方库如 ElementUI）内部的样式。

解决：使用深度选择器（样式穿透）。

- **Vue 2**：`/deep/ .class` 或 `>>> .class`
    
- **Vue 3 / 通用**：`::v-deep .class` 或 `:deep(.class)`
    
