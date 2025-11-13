111111# Proxy

本质：一个包装器
语法：
```
let proxy = new Proxy (target,handler);
```

- `target` —— 是要包装的对象，可以是任何东西，包括函数。
- `handler` —— 代理配置：带有“捕捉器”（“traps”，即拦截操作的方法）的对象。比如 `get` 捕捉器用于读取 `target` 的属性，`set` 捕捉器用于写入 `target` 的属性，等等。

## 捕捉器 

| 内部方法                    | Handler 方法                 | 何时触发                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[[Get]]`               | `get`                      | 读取属性                                                                                                                                                                                                                                                                                                                                                             |
| `[[Set]]`               | `set`                      | 写入属性                                                                                                                                                                                                                                                                                                                                                             |
| `[[HasProperty]]`       | `has`                      | `in` 操作符                                                                                                                                                                                                                                                                                                                                                         |
| `[[Delete]]`            | `deleteProperty`           | `delete` 操作符                                                                                                                                                                                                                                                                                                                                                     |
| `[[Call]]`              | `apply`                    | 函数调用                                                                                                                                                                                                                                                                                                                                                             |
| `[[Construct]]`         | `construct`                | `new` 操作符                                                                                                                                                                                                                                                                                                                                                        |
| `[[GetPrototypeOf]]`    | `getPrototypeOf`           | [Object.getPrototypeOf](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)                                                                                                                                                                                                                                     |
| `[[SetPrototypeOf]]`    | `setPrototypeOf`           | [Object.setPrototypeOf](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)                                                                                                                                                                                                                                     |
| `[[IsExtensible]]`      | `isExtensible`             | [Object.isExtensible](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/isExtensible)                                                                                                                                                                                                                                         |
| `[[PreventExtensions]]` | `preventExtensions`        | [Object.preventExtensions](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/preventExtensions)                                                                                                                                                                                                                               |
| `[[DefineOwnProperty]]` | `defineProperty`           | [Object.defineProperty](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty), [Object.defineProperties](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)                                                                                                   |
| `[[GetOwnProperty]]`    | `getOwnPropertyDescriptor` | [Object.getOwnPropertyDescriptor](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor), `for..in`, `[Object.keys/values/entries](http://object.keys/values/entries)`                                                                                                                                   |
| `[[OwnPropertyKeys]]`   | `ownKeys`                  | [Object.getOwnPropertyNames](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames), [Object.getOwnPropertySymbols](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols), `for..in`, `[Object.keys/values/entries](http://object.keys/values/entries)` |


### 带有get捕捉器的默认值 

语法：
`handler` 应该有 `get(target, property, receiver)`

- `target` —— 是目标对象，该对象被作为第一个参数传递给 `new Proxy`，
- `property` —— 目标属性名，
- `receiver` —— 如果目标属性是一个 getter 访问器属性，则 `receiver` 就是本次读取属性所在的 `this` 对象。




### 使用set捕捉器进行验证 

`set(target, property, value, receiver)`：

- `target` —— 是目标对象，该对象被作为第一个参数传递给 `new Proxy`，
- `property` —— 目标属性名称，
- `value` —— 目标属性的值，
- `receiver` —— 与 `get` 捕捉器类似，仅与 setter 访问器属性相关。
如果写入操作（setting）成功，`set` 捕捉器应该返回 `true`，否则返回 `false`（触发 `TypeError`）。

>[!note 别忘了返回`true`]
>
>对于 `set` 操作，它必须在成功写入时返回 `true`。
>
如果我们忘记这样做，或返回任何假（falsy）值，则该操作将触发 `TypeError`。


### 使用“ownKeys”和“getownpropertydescriptor”进行迭代 


- `Object.getOwnPropertyNames(obj)` 返回非 symbol 键。
- `Object.getOwnPropertySymbols(obj)` 返回 symbol 键。
- `[Object.keys/values()](http://object.keys/values\(\))` 返回带有 `enumerable` 标志的非 symbol 键/值。
- `for..in` 循环遍历所有带有 `enumerable` 标志的非 symbol 键，以及原型对象的键。

语法`handler`  `ownKeys(target)`



### 具有“deleteProperty”和其它捕捉器的受保护属性 

我们将需要以下捕捉器：

- `get` 读取此类属性时抛出错误，
- `set` 写入属性时抛出错误，
- `deleteProperty` 删除属性时抛出错误，
- `ownKeys` 在使用 `for..in` 和像 `Object.keys` 这样的方法时排除以 `_` 开头的属性。

```
user = {
	//...
	checkPassword(value){
		return value === thise._password
	}

}
user = new Proxy(user,{
	get(target,prop){
		if(prop.startsWith('_')){
			throw new Error(!)
		}else{
			let value == target[prop];
			return (typeof value === 'function') ? value.bind(target):value;
		}
	}

})


```

对 `user.checkPassword()` 的调用会将被代理的对象 `user` 作为 `this`（点符号之前的对象会成为 `this`），因此，当它尝试访问 `this._password` 时，`get` 捕捉器将激活（在任何属性读取时，它都会被触发）并抛出错误。

因此，我们在 `(*)` 行中将对象方法的上下文绑定到原始对象 `target`。然后，它们将来的调用将使用 `target` 作为 `this`，不会触发任何捕捉器。

该解决方案通常可行，但并不理想，因为一个方法可能会将未被代理的对象传递到其他地方，然后我们就会陷入困境：原始对象在哪里，被代理的对象在哪里？

此外，一个对象可能会被代理多次（多个代理可能会对该对象添加不同的“调整”），并且如果我们将未包装的对象传递给方法，则可能会产生意想不到的后果。

因此，在任何地方都不应使用这种代理


### 带有has捕捉器的 in range

`has` 捕捉器会拦截 `in` 调用。

`has(target, property)`

- `target` —— 是目标对象，被作为第一个参数传递给 `new Proxy`，
- `property` —— 属性名称

### 包装函数： apply


`apply(target, thisArg, args)` 捕捉器能使代理以函数的方式被调用：

- `target` 是目标对象（在 JavaScript 中，函数就是一个对象），
- `thisArg` 是 `this` 的值。
- `args` 是参数列表


# Reflect

`Reflect` 是一个内建对象，可简化 `Proxy` 的创建。

前面所讲过的内部方法，例如 `[[Get]]` 和 `[[Set]]` 等，都只是规范性的，不能直接调用。

`Reflect` 对象使调用这些内部方法成为了可能。它的方法是内部方法的最小包装

|操作|`Reflect` 调用|内部方法|
|---|---|---|
|`obj[prop]`|`Reflect.get(obj, prop)`|`[[Get]]`|
|`obj[prop] = value`|`Reflect.set(obj, prop, value)`|`[[Set]]`|
|`delete obj[prop]`|`Reflect.deleteProperty(obj, prop)`|`[[Delete]]`|
|`new F(value)`|`Reflect.construct(F, value)`|`[[Construct]]`|


```
let user = {};
Reflect.set(user,'name','john');
alert(user.name);
```

## 代理一个getter
```
let user = {
  _name: "Guest",
  get name() {
    return this._name;
  }
};

let userProxy = new Proxy(user, {
  get(target, prop, receiver) {
    return target[prop]; // 直接访问原始对象属性，未传递 receiver
  }
});

let admin = {
  __proto__: userProxy,
  _name: "Admin"
};

alert(admin.name); // 输出: Guest
```


```
let user = {
  _name: "Guest",
  get name() {
    return this._name;
  }
};

let userProxy = new Proxy(user, {
  get(target, prop, receiver) {
    return Reflect.get(target, prop, receiver); // 传递 receiver，控制 this 绑定
  }
});

let admin = {
  __proto__: userProxy,
  _name: "Admin"
};

alert(admin.name); // 输出: Admin

```

简言之，发起者虽然都是  admin ，但拦截器的实现方式决定了  this  最终绑定到哪个对象——是否通过  Reflect  传递  receiver  是核心差异。


# Proxy的局限性 

### 内部对象：内部插槽（Internal slot）

