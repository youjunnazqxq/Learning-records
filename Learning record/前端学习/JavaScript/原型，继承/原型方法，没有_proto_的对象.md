
# 获取和设置原型的方法
- [Object.getPrototypeOf(obj)](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf) —— 返回对象 `obj` 的 `[[Prototype]]`。
- Object.setPrototypeOf(obj, proto) —— 将对象 `obj` 的 `[[Prototype]]` 设置为 `proto`
- [Object.create(proto, [descriptors])](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/Object/create) —— 利用给定的 `proto` 作为 `[[Prototype]]` 和可选的属性描述来创建一个空对象


```
let animal = {
	eats: true,
};
	let rabbit = Object.creat(animal,{
		jumps:{
			value: ture,
		}
	})

```


我们还可以通过此方法来试下深层拷贝：
```
let clon = Object.creat(
	Object.getPrototypeOf(obj),
	Object.getOwnPropertyDescriptors(obj)
);

```

## Object.getOwnPropertyDescriptors(obj)

- 作用：获取 obj 自身所有属性（不包含原型链上的属性）对应的“属性描述符”（无论属性是可枚举/不可枚举、普通属性/ getter/setter ）