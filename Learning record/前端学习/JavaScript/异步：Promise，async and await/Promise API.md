# Promise.all
`Promise.all` 接受一个可迭代对象（通常是一个数组项为 promise 的数组），并返回一个新的 promise
当所有给定的 promise 都 resolve 时，新的 promise 才会 resolve，并且其结果数组将成为新 promise 的结果。
**如果任意一个 promise 被 reject，由 `Promise.all` 返回的 promise 就会立即 reject，并且带有的就是这个 error。**

## 注意
如果出现了error，其它promise会被忽略

# Promise.allSettled

`Promise.allSettled` 等待所有的 promise 都被 settle，无论结果如何。结果数组会是这样的：
- 对成功的响应，结果数组对应元素的内容为 `{status:"fulfilled", value:result}`，
-  对出现 error 的响应，结果数组对应元素的内容为 `{status:"rejected", reason:error}`。

# Promise.race
与 `Promise.all` 类似，但只等待第一个 settled 的 promise 并获取其结果（或 error）。


# Promise.any

与 `Promise.race` 类似，区别在于 `Promise.any` 只等待第一个 fulfilled 的 promise，并将这个 fulfilled 的 promise 返回。如果给出的 promise 都 rejected，那么返回的 promise 会带有 [`AggregateError`](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/AggregateError) —— 一个特殊的 error 对象，在其 `errors` 属性中存储着所有 promise error。



