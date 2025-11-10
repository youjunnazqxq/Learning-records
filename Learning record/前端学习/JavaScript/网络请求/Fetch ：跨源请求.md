
如果我们向另一个网站发送 `fetch` 请求，则该请求可能会失败。

例如，让我们尝试向 `http://example.com` 发送 `fetch` 请求

# 安全请求 

有两种类型的跨源请求：

1. 安全请求。
2. 所有其他请求
如果一个请求满足下面这两个条件，则该请求是安全的：

3. [安全的方法](https://fetch.spec.whatwg.org/#cors-safelisted-method)：GET，POST 或 HEAD
4. [安全的 header](https://fetch.spec.whatwg.org/#cors-safelisted-request-header) —— 仅允许自定义下列 header：
    - `Accept`，
    - `Accept-Language`，
    - `Content-Language`，
    - `Content-Type` 的值为 `application/x-www-form-urlencoded`，`multipart/form-data` 或 `text/plain`。


## 用于安全请求的CORS


如果一个请求是跨源的，浏览器始终会向其添加 `Origin` header。

例如，如果我们从 `https://javascript.info/page` 请求 `https://anywhere.com/request`，请求的 header 将如下所示


服务器可以检查 `Origin`，如果同意接受这样的请求，就会在响应中添加一个特殊的 header `Access-Control-Allow-Origin`。该 header 包含了允许的源（在我们的示例中是 `https://javascript.info`），或者一个星号 `*`。然后响应成功，否则报错。


```
GET /request
Host： anywhere.com
Origin: url
```

务器可以检查 `Origin`，如果同意接受这样的请求，就会在响应中添加一个特殊的 header `Access-Control-Allow-Origin`。该 header 包含了允许的源（在我们的示例中是 `https://javascript.info`），或者一个星号 `*`。然后响应成功，否则报错。


浏览器在这里扮演受被信任的中间人的角色：

1. 它确保发送的跨源请求带有正确的 `Origin`。
2. 它检查响应中的许可 `Access-Control-Allow-Origin`，如果存在，则允许 JavaScript 访问响应，否则将失败并报错。


# Response header

对于跨源请求，默认情况下，JavaScript 只能访问“安全的” response header：


# 非安全请求 

#### step 1 预检请求
- 方法：`OPTIONS`。
- 路径 —— 与主请求完全相同：`/service.json`。
- 特殊跨源头：
    - `Origin` —— 来源。
    - `Access-Control-Request-Method` —— 请求方法。
    - `Access-Control-Request-Headers` —— 以逗号分隔的“非安全” header 列表。

#### step2 预检响应
服务应响应状态 200 和 header：

- `Access-Control-Allow-Origin: [https://javascript.info](https://javascript.info/)`
- `Access-Control-Allow-Methods: PATCH`
- `Access-Control-Allow-Headers: Content-Type,API-Key`。

这将允许后续通信，否则会触发错误。

如果服务器将来需要其他方法和 header，则可以通过将这些方法和 header 添加到列表中来预先允许它们。

#### step3 实际请求

#### step4 实际响应




# 凭据

要在 `fetch` 中发送凭据，我们需要添加 `credentials: "include"` 选项，像这样：
```
fetch(url,{
	credentials: 'include'
});
```

