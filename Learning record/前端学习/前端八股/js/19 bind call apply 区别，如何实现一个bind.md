`call`、`apply` 和 `bind` 是 JavaScript 中用于显式改变函数执行上下文（即 `this` 指向）的三个核心方法。它们都挂载在 `Function.prototype` 上。

### 核心区别对比

掌握它们的区别，只需记住“执行时机”**和**“传参方式”两个维度：

|**方法**|**执行时机**|**参数传递方式**|**返回值**|**适用场景**|
|---|---|---|---|---|
|**`call`**|**立即执行**|逗号分隔 (`arg1, arg2...`)|原函数的执行结果|明确知道参数个数，需要立即执行时。|
|**`apply`**|**立即执行**|**数组** (`[arg1, arg2...]`)|原函数的执行结果|参数已经是一个数组，或处理 `arguments` 时。|
|**`bind`**|**延迟执行**|逗号分隔 (`arg1, arg2...`)|**一个全新的函数**|绑定事件回调、设置定时器、函数柯里化（分批传参）时。|

---

### 核心特性总结

1. **改变 `this` 指向**：三者的第一个参数都是要绑定的 `this` 对象。如果传入 `null` 或 `undefined`，在非严格模式下 `this` 会指向全局对象（浏览器中是 `window`）。
    
2. **`bind` 的柯里化特性**：`bind` 不仅能绑定 `this`，还能预置参数。你可以先传一部分参数，等调用新函数时再传剩余参数。
    
3. **`bind` 与 `new` 的优先级**：当使用 `bind` 绑定后的函数被 `new` 操作符作为构造函数调用时，`bind` 绑定的 `this` 会失效，`this` 会指向 `new` 出来的全新实例对象。
    

---

### 手写终极版 `bind` 源码

这是一个综合了**改变指向**、**参数拼接（柯里化）**、**处理 `new` 关键字**以及**安全继承原型**的完整实现版本：

JavaScript

```
Function.prototype.myBind = function(context, ...bindArgs) {
  // 1. 防御性编程：确保调用 myBind 的必须是一个函数
  if (typeof this !== 'function') {
    throw new TypeError('调用 myBind 的必须是一个函数');
  }

  // 2. 缓存原函数（也就是调用 myBind 的那个函数）
  const self = this; 
  
  // 3. 声明要返回的全新函数
  const boundFn = function(...callArgs) {
    // 4. 核心逻辑：判断是否被 new 操作符调用
    // 如果 this 是 boundFn 的实例，说明是 new 调用，忽略传入的 context，使用当前的 this（新实例）
    // 否则是普通调用，使用传入的 context
    const finalContext = this instanceof boundFn ? this : context;
    
    // 5. 将两次传入的参数合并，通过 apply 交给原函数执行
    return self.apply(finalContext, [...bindArgs, ...callArgs]);
  };

  // 6. 维护原型链：实现安全的继承，同时防止原型污染
  if (this.prototype) {
    // 使用 Object.create 创建一个干净的中转对象，指向原函数的原型
    boundFn.prototype = Object.create(this.prototype);
  }

  // 7. 返回这个包装好的新函数
  return boundFn;
};
```