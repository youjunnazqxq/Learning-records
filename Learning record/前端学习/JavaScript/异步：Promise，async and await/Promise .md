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

# 内部解析

当进行`let promise = new Promise((resolve,reject) => {})`的时候，这个对象是立即返回的，但是其内部的数据来说并不是这样的：
### 抽屉 1：状态记录仪 (`[[PromiseState]]`)

这是最重要的数据，用来标记当前任务进行到哪一步了。 它只有三种可能的值：

- **`"pending"`** (等待中)：刚 `new` 出来的时候，默认就是这个。
    
- **`"fulfilled"`** (已成功)：调用 `resolve()` 后变成这个。
    
- **`"rejected"`** (已失败)：调用 `reject()` 或报错后变成这个。
    

### 抽屉 2：结果暂存区 (`[[PromiseResult]]`)

这里存放的是任务的结果数据。

- **刚创建时**：这里是 `undefined`（空的）。
    
- **成功后**：这里存的是你传给 `resolve(数据)` 的那个**数据**。
    
- **失败后**：这里存的是你传给 `reject(错误)` 的那个**错误对象**。
    

### 抽屉 3：排队的小本本 (`[[PromiseFulfillReactions]]` 等)

这是一个**列表（队列）**。

- 当你调用 `.then(fn)` 时，JS 并不是马上执行 `fn`，而是把 `fn` 这个函数**记在这个小本本上**。
    
- Promise 对象一直拿着这个小本本，一旦状态变成“成功”，它就会把本子上的函数一个个拿出来去微任务队列里执行。
这是异步等待填充的，这其中resolve和error更像是一个动作，通知数据变化的一个动作；
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


