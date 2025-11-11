基本语法：
`let socker = new WebSocket("ws://javascript.info");`

始终使用 `wss://`

`wss://` 协议不仅是被加密的，而且更可靠。

因为 `ws://` 数据不是加密的，对于任何中间人来说其数据都是可见的。并且，旧的代理服务器不了解 WebSocket，它们可能会因为看到“奇怪的” header 而中止连接。

另一方面，`wss://` 是基于 TLS 的 WebSocket，类似于 HTTPS 是基于 TLS 的 HTTP），传输安全层在发送方对数据进行了加密，在接收方进行解密。因此，数据包是通过代理加密传输的。它们看不到传输的里面的内容，且会让这些数据通过。


一旦 socket 被建立，我们就应该监听 socket 上的事件。一共有 4 个事件：

- **`open`** —— 连接已建立，
- **`message`** —— 接收到数据，
- **`error`** —— WebSocket 错误，
- **`close`** —— 连接已关闭。



```
let socket = new WebSocket("wss://javascript.info/article/websocket/demo/hello");

socket.onopen = function(e) {
  alert("[open] Connection established");
  alert("Sending to server");
  socket.send("My name is John");
};

socket.onmessage = function(event) {
  alert(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // 例如服务器进程被杀死或网络中断
    // 在这种情况下，event.code 通常为 1006
    alert('[close] Connection died');
  }
};

socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};
```


# 建立WebSocket
当 `new WebSocket(url)` 被创建后，它将立即开始连接。

在连接期间，浏览器（使用 header）问服务器：“你支持 WebSocket 吗？”如果服务器回复说“我支持”，那么通信就以 WebSocket 协议继续进行，该协议根本不是 HTTP。

![[Pasted image 20251110211936.png]]

如果服务器同意切换为 WebSocket 协议，服务器应该返回响应码 101：

#### 扩展和子协议

WebSocket 可能还有其他 header，`Sec-WebSocket-Extensions` 和 `Sec-WebSocket-Protocol`，它们描述了扩展和子协议。

- `Sec-WebSocket-Extensions: deflate-frame` 表示浏览器支持数据压缩。扩展与传输数据有关，扩展了 WebSocket 协议的功能。`Sec-WebSocket-Extensions` header 由浏览器自动发送，其中包含其支持的所有扩展的列表。
    
- `Sec-WebSocket-Protocol: soap, wamp` 表示我们不仅要传输任何数据，还要传输 [SOAP](https://en.wikipedia.org/wiki/SOAP) 或 WAMP（“The WebSocket Application Messaging Protocol”）协议中的数据。WebSocket 子协议已经在 [IANA catalogue](https://www.iana.org/assignments/websocket/websocket.xml) 中注册。因此，此 header 描述了我们将要使用的数据格式。
    
    这个可选的 header 是使用 `new WebSocket` 的第二个参数设置的。它是子协议数组，例如，如果我们想使用 SOAP 或 WAMP


# 数据传输
WebSocket 通信由 “frames”（即数据片段）组成，可以从任何一方发送，并且有以下几种类型：

- “text frames” —— 包含各方发送给彼此的文本数据。
- “binary data frames” —— 包含各方发送给彼此的二进制数据。
- “ping/pong frames” 被用于检查从服务器发送的连接，浏览器会自动响应它们。
- 还有 “connection close frame” 以及其他服务 frames。

在浏览器里，我们仅直接使用文本或二进制 frames


**WebSocket `.send()` 方法可以发送文本或二进制数据。**

`socket.send(body)` 调用允许 `body` 是字符串或二进制格式，包括 `Blob`，`ArrayBuffer` 等。不需要额外的设置：直接发送它们就可以了。

**当我们收到数据时，文本总是以字符串形式呈现。而对于二进制数据，我们可以在 `Blob` 和 `ArrayBuffer` 格式之间进行选择。**

# 限速
`socket.bufferedAmount` 属性储存了目前已缓冲的字节数，等待通过网络发送。

我们可以检查它以查看 socket 是否真的可用于传输。


# 连接关闭 

通常，当一方想要关闭连接时（浏览器和服务器都具有相同的权限），它们会发送一个带有数字码（numeric code）和文本形式的原因的 “connection close frame”。

`socker.close([code],[reason])`

- `code` 是一个特殊的 WebSocket 关闭码（可选）
- `reason` 是一个描述关闭原因的字符串（可选）

最常见的数字码：

- `1000` —— 默认，正常关闭（如果没有指明 `code` 时使用它），
- `1006` —— 没有办法手动设定这个数字码，表示连接丢失（没有 close frame


# 连接状态 
要获取连接状态，可以通过带有值的 `socket.readyState` 属性：

- **`0`** —— “CONNECTING”：连接还未建立，
- **`1`** —— “OPEN”：通信中，
- **`2`** —— “CLOSING”：连接关闭中，
- **`3`** —— “CLOSED”：连接已关闭。


