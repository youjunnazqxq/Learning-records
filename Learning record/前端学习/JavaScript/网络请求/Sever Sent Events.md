[Server-Sent Events](https://html.spec.whatwg.org/multipage/comms.html#the-eventsource-interface) 规范描述了一个内建的类 `EventSource`，它能保持与服务器的连接，并允许从中接收事件。

与 `WebSocket` 类似，其连接是持久的

| `WebSocket`      | `EventSource` |
| ---------------- | ------------- |
| 双向：客户端和服务端都能交换消息 | 单向：仅服务端能发送消息  |
| 二进制和文本数据         | 仅文本数据         |
| WebSocket 协议     | 常规 HTTP 协议    |

# 获取消息 



要开始接收消息，我们只需要创建 `new EventSource(url)` 即可。

浏览器将会连接到 `url` 并保持连接打开，等待事件。

服务器响应状态码应该为 200，header 为 `Content-Type: text/event-stream`，然后保持此连接并以一种特殊的格式写入消息，
- `data:` 后为消息文本，冒号后面的空格是可选的。
- 消息以双换行符 `\n\n` 分隔。
- 要发送一个换行 `\n`，我们可以在要换行的位置立即再发送一个 `data:`（上面的第三条消息）。


#### 跨源请求 

#### 重新连接 

创建之后，`new EventSource` 连接到服务器，如果连接断开 —— 则重新连接。

这非常方便，我们不用去关心重新连接的事情。

每次重新连接之间有一点小的延迟，默认为几秒钟。

服务器可以使用 `retry:` 来设置需要的延迟响应时间（以毫秒为单位）。[]()
