你需要下载的包名是 `pinia-plugin-persistedstate`。



Bash

```
# 使用 npm 下载
npm install pinia-plugin-persistedstate
```

顺便一提，在重构像 Geeker-Admin 这种企业级项目时，使用 `pnpm` 来管理依赖体验会更好且速度更快。如果你当前的环境中配置了它，也可以直接运行：

Bash

```
pnpm add pinia-plugin-persistedstate
```



**准备好进入具体的 Store 模块（例如 `GlobalStore`）进行笔记梳理了吗？**
Markdown

````
# Pinia 持久化插件 (Persist) 核心接口配置指南

## 1. 插件的引入与全局挂载
在使用 `persist` 接口前，必须先在 Pinia 实例上注册该插件。这通常在单独的 `src/stores/index.ts` 文件中完成，以保持逻辑解耦。

```typescript
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
// 核心步骤：将持久化插件挂载到 pinia 实例上
pinia.use(piniaPluginPersistedstate)

export default pinia
````

---

## 2. 基础使用：一键开启持久化

在定义 Store 时（特别是 Setup 语法下），`defineStore` 接收**第三个参数**作为配置对象。

最简单的方式是直接传入 `persist: true`。这会将该 Store 返回的所有 State，使用默认的 Store ID 作为 Key，全量保存到 `localStorage` 中。

TypeScript

```
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useDemoStore = defineStore(
  'demo', // 这是 Store ID，默认也会作为 localStorage 的 Key
  () => {
    const username = ref('admin')
    const count = ref(0)
    return { username, count }
  },
  {
    // 基础用法：一键开启全量持久化
    persist: true 
  }
)
```

---

## 3. 进阶使用：Persist 接口属性详解 (对象配置)

在企业级项目中（如 Geeker-Admin），为了性能和规范，我们几乎不会用 `persist: true`，而是传入一个 **Persist 配置对象** 来进行精细化控制。

以下是 `persist` 对象中最常用的三个核心接口属性：

TypeScript

```
// ... 省略 setup 逻辑
  {
    persist: {
      // 1. key (自定义存储名称)
      // 作用：覆盖默认的 Store ID。防止不同项目在同一个 localhost 端口下运行时，缓存相互污染。
      key: 'geeker-demo-store',

      // 2. storage (指定存储介质)
      // 作用：默认是 localStorage。如果你希望数据在关闭浏览器页签后就销毁，可以改为 sessionStorage。
      storage: sessionStorage,

      // 3. paths (白名单按需存储) 🌟 最常用
      // 作用：数组格式，传入需要持久化的 state 变量名。未写入数组的变量将只存在于内存中。
      paths: ['username'] // 这里只有 username 会被缓存，count 刷新页面后会重置为 0
    }
  }
```

### 补充进阶接口（按需了解）：

- **`serializer`**: 自定义序列化器。默认使用 `JSON.stringify` 和 `JSON.parse`。如果你的 state 里存了 `Set`、`Map` 或是复杂的 `Date` 对象，可以通过这个接口配置自定义的转换逻辑。
    
- **`beforeRestore` / `afterRestore`**: 钩子函数。可以在数据从本地存储恢复到 Pinia 实例之前或之后执行特定的逻辑（比如打印日志或发送埋点数据）。
    

```

***

掌握了这个配置对象，你在处理状态存储时就能游刃有余了。

**接下来，你想直接实战一下，看看在 `GlobalStore` 中如何利用这些接口来持久化侧边栏的折叠状态和全局主题颜色吗？**
```