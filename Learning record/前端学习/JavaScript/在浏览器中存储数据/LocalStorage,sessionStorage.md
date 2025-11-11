
Web 存储对象 `localStorage` 和 `sessionStorage` 允许我们在浏览器上保存键/值对

我们已经有了 cookie。为什么还要其他存储对象呢？

- 与 cookie 不同，Web 存储对象不会随每个请求被发送到服务器。因此，我们可以保存更多数据。大多数现代浏览器都允许保存至少 5MB 的数据（或更多），并且具有用于配置数据的设置。
- 还有一点和 cookie 不同，服务器无法通过 HTTP header 操纵存储对象。一切都是在 JavaScript 中完成的。
- 存储绑定到源（域/协议/端口三者）。也就是说，不同协议或子域对应不同的存储对象，它们之间无法访问彼此数据。

# LocalStorage

`localStorage` 最主要的特点是：

- 在同源的所有标签页和窗口之间共享数据。
- 数据不会过期。它在浏览器重启甚至系统重启后仍然存在。

## 遍历键 

正如我们所看到的，这些方法提供了“按照键获取/设置/删除”的功能。但我们如何获取所有保存的值或键呢？

不幸的是，存储对象是不可迭代的。

一种方法是像遍历数组那样遍历它们：


另一个方式是使用 `for key in localStorage` 循环，就像处理常规对象一样。

它会遍历所有的键，但也会输出一些我们不需要的内建字段。
我们需要使用 `hasOwnProperty` 检查来过滤掉原型中的字段：

# 仅字符串 
请注意，键和值都必须是字符串。

如果是任何其他类型，例数字或对象，它会被自动转换为字符串。


# Storage事件 

当 `localStorage` 或 `sessionStorage` 中的数据更新后，[storage](https://html.spec.whatwg.org/multipage/webstorage.html#the-storageevent-interface) 事件就会触发，它具有以下属性：

- `key` —— 发生更改的数据的 `key`（如果调用的是 `.clear()` 方法，则为 `null`）。
- `oldValue` —— 旧值（如果是新增数据，则为 `null`）。
- `newValue` —— 新值（如果是删除数据，则为 `null`）。
- `url` —— 发生数据更新的文档的 url。
- `storageArea` —— 发生数据更新的 `localStorage` 或 `sessionStorage` 对象。