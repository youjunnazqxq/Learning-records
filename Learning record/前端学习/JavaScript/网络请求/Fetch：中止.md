
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