
# 加载脚本

### script.onload

我们的得力助手是 `load` 事件。它会在脚本加载并执行完成时触发

```
let script = document.createElement('script');
// 可以从任意域（domain），加载任意脚本
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.3.0/lodash.js';
document.head.append(script);

script.onload = function() {
  // 该脚本创建了一个变量 "_"
  alert( _.VERSION ); // 显示库的版本
};

```

### script.onerror

发生在脚本加载期间的 error 会被 `error` 事件跟踪到

#### onload/onerror 事件仅跟踪加载本身 

在脚本处理和执行期间可能发生的 error 超出了这些事件跟踪的范围。也就是说：如果脚本成功加载，则即使脚本中有编程 error，也会触发 `onload` 事件。如果要跟踪脚本 error，可以使用 `window.onerror` 全局处理程序


# 其它资源 
`load` 和 `error` 事件也适用于其他资源，基本上（basically）适用于具有外部 `src` 的任何资源


# 跨源策略

这里有一条规则：来自一个网站的脚本无法访问其他网站的内容。例如，位于 `[https://facebook.com](https://facebook.com/)` 的脚本无法读取位于 `[https://gmail.com](https://gmail.com/)` 的用户邮箱。

或者，更确切地说，一个源（域/端口/协议三者）无法获取另一个源（origin）的内容。因此，即使我们有一个子域，或者仅仅是另一个端口，这都是不同的源，彼此无法相互访问。

这个规则还影响其他域的资源。
如果我们使用的是来自其他域的脚本，并且该脚本中存在 error，那么我们无法获取 error 的详细信息。


**要允许跨源访问，`<script>` 标签需要具有 `crossorigin` 特性（attribute），并且远程服务器必须提供特殊的 header。**



