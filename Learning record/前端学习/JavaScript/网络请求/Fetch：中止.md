
# AbortController 对象

##### 语法：
`let controller = new AbortController();`


控制器是一个极其简单的对象。

- 它具有单个方法 `abort()`，
- 和单个属性 `signal`，我们可以在这个属性上设置事件监听器。

当 `abort()` 被调用时：

- `controller.signal` 就会触发 `abort` 事件。
- `controller.signal.aborted` 属性变为 `true`。

通常，我们需要处理两部分：

1. 一部分是通过在 `controller.signal` 上添加一个监听器，来执行可取消操作。
2. 另一部分是触发取消：在需要的时候调用 `controller.abort()`。

# 与fetch一起使用 

为了能够取消 `fetch`，请将 `AbortController` 的 `signal` 属性作为 `fetch` 的一个可选参数（option）进行传递


```
let controller = new AbortCOntroller();
fetch(url,{
	signal: controller.signal;
})
```

现在，想要中止 `fetch`，调用 `controller.abort()` 即可

当一个 fetch 被中止，它的 promise 就会以一个 error `AbortError` reject，因此我们应该对其进行处理，例如在 `try..catch` 中

# AbortController 是可伸缩的

`AbortController` 是可伸缩的。它允许一次取消多个 fetch



# 示例：
```
// 1. 创建“终止器”
const controller = new AbortController();

// 2. 从“终止器”中获取“信号”
const signal = controller.signal;

// 3. 将“信号”作为配置的一部分传递给 fetch
fetch('https://api.example.com/data', {
  method: 'GET',
  
  // 把它放在这里，与 method, headers 等同级
  signal: signal 
  
  // (ES6 简写: signal)
  
}).catch(err => {
  if (err.name === 'AbortError') {
    console.log('Fetch 请求已被中止！');
  } else {
    console.error('Fetch 错误:', err);
  }
});

// 4. 在未来的某个时刻（比如 1 秒后）按下“停止按钮”
setTimeout(() => {
  controller.abort();
}, 1000); // 1秒后中止请求
```