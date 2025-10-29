
# Reference type 解读 

仔细看的话，我们可能注意到 `obj.method()` 语句中的两个操作：

1. 首先，点 `'.'` 取了属性 `obj.method` 的值。
2. 接着 `()` 执行了它

**为确保 `user.hi()` 调用正常运行，JavaScript 玩了个小把戏 —— 点 `'.'` 返回的不是一个函数，而是一个特殊的 [Reference Type](https://tc39.github.io/ecma262/#sec-reference-specification-type) 的值。** 


Reference Type 的值是一个三个值的组合 `(base, name, strict)`，其中：

- `base` 是对象。
- `name` 是属性名。
- `strict` 在 `use strict` 模式下为 true。

Reference Type 是 JavaScript 内部的一种“中间类型”，其核心作用是在属性访问（如  obj.method ）到函数调用（ () ）的过程中，携带足够的信息（对象  base 、属性名  name 、严格模式标记  strict ），从而确保函数调用时能正确设置  this
