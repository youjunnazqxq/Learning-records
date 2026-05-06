
### 如何定义这个变量？

在 Vue 3 的 `<script setup>` 语法中，由于登录表单通常包含多个字段（如用户名、密码），我们一般会使用 `reactive` 来定义一个响应式的对象。

代码写出来是这样的：

JavaScript

```
<script setup>
import { reactive } from 'vue'

// 这里就是你在定义 :model 所绑定的变量
const loginForm = reactive({
  username: '', // 初始值为空字符串
  password: ''  // 初始值为空字符串
})
</script>
```

### 为什么必须要定义成对象（如 `loginForm`）？

`<el-form>` 作为“大总管”，它需要一个统一的“账本”来记录所有输入框的数据。

- 这个 `loginForm` 对象就是“账本”。
    
- 里面的 `username` 和 `password` 就是“账本”里的具体条目。
    

当你把这个“账本”交给了 `<el-form>`（通过 `:model="loginForm"`），表单内部的各个输入框就知道该把用户敲进去的字存到哪里了。

接下来，你想看看表单里的每一行（`<el-form-item>`）是如何从这个“账本”里精准认领属于自己的那一条数据的吗？