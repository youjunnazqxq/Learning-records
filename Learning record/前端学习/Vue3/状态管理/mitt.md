

### 📝 Vue3 组件通信：mitt

#### 1. 核心作用

替代 Vue2 的 EventBus，实现任意组件（兄弟、祖孙等）之间的通信。

#### 2. 安装与配置

**第一步：安装**

PowerShell

```
npm i mitt
```

第二步：配置全局 Emitter

新建文件 src/utils/emitter.ts，创建一个全局共享的发射器对象。

TypeScript

```
// 引入 mitt
import mitt from "mitt";

// 创建 emitter
const emitter = mitt()

// 暴露 emitter
export default emitter
```

---

#### 3. 如何使用

接收数据 (绑定事件)

通常在挂载时绑定，务必在卸载时解绑（防止内存泄漏）。

TypeScript

```
import emitter from "@/utils/emitter";
import { onUnmounted } from "vue";

// 1. 绑定事件：当 'send-toy' 被触发时执行回调
emitter.on('send-toy', (value) => {
  console.log('send-toy事件被触发', value)
})

// 2. 解绑事件：组件卸载前清理
onUnmounted(() => {
  emitter.off('send-toy')
})
```

发送数据 (触发事件)

在合适的时机（如点击按钮）触发事件。

TypeScript

```
import emitter from "@/utils/emitter";

function sendToy() {
  // 触发 'send-toy' 事件，并携带数据
  emitter.emit('send-toy', '我是数据')
}
```

---

**💡 总结流程：**

1. **初始化**：创建一个全局的 `emitter.ts`。
    
2. **订阅 (On)**：接收方 `emitter.on('名字', 回调)`。
    
3. **发布 (Emit)**：发送方 `emitter.emit('名字', 数据)`。
    
4. **清理 (Off)**：接收方 `onUnmounted` 中 `emitter.off`。