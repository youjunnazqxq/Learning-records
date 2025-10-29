# Proxy
语法：
```
let proxy = new Proxy(target,handler);
```
- `target` —— 是要包装的对象，可以是任何东西，包括函数。
- `handler` —— 代理配置：带有“捕捉器”（“traps”，即拦截操作的方法）的对象。比如 `get` 捕捉器用于读取 `target` 的属性，`set` 捕捉器用于写入 `target` 的属性，等等。

内部的方法

| 内部方法 | Handler 方法 | 何时触发 |
| :--- | :--- | :--- |
| `[[Get]]` | `get` | 读取属性 |
| `[[Set]]` | `set` | 写入属性 |
| `[[HasProperty]]` | `has` | `in` 操作符 |
| `[[Delete]]` | `deleteProperty` | `delete` 操作符 |
| `[[Call]]` | `apply` | 函数调用 |
| `[[Construct]]` | `construct` | `new` 操作符 |
| `[[GetPrototypeOf]]` | `getPrototypeOf` | `Object.getPrototypeOf` |
| `[[SetPrototypeOf]]` | `setPrototypeOf` | `Object.setPrototypeOf` |
| `[[IsExtensible]]` | `isExtensible` | `Object.isExtensible` |
| `[[PreventExtensions]]` | `preventExtensions` | `Object.preventExtensions` |
| `[[DefineProperty]]` | `defineProperty` | `Object.defineProperty`, `Object.defineProperties` |
| `[[GetOwnProperty]]` | `getOwnPropertyDescriptor` | `Object.getOwnPropertyDescriptor`, `for..in`, `Object.keys/values/entries` |
| `[[OwnPropertyKeys]]` | `ownKeys` | `Object.getOwnPropertyNames`, `Object.getOwnPropertySymbols`, `for..in`, `Object.keys/values/entries` |


## 带有get捕捉器的默认值 

`handler` 应该有 `get(target, property, receiver)` 方法
- `target` —— 是目标对象，该对象被作为第一个参数传递给 `new Proxy`，
- `property` —— 目标属性名，
- `receiver` —— 如果目标属性是一个 getter 访问器属性，则 `receiver` 就是本次读取属性所在的 `this` 对象。

## 使用set捕捉器进行验证 

set(target, property, value, receiver)
- `target` —— 是目标对象，该对象被作为第一个参数传递给 `new Proxy`，
- `property` —— 目标属性名称，
- `value` —— 目标属性的值，
- `receiver` —— 与 `get` 捕捉器类似，仅与 setter 访问器属性相关。

如果写入操作（setting）成功，`set` 捕捉器应该返回 `true`，否则返回 `false`（触发 `TypeError`）。






