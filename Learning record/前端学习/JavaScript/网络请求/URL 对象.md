# 创建语法

` new URL(url,[base])`
- **`url`** —— 完整的 URL，或者仅路径（如果设置了 base），
- **`base`** —— 可选的 base URL：如果设置了此参数，且参数 `url` 只有路径，则会根据这个 `base` 生成 URL。


#### URL组件的备忘录 

![[Pasted image 20251110192603.png]]

**`search` (查询参数)**

- **示例:** `?p1=v1&p2=v2...`
    
- **作用:** 用于向服务器传递额外的数据。它总是以一个 `?` 开始，由**键值对** (`key=value`) 组成，多个键值对之间用 `&` 分隔。
    
- **常见用途:** 搜索查询 (`?q=keyword`)、分页 (`?page=2`)、筛选条件等。

**`hash` (哈希/锚点)**

- **示例:** `#hash`
    
- **作用:** 指向页面中的特定部分（一个“锚点”）。它总是以 `_#_` 开始。
    
- **关键特性:** `hash` 及其之后的部分**仅在客户端（浏览器）上处理，永远不会发送到服务器**。
    
- **常见用途:**
    
    - 页面内跳转（例如，点击“返回顶部”）。
        
    - 单页面应用 (SPA) 中用来模拟页面跳转（“hash 路由”）。


## SearchParams
假设，我们想要创建一个具有给定搜索参数的 url，例如：`https://google.com/search?query=JavaScript`。

- **`append(name, value)`** —— 按照 `name` 添加参数，
- **`delete(name)`** —— 按照 `name` 移除参数，
- **`get(name)`** —— 按照 `name` 获取参数，
- **`getAll(name)`** —— 获取相同 `name` 的所有参数（这是可行的，例如 `?user=John&user=Pete`），
- **`has(name)`** —— 按照 `name` 检查参数是否存在，
- **`set(name, value)`** —— set/replace 参数，
- **`sort()`** —— 按 name 对参数进行排序，很少使用，
- ……并且它是可迭代的，类似于 `Map`

```
let url = new URL('https://google.com/search');

url.searchParams.set('q', 'test me!'); // 添加带有一个空格和一个 ！ 的参数

alert(url); // https://google.com/search?q=test+me%21

url.searchParams.set('tbs', 'qdr:y'); // 添加带有一个冒号 ： 的参数

// 参数会被自动编码
alert(url); // https://google.com/search?q=test+me%21&tbs=qdr%3Ay

// 遍历搜索参数（被解码）
for(let [name, value] of url.searchParams) {
  alert(`${name}=${value}`); // q=test me!，然后是 tbs=qdr:y
}
```



# 编码 （encoding）

[RFC3986](https://tools.ietf.org/html/rfc3986) 标准定义了 URL 中允许哪些字符，不允许哪些字符。

那些不被允许的字符必须被编码，例如非拉丁字母和空格 —— 用其 UTF-8 代码代替，前缀为 `%`，例如 `%20`（由于历史原因，空格可以用 `+` 编码，但这是一个例外）。



# 编码字符串 

在过去，在出现 `URL` 对象之前，人们使用字符串作为 URL。

而现在，`URL` 对象通常更方便，但是仍然可以使用字符串。在很多情况下，使用字符串可以使代码更短。

如果使用字符串，则需要手动编码/解码特殊字符。

下面是用于编码/解码 URL 的内建函数：

- [encodeURI](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) —— 编码整个 URL。
- [decodeURI](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) —— 解码为编码前的状态。
- [encodeURIComponent](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) —— 编码 URL 组件，例如搜索参数，或者 hash，或者 pathname。
- [decodeURIComponent](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) —— 解码为编码前的状态。

所以，对于一个 URL 整体，我们可以使用 `encodeURI`：
而对于 URL 参数，我们应该改用 `encodeURIComponent`：