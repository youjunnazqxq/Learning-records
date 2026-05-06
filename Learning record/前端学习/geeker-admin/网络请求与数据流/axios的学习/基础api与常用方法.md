没问题，那我们就正式进入 **第一层级：基础 API 与传参** 的详细拆解。

为了让你学得更透彻，我们结合你在 `geeker-admin`（后台管理系统）中一定会遇到的 **“增删改查” (CRUD)** 场景来讲。

在后台管理系统中，我们对数据的操作无非就是这四种。Axios 刚好对应了 HTTP 的四种主要方法。

---

### 1. 核心四件套：GET, POST, PUT, DELETE

请记住这四种方法对应的业务含义：

|**方法**|**英文**|**业务含义**|**就像...**|**传参重点**|
|---|---|---|---|---|
|**GET**|Read|**查** (获取数据)|去公告栏读通知|用 `params` (拼在 URL 后)|
|**POST**|Create|**增** (新建数据)|往意见箱投信|用 `data` (放在信封里)|
|**PUT**|Update|**改** (修改数据)|把旧文件拿出来改好放回去|用 `data` (放在信封里)|
|**DELETE**|Delete|**删** (删除数据)|撕掉一张纸|只要告诉 ID 就行|

#### ① GET 请求（查）

**场景**：获取用户列表、查询详情。

**关键**：数据暴露在 URL 上，**不要**传密码等敏感信息。

JavaScript

```
// 写法：axios.get(url, config)
axios.get('/user/list', {
  params: {
    status: 'active', // 只要活跃用户
    page: 1           // 第一页
  }
});
// 实际发出的请求：GET /user/list?status=active&page=1
```

#### ② POST 请求（增）

**场景**：新增一个用户、登录。

**关键**：数据在 Body 里，安全，容量大。

JavaScript

```
// 写法：axios.post(url, data, config)
axios.post('/user/add', {
  name: 'Jack',
  age: 18,
  gender: 'male'
});
// 实际发出的请求：POST /user/add
// Body: { "name": "Jack", "age": 18, "gender": "male" }
```

#### ③ PUT 请求（改）

**场景**：修改用户信息。

**关键**：用法和 POST 几乎一模一样！区别在于语义（告诉后端我是来“更新”的）。

JavaScript

```
// 写法：axios.put(url, data, config)
axios.put('/user/update', {
  id: 1001,      // 必须告诉后端改谁
  name: 'Jack New' // 改成什么
});
```

#### ④ DELETE 请求（删）

**场景**：删除一个用户。

**关键**：通常只需要传一个 ID。

**注意**：它的参数写法和 GET 类似（放在 config 里），但也支持 data（看后端怎么设计，通常用 URL 参数多）。

JavaScript

```
// 写法：axios.delete(url, config)
axios.delete('/user/delete', {
  params: {
    id: 1001
  }
});
// 实际发出的请求：DELETE /user/delete?id=1001
```

---

### 2. 万能公式：`axios(config)`

虽然上面 `axios.get`、`axios.post` 很常用，但在 `geeker-admin` 这种封装好的项目中，你可能会看到一种 **“万能写法”**。

Axios 允许你直接传一个大对象（配置对象 `config`），你想怎么发都行：

JavaScript

```
axios({
  method: 'post', // 这里可以换成 get, put, delete
  url: '/user/login',
  data: {         // 如果是 get 就要改成 params
    firstName: 'Fred',
    lastName: 'Flintstone'
  },
  timeout: 1000,  // 1秒超时
  headers: {      // 自定义请求头
    'Content-Type': 'application/json'
  }
});
```

**为什么这种写法重要？**

因为它最适合 **封装**。你可以写一个公共函数，把 method、url、data 当作变量传进去。

---

### 3. 我们收到了什么？（响应结构）

当你发出请求，Axios 会给你带回来一个 **响应对象 (Response Object)**。

这也是初学者容易晕的地方：**后端返回的数据，到底在哪里？**

假设后端给你回了这个 JSON：`{ "code": 200, "msg": "成功", "list": [...] }`

在 Axios 的 `then((res) => { ... })` 里，这个 `res` 包含了更多信息：

JavaScript

```
axios.get('/user').then(res => {
  // 1. res.data (最重要！)
  // 这里才是后端真正给你的东西：{ code: 200, msg: "成功", list: [...] }
  console.log(res.data); 

  // 2. res.status
  // HTTP 状态码，比如 200, 404, 500
  console.log(res.status);

  // 3. res.headers
  // 服务器回给你的头信息
  console.log(res.headers);
});
```

**新手误区提醒：**

很多新手会发现控制台打印出来是 `undefined`，因为他们直接用了 `res.list`。

**错！** 必须是 `res.data.list`。Axios 帮你包了一层外壳。

---

### 4. 第一层级小测验（验证你是否掌握）

假设你在 `geeker-admin` 里接到了一个任务：**“做一个API，把选中的商品ID发送给后端进行批量删除”。**

- **接口地址**：`/goods/batch-delete`
    
- **请求方式**：POST
    
- **需要参数**：一个数组 `ids: [1, 2, 3]`
    

请你尝试写出这个 Axios 请求代码（用 `axios.post` 的方式）。

（你可以试着写一下，或者在脑子里构思一下，然后看我下面的答案）。

<details>

<summary>👉 点击这里查看参考答案</summary>

JavaScript

```
// 注意：是 POST，所以参数放第二个位置（data）
axios.post('/goods/batch-delete', {
  ids: [1, 2, 3]
})
.then(res => {
  console.log('删除成功', res.data);
})
.catch(err => {
  console.log('删除失败', err);
});
```

**如果你刚才想的是 `params`，那就掉进陷阱啦！POST 请求要用 Body (data)。**

</details>

---

这第一层级的内容，你觉得清晰了吗？如果这一层没问题，我们就可以进入 **第二层级：Axios 实例与拦截器**，那是 `geeker-admin` 代码的核心所在。