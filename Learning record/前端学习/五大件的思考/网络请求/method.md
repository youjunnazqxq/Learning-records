
### 1. GET (获取数据)

用于向服务器请求获取资源。参数会附加在 URL 的末尾（查询字符串）。

- **语法:**
    
    JavaScript
    
    ```
    // 别名语法
    axios.get('/user/list', { 
      params: { role: 'admin', page: 1 } 
    });
    
    // 或者基础对象语法
    axios({
      method: 'get',
      url: '/user/list',
      params: { role: 'admin', page: 1 }
    });
    ```
    

### 2. POST (提交/新建数据)

用于向服务器提交数据，通常用于创建新记录（如注册用户、提交表单）。数据包含在请求体（Request Body）中。

- **语法:**
    
    JavaScript
    
    ```
    axios.post('/user/create', { 
      username: 'xiaoming', 
      age: 18 
    });
    ```
    

### 3. PUT (完整更新数据)

用于更新服务器上的资源。通常是将整个对象完整替换。数据包含在请求体中。

- **语法:**
    
    JavaScript
    
    ```
    axios.put('/user/update/1', { 
      username: 'xiaoming_new', 
      age: 20 
    });
    ```
    

### 4. PATCH (局部更新数据)

也用于更新资源，但通常只提交需要修改的特定字段，而不是完整替换。

- **语法:**
    
    JavaScript
    
    ```
    axios.patch('/user/update-status/1', { 
      status: 'active' 
    });
    ```
    

### 5. DELETE (删除数据)

用于请求服务器删除指定的资源。

- **语法:**
    
    JavaScript
    
    ```
    axios.delete('/user/delete/1'); 
    ```
    

---

### ⚠️ 最核心的注意事项（极易踩坑）

在使用这些方法时，绝大多数新手都会在**传参方式**上栽跟头。请牢记以下三点：

**第一：分清 `params` 和 `data`**

- **`params` (Query 参数):** 专属于 `GET` 和 `DELETE`。参数会被拼接到 URL 后面（如 `?id=1`）。
    
- **`data` (Body 数据):** 专属于 `POST`、`PUT` 和 `PATCH`。数据会被放在请求体内，URL 上看不见，更安全，且能传输海量数据。
    

**第二：DELETE 方法的语法怪癖**

如果你需要在 `DELETE` 请求的 Body 中传递数据（虽然不常见，但有些后端会这么要求），它的别名语法非常特殊：

JavaScript

```
// POST 的第二个参数直接是数据
axios.post('/delete-users', [1, 2, 3]); 

// DELETE 的第二个参数是配置对象！数据必须包裹在 data 属性里！
axios.delete('/delete-users', { 
  data: [1, 2, 3] 
}); 
```

**第三：Content-Type (请求头类型)**

Axios 会自动将你传入的 JS 对象序列化为 JSON 格式（`application/json`）。但如果后端要求接收传统的表单格式，或者你需要**上传文件**（图片、视频），你就必须使用 `FormData` 对象，Axios 会自动将请求头切换为 `multipart/form-data`。


### 1. GET 请求的参数位置

在 HTTP 协议规范里，GET 请求通常是没有请求体（Request Body）的。它的数据都拼接在 URL 后面。

因此，Axios 设计的 `get` 函数签名是：**`axios.get(url[, config])`**

- **第一个参数：** 必填的 `url`。
    
- **第二个参数：** 可选的 **配置对象（config）**。
    
- **结论：** 因为你需要传递的 `role: 'admin'` 属于查询参数，所以你必须把它放在配置对象的 `params` 属性里传进去。这就是为什么外面有一层 `{}`。
    

### 2. POST 请求的参数位置

POST 请求最核心的目的是提交庞大的数据，这些数据必须放在请求体（Body）中。

为了让开发者写起来最爽，Axios 设计的 `post` 函数签名是：**`axios.post(url[, data[, config]])`**

- **第一个参数：** 必填的 `url`。
    
- **第二个参数：** 可选的 **请求体数据（data/body）**。Axios 会自动把这个对象塞进请求体里。
    
- **第三个参数：** 才是那个 **配置对象（config）**（比如你想在这个请求里单独加个自定义的 Headers，或者设置超时时间，就要写在第三个参数里）。