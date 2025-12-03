

### 📝 Vuex Getters 核心总结

#### 1. 定义

Getters 是 Vuex Store 中的计算属性 (Computed Properties)。

它就像 Vue 组件里的 computed 一样，用于对 State 中的数据进行加工、筛选、计算后再输出。

#### 2. 核心作用 (Why)

1. **复用性 (DRY)**：将处理数据的逻辑提取到 Store 中，避免在多个组件里重复写相同的代码。
    
2. **缓存性 (Caching)**：**这是最重要的特性。** 只有当依赖的 `State` 发生变化时，Getter 才会重新计算；否则直接返回缓存结果，极大优化性能。
    
3. **组合性**：Getter 也可以引用其他的 Getter。
    

#### 3. 语法结构

定义 Getter (在 store.js 中):

接收两个参数：

1. `state`: 访问原始数据。
    
2. `getters`: 访问其他的 getter。
    

JavaScript

```
getters: {
  // 基础用法
  doneTodos: (state) => {
    return state.todos.filter(todo => todo.done)
  },
  
  // 进阶用法：引用其他 getter
  doneTodosCount: (state, getters) => {
    return getters.doneTodos.length // 复用上面的结果
  }
}
```

#### 4. 组件中使用 (Usage)

**方式 A：直接访问 (属性访问)**

JavaScript

```
// 在组件的 computed 中
computed: {
  doneCount() {
    return this.$store.getters.doneTodosCount
  }
}
```

方式 B：辅助函数 (mapGetters)

最常用的简写方式。

JavaScript

```
import { mapGetters } from 'vuex'

export default {
  computed: {
    // 将 store 中的 getters 映射到局部计算属性
    ...mapGetters(['doneTodos', 'doneTodosCount'])
    
    // 或者取别名
    // ...mapGetters({ count: 'doneTodosCount' })
  }
}
```

---

#### 💡 一句话比喻

- **State** 是仓库里的**生鲜食材** (原始数据)。
    
- **Getters** 是大厨加工好的**成品菜肴** (处理后的数据)。
    
- 顾客 (组件) 通常更喜欢直接点菜 (Getters)，而不是自己去仓库拿菜洗菜 (在组件内重复逻辑)。