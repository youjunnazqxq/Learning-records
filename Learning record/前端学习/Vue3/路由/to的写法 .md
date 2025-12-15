
### 1. 字符串写法

直接传入一个字符串路径。这是最简单的方式，适用于不需要动态参数或参数较简单的场景。

- **基础跳转**：
    
    代码段
    
    ```
    <router-link to="/home">主页</router-link>
    ```
    
- **带参数跳转**（直接拼接）：
    
    代码段
    
    ```
    <router-link to="/news/detail?a=1&b=2">跳转</router-link>
    
    <router-link to="/news/detail/001/新闻001">跳转</router-link>
    ```
    

### 2. 对象写法

传入一个对象，需要使用 `v-bind` (即 `:to`)。这种方式更灵活，特别是在处理复杂的参数传递时。

- **使用 `path` 跳转**：
    
    代码段
    
    ```
    <router-link :to="{path:'/home'}">Home</router-link>
    ```
    
- 使用 name 跳转（命名路由）：
    
    可以通过路由配置中的 name 属性直接跳转，这在路径较长时非常有用。
    
    代码段
    
    ```
    <router-link :to="{name:'guanyu'}">跳转</router-link>
    ```
    
- **传递 `query` 参数**（配合 `path` 或 `name`）：
    
    代码段
    
    ```
    <RouterLink 
      :to="{
        path:'/news/detail',
        query:{
          id: news.id,
          title: news.title
        }
      }"
    >
      {{news.title}}
    </RouterLink>
    ```
    
- **传递 `params` 参数**（**必须配合 `name`**）：
    
    > **注意**：如果使用对象写法传递 `params` 参数，必须使用 `name`，不能使用 `path`。
    
    代码段
    
    ```
    <RouterLink 
      :to="{
        name:'xiang', // 必须使用 name
        params:{
          id: news.id,
          title: news.title
        }
      }"
    >
      {{news.title}}
    </RouterLink>
    ```
    

### 总结

|**写法**|**形式**|**示例**|**备注**|
|---|---|---|---|
|**字符串写法**|`to="..."`|`to="/home"`|简单直接，适合静态路径|
|**对象写法**|`:to="{...}"`|`:to="{path:'/home'}"`<br><br>  <br><br>`:to="{name:'user'}"`|灵活，支持 `query`/`params` 对象传参|