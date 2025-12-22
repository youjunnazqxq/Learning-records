

### 1. 核心结构

一个完整的表单通常由三层组成：

1. **`el-form`**：最外层，负责绑定整个数据对象和校验规则。
    
2. **`el-form-item`**：中间层，负责显示标签（label）、校验错误信息以及布局。
    
3. **输入组件**：最内层，如 `el-input`，负责具体的数据输入。
    

---

### 2. 关键属性 (Props)

要让 `el-form` 正常工作，有三个属性是最常用的：

|**属性名**|**说明**|
|---|---|
|**`:model`**|**表单数据对象**。用于存放表单中所有字段的值（通常是一个对象）。|
|**`:rules`**|**表单验证规则**。定义哪些字段是必填的、长度限制或正则表达式等。|
|**`label-width`**|**标签宽度**。设置所有 `el-form-item` 标签的统一宽度（例如 `100px`）。|

---

### 3. 代码示例

这是一个典型的 `el-form` 使用场景：

HTML

```
<template>
  <el-form :model="userForm" :rules="myRules" ref="formRef" label-width="80px">
    
    <el-form-item label="用户名" prop="username">
      <el-input v-model="userForm.username"></el-input>
    </el-form-item>

    <el-form-item label="年龄" prop="age">
      <el-input v-model.number="userForm.age"></el-input>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref, reactive } from 'vue'

const userForm = reactive({
  username: '',
  age: ''
})

const myRules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
  ]
}
</script>
```

---

### 4. 主要功能总结

- **统一布局**：通过 `label-position` 可以一键切换标签是在上方还是左方。
    
- **数据双向绑定**：配合 `v-model` 轻松获取用户输入的内容。
    
- **强大的校验**：通过 `validate` 方法，可以一键检查整个表单是否符合规范，如果不符合，会自动在对应的输入框下显示红色提示。
    
- **表单重置**：调用 `resetFields()` 即可将所有表单项恢复初始值并清除校验痕迹。
    

**您是想了解如何配置表单校验规则，还是想知道如何进行表单的响应式布局？**