

### 📝 Vuex 四大辅助函数 (Map Helpers) 总结

#### 1. 核心概念

这四个方法是 Vuex 提供的语法糖。

作用：将 Store 中的数据 (State/Getters) 或方法 (Mutations/Actions) 映射为组件内部的属性或方法，让你不需要每次都写 this.$store.xxxx，从而简化代码。

#### 2. 分类记忆表 (关键)

请记住：**前两个是“读”数据的，后两个是“操作”逻辑的。**

|**函数名**|**对应 Vuex 概念**|**放在组件哪里?**|**作用**|**映射后怎么用?**|
|---|---|---|---|---|
|**mapState**|`State` (原始数据)|**computed**|获取仓库里的变量|`this.name`|
|**mapGetters**|`Getters` (加工数据)|**computed**|获取仓库里的计算结果|`this.bigCount`|
|**mapMutations**|`Mutations` (同步方法)|**methods**|获取修改数据的方法|`this.ADD()`|
|**mapActions**|`Actions` (异步方法)|**methods**|获取异步逻辑的方法|`this.fetchData()`|

#### 3. 语法关键点

必须使用 ES6 的 **展开运算符 (`...`)** 将它们合并到组件的配置项中。

**代码模板：**

JavaScript

```
<script>
// 0. 必须先引入
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  // 1. 数据类放在 computed
  computed: {
    // 这里的 ... 是把映射出来的对象，合并到当前 computed 里
    ...mapState(['count', 'user']), 
    ...mapGetters(['doubleCount'])
  },

  // 2. 方法类放在 methods
  methods: {
    ...mapMutations(['INCREMENT']),
    ...mapActions(['loginAsync'])
  }
}
</script>
```

#### 4. 一句话总结

- 想**偷懒**不写 `this.$store.state.xxx`？用 **`mapState`**。
    
- 想**偷懒**不写 `this.$store.getters.xxx`？用 **`mapGetters`**。
    
- 想**偷懒**不写 `this.$store.commit('xxx')`？用 **`mapMutations`**。
    
- 想**偷懒**不写 `this.$store.dispatch('xxx')`？用 **`mapActions`**。