

### 一、 核心属性 (Attributes)

我们可以把它的属性分为“数据绑定”、“UI 展示”和“状态控制”三类：

#### 1. 数据绑定类

- **`v-model` (最常用)**：双向绑定开关的值。默认情况下，打开是 `true`，关闭是 `false`。
    
- **`active-value` / `inactive-value`**：自定义开关的值。这非常重要！如果你的后端数据库存的不是布尔值，而是数字 `1`（代表开）和 `0`（代表关），或者字符串 `'yes'` 和 `'no'`，你就可以用这两个属性来进行映射，而不需要自己手动转换数据格式。
    
    - 示例：`<el-switch v-model="status" :active-value="1" :inactive-value="0" />`
        

#### 2. UI 展示类

- **`active-text` / `inactive-text`**：在开关的右侧（或左侧）显示文字描述（如“开启”、“关闭”）。
    
- **`inline-prompt`**：布尔值。如果设为 `true`，上面设置的文字描述会**内嵌到开关的滑块里面**，而不是显示在外面。这在空间紧凑的地方非常实用。
    
- **颜色控制 (CSS 变量)**：在 Vue 3 的 Element Plus 中，官方推荐通过内联样式修改 CSS 变量来改变开关颜色，而不是旧版的属性。
    
    - 示例：`<el-switch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" />`
        
- **`active-icon` / `inactive-icon`**：可以在开关内部显示具体的图标（比如你代码里暗黑模式如果用原生 switch，就可以一边放太阳图标，一边放月亮图标）。
    

#### 3. 状态控制类

- **`disabled`**：布尔值。设为 `true` 时，开关变为灰色，不可点击。通常用于权限控制（比如普通用户不能修改某项系统设置）。
    
- **`loading`**：布尔值。设为 `true` 时，开关滑块上会出现一个旋转的加载动画，并且此时不可点击。这在等待接口响应时极其好用。
    

---

### 二、 核心事件 (Events)

- **`@change`**：当开关的值发生变化时触发。它会把你切换后的最新值作为参数传给你的回调函数。你代码里的 `@change="setAsideTheme"` 就是在开关拨动后，去执行切换侧边栏样式的逻辑。
    

---

### 三、 实战开发中的注意点 (坑点)

在真实业务中使用 `<el-switch>` 时，最容易在以下两个场景里翻车：

#### 1. 数据类型的隐式转换问题

如果你使用了 `active-value="1"`（注意这里 `1` 外面没有冒号，代表它传的是**字符串** `"1"`），但你后端要求的是**数字** `1`，就会导致状态匹配不上。

**避坑指南**：如果要绑定数字或布尔值，一定要加上 `v-bind`（即冒号），写成 `:active-value="1"`。

#### 2. 异步切换（乐观更新 vs 悲观更新）

默认情况下，用户点击开关，滑块会**立刻**滑到另一边（乐观更新）。但如果这个操作需要调用后端 API 去保存，而 API 请求失败了，这时候界面显示的是“开”，数据库里其实还是“关”，这就造成了数据不一致。

**避坑指南**：Element Plus 提供了一个非常强大的属性叫 **`before-change`**。

- 它接收一个函数，可以返回一个 `boolean` 或者 `Promise`。
    
- 你可以把 API 请求写在这个函数里。如果 API 返回成功，`Promise.resolve()`，开关才会真正滑过去；如果 API 报错，`Promise.reject()`，开关会弹回原位，有效防止数据假死。
    

JavaScript

```
// before-change 使用示例
const beforeChange = () => {
  return new Promise((resolve, reject) => {
    // 模拟调用接口
    api.updateSettings().then(() => {
      resolve(true) // 接口成功，允许开关切换
    }).catch(() => {
      reject(new Error('Error')) // 接口失败，阻止开关切换
    })
  })
}
```

你的代码目前是在纯前端做布局状态管理（存入 Pinia），所以直接用 `v-model` 配合 `@change` 就足够了，不需要用到 `before-change` 这种重型逻辑。