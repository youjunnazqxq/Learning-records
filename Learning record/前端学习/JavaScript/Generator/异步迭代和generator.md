1. 使用 `Symbol.asyncIterator` 取代 `Symbol.iterator`。
2. `next()` 方法应该返回一个 `promise`（带有下一个值，并且状态为 `fulfilled`）。
    - 关键字 `async` 可以实现这一点，我们可以简单地使用 `async next()`。
3. 我们应该使用 `for await (let item of iterable)` 循环来迭代这样的对象。
    - 注意关键字 `await`。

# 异步 generator

在 `function*` 前面加上 `async`。这即可使 generator 变为异步的。

然后使用 `for await (...)` 来遍历它

这样产生的迭代器是有区别的，例如：对于异步 generator，`generator.next()` 方法是异步的，它返回 promise。在一个常规的 generator 中，我们使用 `result = generator.next()` 来获得值。但在一个异步 generator 中，我们应该添加 `await` 关键字
```
result = await generator.next();
```



