

## 1. Axios 请求的通用公式

无论你发送什么请求，Axios 的核心逻辑都可以概括为：

axios(URL, [Config]) 或者 axios.[method](URL, [Data/Params], [Config])。

### URL 的角色

- **含义**：网络资源的地址（门牌号）。
    
- **组成**：通常由 `baseURL`（服务器根地址）+ `path`（具体接口路径）组成。
    
- **示例**：`https://api.com/v1/user`。
    

---

## 2. 不同请求方式的配置详解

这是最容易记混的部分，请重点看 **`params`** 和 **`data`** 的区别：

### ① GET 请求（查）

用于从服务器获取数据。参数显示在 URL 后面。

JavaScript

```
axios.get('/api/users', {
  // params 会被拼成 /api/users?role=admin&page=1
  params: {
    role: 'admin',
    page: 1
  },
  timeout: 5000 // 配置：5秒超时
});
```

### ② POST / PUT / PATCH 请求（增/改）

用于向服务器发送数据。数据放在请求体（Body）里，不在 URL 显示。

JavaScript

```
// 注意：第二个参数直接就是 data，第三个才是 config
axios.post('/api/users', 
  { name: 'Hermit', age: 18 }, // data：发送给后端的内容
  { headers: { 'Content-Type': 'application/json' } } // config：额外配置
);
```

### ③ DELETE 请求（删）

用于删除资源。参数通常直接在 URL 路径里，或者通过 `params` 传递。

JavaScript

```
axios.delete('/api/users/123'); // 删除 ID 为 123 的用户
```

---

## 3. 配置对象（Config）核心参数一览表

配置对象就像是你给 Axios 下达的“执行指令集”：

|**配置项**|**存放位置**|**作用**|**适用场景**|
|---|---|---|---|
|**`url`**|字符串|请求的路径地址|所有请求|
|**`method`**|字符串|请求动词（get, post 等）|统一配置写法时必填|
|**`baseURL`**|字符串|自动加在 url 前面的前缀|区分开发/生产环境|
|**`params`**|对象|拼接到 URL 上的参数|**GET** 请求传参|
|**`data`**|对象/字符串|放在请求体里的数据|**POST/PUT/PATCH** 传参|
|**`headers`**|对象|设置请求头（如 Token）|身份验证、格式声明|
|**`timeout`**|数值|设置请求超时限制（毫秒）|防止请求无限期挂起|

---

## 4. 为什么我们要区分这些？

- **URL vs Params**：为了让地址清晰。`params` 帮你自动处理了 URL 编码（比如空格变 `%20`），不需要你自己手动拼字符串。
    
- **Data vs Params**：为了安全和容量。`data` 可以发送巨大的 JSON 或文件，且不会出现在浏览器的历史记录（地址栏）里。
    
- **Method 的语义化**：为了让后端和同事一眼看出你在干什么（是想拿数据、还是想改数据）。
    

---

## 5. 总结图示

Plaintext

```
请求方式 | 参数字段 | 参数去向       | 形象比喻
----------------------------------------------------------
GET      | params   | URL 问号后面  | 写在信封封面的备注
POST     | data     | 请求体 (Body) | 装在信封里面的信件
PUT      | data     | 请求体 (Body) | 整箱替换掉旧包裹
PATCH    | data     | 请求体 (Body) | 给旧包裹打个小补丁
```

**基础知识我们已经全部打通了！** 接下来，你准备好进入实战阶段，看看如何把这些配置封装进一个 `request.js` 文件，实现**一处配置、全项目通用**的“解耦”架构吗？


## 6.配置头



## 1. 为什么叫“头” (Headers)？

在一个完整的 HTTP 请求中，数据被分为两部分：

1. **Header (头)**：相当于信封。上面写着地址、收件人、寄件人身份、信件格式等。服务器先读“头”，决定是否接收这封信。
    
2. **Body (体)**：相当于信件内容。就是你用 POST 发送的那些真正的数据。
    

---

## 2. 在 Axios 中最常配置的“头”

虽然 HTTP 协议规定了很多头信息，但在前端开发中，我们 90% 的时间只需要关注以下几个：

### ① `Authorization` (授权信息)

这是最重要的头。

- **作用**：携带 Token，证明你有权限访问接口。
    
- **格式**：通常以 `Bearer` 开头。
    
- **示例**：`Authorization: Bearer eyJhbG...`
    

### ② `Content-Type` (内容类型)

告诉服务器，我发给你的数据是什么格式的。

- **`application/json`**：最常用，告诉后端我发的是一个 JSON 对象。
    
- **`application/x-www-form-urlencoded`**：普通的表单格式。
    
- **`multipart/form-data`**：用于上传文件。
    

### ③ `Accept` (接收类型)

告诉服务器，我希望你返回给我什么格式的数据。

- **示例**：`Accept: application/json`（我只要 JSON）。
    

### ④ 自定义头 (Custom Headers)

根据后端的要求，有时需要传一些特殊字段。

- **示例**：`X-Requested-With: XMLHttpRequest` 或 `App-Version: 1.2.0`。