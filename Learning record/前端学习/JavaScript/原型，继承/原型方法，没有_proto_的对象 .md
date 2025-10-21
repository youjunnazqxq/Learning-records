# 获取和修改`[[Prototype]]`

- [Object.getPrototypeOf(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf) —— 返回对象 `obj` 的 `[[Prototype]]`。
- [Object.setPrototypeOf(obj, proto)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf) —— 将对象 `obj` 的 `[[Prototype]]` 设置为 `proto`。
-  [Object.create(proto, [descriptors])](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/create) —— 利用给定的 `proto` 作为 `[[Prototype]]` 和可选的属性描述来创建一个空对象。

# Object.create

这是一个方法，可以用来创建一个没有在原型链中的对象例如

```
let animal = {
	eats: true,
};

let rabbit = Object.create(animal,{
	jumps: {
		value :true;
	}
});
```

## 准确浅拷贝

除了递归方法来拷贝外，我们可以借助这个方法来拷贝另外一个对象，例如：
```
let clone = Object.create(
	Object.getPrototypeOf(obj),
	Object.getOwnPropertyDescriptors(obj)	
);
```
`Object.getOwnPropertyDescriptors()` 方法最核心、最独特的作用，就是**它能获取属性的完整“状态”**（即**属性描述符**），而不仅仅是属性的“值”。