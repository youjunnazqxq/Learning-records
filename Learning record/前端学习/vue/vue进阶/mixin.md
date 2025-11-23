

## Vue 配置项：mixin (混入) 学习笔记

### 1. 核心功能

**mixin** 用于**复用配置**。

- **场景：** 当你发现两个或多个组件里写了完全一样的代码（比如一样的 `methods` 方法、一样的 `data` 数据，或者一样的生命周期钩子）时。
    
- **作用：** 可以把这些共用的配置提取出来，封装成一个单独的“混入对象”，然后在需要的组件里引入它。
    

### 2. 使用步骤

#### 第一步：定义混合 (Define)

通常新建一个 `.js` 文件（例如 `mixin.js`），导出一个包含 Vue 配置项的对象。

JavaScript

```
// mixin.js
export const myMixin = {
  data() {
    return {
      x: 100,
      y: 200
    }
  },
  methods: {
    showHello() {
      alert('你好啊！')
    }
  },
  mounted() {
    console.log('Mixin里的mounted触发了')
  }
}
```

#### 第二步：使用混合 (Use)

方式一：局部混入 (Local Mixin)

最常用。只在当前组件生效，不影响其他组件。

JavaScript

```
import { myMixin } from './mixin.js' // 1. 引入

export default {
  name: 'Student',
  data() { ... },
  mixins: [myMixin] // 2. 配置：注意这里是数组，可以混入多个
}
```

方式二：全局混入 (Global Mixin)

一旦使用，所有组件（包括 App.vue 甚至第三方组件）都会拥有这些配置。慎用！

JavaScript

```
// main.js
import { myMixin } from './mixin.js'

Vue.mixin(myMixin) // 全局注册
```

### 3. ⚠️ 重要的“合并规则” (笔记补充)

当组件自己的配置和 Mixin 的配置发生冲突时，Vue 有一套默认规则：

1. **数据对象 (data) & 方法 (methods)：**
    
    - **组件优先。** 如果名字一样（冲突了），以组件自己定义的为准。
        
    - 如果名字不一样，则合并在一起。
        
2. **生命周期钩子 (mounted, created 等)：**
    
    - **都会执行。**
        
    - **顺序：** Mixin 里的钩子 **先执行**，组件自己的钩子 **后执行**。
        

---

我可以为你做下一步：

如果你学到了 plugin (插件) 这一节，想知道 Mixin (混入) 和 Plugin (插件) 有什么区别，我可以为你做个对比总结。