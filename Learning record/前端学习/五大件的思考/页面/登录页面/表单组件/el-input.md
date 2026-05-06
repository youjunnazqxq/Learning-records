
### 一、 绝对不能漏掉的核心属性

- **`v-model`（双向数据绑定）**
    
    - **作用**：建立输入框和你的响应式变量（`loginForm`）之间的双向连接。
        
    - **怎么用**：必须精确绑定到具体的字段上，比如 `v-model="loginForm.username"`。这样用户敲进去的每一个字，都会立刻同步到你的 JS 变量里；反之，你在 JS 里把变量清空，输入框也会立刻变空白。
        

### 二、 登录框常用的“体验加分”属性

为了让登录框看起来专业且好用，以下这几个属性你几乎每次都会用到：

- **`placeholder`（占位提示文本）**
    
    - **作用**：输入框为空时显示的灰色提示语。
        
    - **怎么用**：`placeholder="请输入用户名"`。
        
- **`type`（输入框类型）**
    
    - **作用**：定义输入框的性质。默认为普通文本 `text`。
        
    - **怎么用**：在写密码框时，**必须**加上 `type="password"`，这样用户输入的字符才会变成黑圆点，保护隐私。
        
- **`show-password`（密码显示/隐藏开关）**
    
    - **作用**：Element 提供的一个非常贴心的语法糖。只要在密码框加上这个属性，输入框右侧就会自动出现一个“小眼睛”图标，用户点击就能切换查看明文密码。
        
- **`clearable`（一键清空）**
    
    - **作用**：加上后，只要输入框里有内容，右侧就会悬浮一个 `x` 图标，点击直接清空当前行。常用于用户名输入框。
        
- **`prefix-icon` / `suffix-icon`（前缀/后缀图标）**
    
    - **作用**：在输入框的头部或尾部加入图标。登录框通常会在头部加个“小人头（User）”和“锁（Lock）”，让界面更直观。
        

### 三、 提升交互的实用事件

- **`@keyup.enter`（回车键监听）**
    
    - **作用**：很多用户输完密码后，习惯直接敲击键盘上的回车键（Enter）来登录，而不是去用鼠标点“登录”按钮。
        
    - **怎么用**：在密码框上绑定 `@keyup.enter="handleLogin"`，按下回车就能直接调用登录函数。
        

---

### 标准登录框 `<el-input>` 组合示例

把上面这些属性组合起来，你的用户名和密码输入框代码应该是这样的：

HTML

```
<el-form-item prop="username">
  <el-input 
    v-model="loginForm.username" 
    placeholder="请输入用户名" 
    prefix-icon="User" 
    clearable 
  />
</el-form-item>

<el-form-item prop="password">
  <el-input 
    v-model="loginForm.password" 
    type="password" 
    placeholder="请输入密码" 
    prefix-icon="Lock" 
    show-password 
    @keyup.enter="handleLogin" 
  />
</el-form-item>
```

现在，组成登录表单的“三剑客”（`el-form` 统管全局、`el-form-item` 负责排版和验证提示、`el-input` 负责收集输入）我们已经全部梳理完毕了。

结构搭好之后，最重要的就是点击“登录”按钮时的逻辑处理了。你想看看在 `handleLogin` 方法里，如何触发这套表单的全局校验，并准备把数据发给后端吗？