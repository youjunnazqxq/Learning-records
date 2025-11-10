# 基本语法

`let promise = fetch(url,[options])`
- **`url`** —— 要访问的 URL。
- **`options`** —— 可选参数：method，header 等

浏览器立即启动请求，并返回一个该调用代码应该用来获取结果的 `promise`。

获取响应通常需要经过两个阶段。

**第一阶段，当服务器发送了响应头（response header），`fetch` 返回的 `promise` 就使用内建的 [Response](https://fetch.spec.whatwg.org/#response-class) class 对象来对响应头进行解析。**
如果 `fetch` 无法建立一个 HTTP 请求，例如网络问题，亦或是请求的网址不存在，那么 promise 就会 reject。异常的 HTTP 状态，例如 404 或 500，不会导致出现 error。

我们可以在 response 的属性中看到 HTTP 状态：

- **`status`** —— HTTP 状态码，例如 200。
- **`ok`** —— 布尔值，如果 HTTP 状态码为 200-299，则为 `true`。

**第二阶段，为了获取 response body，我们需要使用一个其他的方法调用。**

`Response` 提供了多种基于 promise 的方法，来以不同的格式访问 body：

- **`response.text()`** —— 读取 response，并以文本形式返回 response，
- **`response.json()`** —— 将 response 解析为 JSON 格式，
- **`response.formData()`** —— 以 `FormData` 对象（在 [下一章](https://zh.javascript.info/formdata) 有解释）的形式返回 response，
- **`response.blob()`** —— 以 [Blob](https://zh.javascript.info/blob)（具有类型的二进制数据）形式返回 response，
- **`response.arrayBuffer()`** —— 以 [ArrayBuffer](https://zh.javascript.info/arraybuffer-binary-arrays)（低级别的二进制数据）形式返回 response，
- 另外，`response.body` 是 [ReadableStream](https://streams.spec.whatwg.org/#rs-class) 对象，它允许你逐块读取 body，我们稍后会用一个例子解释它

# Response header 

Response header 位于 `response.headers` 中的一个类似于 Map 的 header 对象。

它不是真正的 Map，但是它具有类似的方法，我们可以按名称（name）获取各个 header


# Request header 


要在 `fetch` 中设置 request header，我们可以使用 `headers` 选项。它有一个带有输出 header 的对象，
常见请求头的内容：
1. 描述请求内容 (您发了什么？

### 1. 描述请求内容 (您发了什么？)

这类头部在您使用 `POST` 或 `PUT`（即有 `body`）时**至关重要**。

|**常见头部**|**作用 (告诉服务器...)**|**如何理解 (大白话)**|
|---|---|---|
|**`Content-Type`**|“我 `body` 里发给你的数据是**什么格式**的。”|“包裹里装的是 **JSON**。” (或“...是**表单**。”)<br><br>  <br><br>**这是您在 `POST` 请求中几乎总要手动设置的。**|
|`Content-Length`|“我 `body` 里的数据**有多长**（多少字节）。”|“这个包裹重 128 克。”<br><br>  <br><br>(通常 `fetch` 或浏览器会自动帮您计算并添加。)|

---

### 2. 描述客户端期望 (您想要什么？)

这类头部告诉服务器您希望**收到**什么样的数据。

|**常见头部**|**作用 (告诉服务器...)**|**如何理解 (大白话)**|
|---|---|---|
|**`Accept`**|“我**希望**你返回给我**什么格式**的数据。”|“请回信给我 **JSON** 格式的。”（服务器不一定会听，但会尽量满足）|
|`Accept-Language`|“我**希望**的语言是...。”|“请优先用**中文**（`zh-CN`）或**英文**（`en`）回复我。”（用于国际化网站）|
|`Accept-Encoding`|“我能理解这些**压缩格式**。”|“你可以把回复用 `gzip` 压缩一下再发给我，我解得开，这样快一点。”|

**重要区别：**

- **`Content-Type`**：描述您**发送**的 `body`。（您是“说”JSON）
    
- **`Accept`**：描述您**期望**的 `response`。（您想“听”JSON）
    

---

### 3. 身份与权限 (您是谁？)

这类头部用于身份验证和会话管理。

|**常见头部**|**作用 (告诉服务器...)**|**如何理解 (大白话)**|
|---|---|---|
|**`Authorization`**|“这是我的**身份凭证**。”|“这是我的**API 密钥** / **令牌 (Token)**。”<br><br>  <br><br>(例如 `Bearer ey...`，这是您在 `fetch` 中经常要手动设置的。)|
|`Cookie`|“这是你上次给我的**“小纸条”**。”|“这是我的登录状态 / 会话 ID。” (浏览器通常会自动携带，用于保持登录。)|

---

### 4. 描述客户端自身 (您从哪来？)

|**常见头部**|**作用 (告诉服务器...)**|**如何理解 (大白话)**|
|---|---|---|
|**`User-Agent`**|“我是**什么浏览器** / **什么工具**。”|“我来自 **Chrome 浏览器** (Windows 10)。”（服务器可能用它来返回特定兼容内容）|
|`Referer`|“我是从**哪个页面**点过来的。”|“我是从 `google.com` 的搜索结果点过来的。”（用于分析流量来源）|

### 5. 控制与路由 (您想让服务器怎么做？)

这类头部用于控制请求的流转和缓存。

|**常见头部**|**作用 (告诉服务器...)**|**如何理解 (大白话)**|
|---|---|---|
|**`Host`**|“我想访问你这台服务器上的**哪个网站**。”|“我要访问 `api.example.com`。”（一个 IP 地址上可能有很多网站，`Host` 用来区分。浏览器 100% 自动添加。）|
|`Cache-Control`|“我关于**缓存**的策略是...”|“我不要旧的缓存，请给我最新的（`no-cache`）。”（用于强制刷新）|


# POST 请求 
要创建一个 `POST` 请求，或者其他方法的请求，我们需要使用 `fetch` 选项

- **`method`** —— HTTP 方法，例如 `POST`，
- **`body`** —— request body，其中之一：
    - 字符串（例如 JSON 编码的），
    - `FormData` 对象，以 `multipart/form-data` 形式发送数据，
    - `Blob`/`BufferSource` 发送二进制数据，
    - [URLSearchParams](https://zh.javascript.info/url)，以 `x-www-form-urlencoded` 编码形式发送数据，很少使用。

```
let user = {
};
let response = await fetch(url,{
	method: 'POST',
	headers:{
		'Content-Type': 'application/json;charset=utf-8'
	},
	body:JSON.stringify(user);

});
```


