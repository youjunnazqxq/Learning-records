# 语法

```
let promise = new Promise(function(resolve,reject){
	//executor(生产者代码)
}）
```
new Promise(executor)：你（开发者）提供 `executor` 函数。
executor(resolve, reject)：`executor` 立即执行，它有两个“开关”：
成功时：你来决定何时调用 `resolve(value)`，把结果 `value` 传出去。
失败时：你来决定何时调用 `reject(error)`，把错误 `error` 传出去。


## promise内部属性 

- `state` —— 最初是 `"pending"`(未发生)，然后在 `resolve` 被调用时变为 `"fulfilled"`，或者在 `reject` 被调用时变为 `"rejected"`。
- `result` —— 最初是 `undefined`，然后在 `resolve(value)` 被调用时变为 `value`，或者在 `reject(error)` 被调用时变为 `error`。

![[Pasted image 20251025154040.png]]


# 消费者 then catch

# then

语法：
```
promise.then(
	function(result){handle successfule result};
	function(error){handle an error};
)
```
`.then` 的第一个参数是一个函数，该函数将在 promise resolved 且接收到结果后执行。

`.then` 的第二个参数也是一个函数，该函数将在 promise rejected 且接收到 error 信息后执行。


## catch
如果我们只对 error 感兴趣，那么我们可以使用 `null` 作为第一个参数：`.then(null, errorHandlingFunction)`。或者我们也可以使用 `.catch(errorHandlingFunction)`，其实是一样的：

## 清理 finally

finally的意思是程序执行完就开始运行。`finally` 的功能是设置一个处理程序在前面的操作完成后，执行清理/终结

- `finally` 处理程序（handler）没有参数。在 `finally` 中，我们不知道 promise 是否成功。没关系，因为我们的任务通常是执行“常规”的完成程序（finalizing procedures）。（不消耗结果，与之相反的是then会消耗error和result）

- `finally` 处理程序将结果或 error “传递”给下一个合适的处理程序。

-  `finally` 处理程序也不应该返回任何内容。如果它返回了，返回的值会默认被忽略。
此规则的唯一例外是当 `finally` 处理程序抛出 error 时。此时这个 error（而不是任何之前的结果）会被转到下一个处理程序。


