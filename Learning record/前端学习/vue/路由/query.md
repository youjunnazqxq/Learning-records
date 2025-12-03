

### 1. 字符串写法 (String Syntax)

这是最原始的写法，直接把参数拼接在网址后面。

HTML

```
<router-link :to="`/home/message/detail?id=666&title=你好`">跳转</router-link>
```

- **特点：** 简单粗暴，手写 `?` 和 `&`。
    
- **缺点：** 如果参数很多，或者参数里包含特殊符号（比如空格、&、?），拼接起来很容易出错，且难以阅读。
    

### 2. 对象写法 (Object Syntax) —— **强烈推荐**

这是 Vue Router 提供的更规范的写法。

JavaScript

```
// 截图中的第二段代码
<router-link 
  :to="{
    path: '/home/message/detail', // 去哪里？
    query: {                      // 带什么货？
      id: 666,
      title: '你好'
    }
  }"
>
  跳转
</router-link>
```

- **`path`**: 路由的路径（地址）。
    
- **`query`**: 一个对象，专门放你要传的参数。
    
- **优点：** * **清晰：** 结构一目了然。
    
    - **自动处理：** Vue 会自动帮你把这个对象转换成 `?id=666&title=你好`。
        
    - **安全：** 如果你的数据里有特殊字符，Vue 会自动帮你做 URL 编码，防止出错。
        

### 3. URL 最终长什么样？

无论你用上面哪种写法，当你点击“跳转”后，浏览器地址栏都会变成：

`http://localhost:8080/#/home/message/detail?id=666&title=你好`

### 4. 怎么拿到这个数据？

在目标组件（Detail 组件）里，通过“身份证” `$route` 来拿：

- `this.$route.query.id` 拿到 `666`
    
- `this.$route.query.title` 拿到 `'你好'`
    

### 总结

在你的截图中，**Query 参数就是那个 `query: { ... }` 对象里的内容**。它是用来告诉目标页面：“我要看具体的哪一条信息”。

---

你可以让我：

除了 Query 参数，路由还有一种把参数直接写在路径里的方式（比如 /detail/666），叫做 Params 参数。需要我为你解释 Query 参数和 Params 参数在写法和功能上的具体区别吗？