在 JavaScript 中，`new` 操作符用于创建一个给定构造函数的实例对象。它的核心作用是将一个普通的函数转变为一个“对象工厂”，并自动帮你处理好原型的链接和 `this` 的指向。

当你在代码中执行 `new Constructor()` 时，JavaScript 引擎在底层其实默默执行了 **4 个关键步骤**：

### 1. 创建新对象

在内存中创建一个全新的、空的 JavaScript 对象。

- _可以理解为：_ `const obj = {};`
    

### 2. 链接原型（建立继承关系）

将这个全新对象的隐式原型（`__proto__`）指向构造函数的显式原型（`prototype`）。这是 JavaScript 实现原型链继承的最关键一步，让新对象能够访问构造函数原型上的方法。

- _可以理解为：_ `obj.__proto__ = Constructor.prototype;` （在现代 JS 中，推荐的底层等价操作是 `Object.setPrototypeOf(obj, Constructor.prototype)`）
    

### 3. 绑定 this 并执行构造函数

将构造函数内部的 `this` 上下文绑定到这个新创建的对象上，并执行构造函数内部的代码。这样，构造函数里写的 `this.name = ...` 就会把属性添加到这个新对象上。

- _可以理解为：_ `const result = Constructor.apply(obj, args);`
    

### 4. 决定返回值

这是很多开发者容易忽略的细节。`new` 表达式最终返回什么，取决于构造函数自身的返回值：

- 如果构造函数**没有返回值**，或者返回的是一个**基本数据类型**（如 `123`, `"hello"`, `true`），那么 `new` 会忽略它，强制返回第一步创建的**新对象 `obj`**。
    
- 如果构造函数显式返回了一个**引用数据类型**（即另一个对象、数组或函数），那么 `new` 就会放弃第一步创建的新对象，转而返回这个**自定义的对象**。
    

---

### 💻 核心面试考点：手写模拟 `new`

为了彻底搞懂它，我们可以用纯 JavaScript 模拟实现一个 `new` 操作符的功能。这在前端面试中也是极其高频的手写代码题：

JavaScript

```
function myNew(Constructor, ...args) {
  // 1. 创建一个新对象
  const obj = {};
  
  // 2. 将新对象的隐式原型链接到构造函数的显式原型上
  Object.setPrototypeOf(obj, Constructor.prototype);
  // (老写法：obj.__proto__ = Constructor.prototype;)
  
  // 3. 将 this 绑定到新对象上，并执行构造函数
  const result = Constructor.apply(obj, args);
  
  // 4. 判断构造函数的返回值类型，决定最终返回什么
  // 如果 result 是对象且不为 null，或者 result 是函数，则返回 result；否则返回 obj
  if ((typeof result === 'object' && result !== null) || typeof result === 'function') {
    return result;
  }
  
  return obj;
}

// === 测试一下 ===
function Person(name, age) {
  this.name = name;
  this.age = age;
}
Person.prototype.sayHi = function() {
  console.log(`大家好，我是 ${this.name}`);
};

// 使用原生的 new
const p1 = new Person('张三', 25);
p1.sayHi(); // 输出：大家好，我是 张三

// 使用我们手写的 myNew
const p2 = myNew(Person, '李四', 30);
p2.sayHi(); // 输出：大家好，我是 李四
```