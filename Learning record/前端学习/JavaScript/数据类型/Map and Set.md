
# Map

与java类似，Map是一个映射，Map运行任何类型的键（与对象只允许字符串和symbol类不同）。
## 方法

- new Map（）
- set（key,value）存值
- map.get(key)//如果不存在返回undefined
- map.has(key)//判断是否存在
- map.clear
- map.size

## 对象用作键
与对象不同的是，map可以用对象用作键，而对象呢，存入的时候对象回变为“object Object”
>[! note ]
>链式调用
>map.set方法会返回map本身

## Map迭代
- `map.keys()` —— 遍历并返回一个包含所有键的可迭代对象，
- `map.values()` —— 遍历并返回一个包含所有值的可迭代对象，
- `map.entries()` —— 遍历并返回一个包含所有实体 `[key, value]` 的可迭代对象，`for..of` 在默认情况下使用的就是这个。


## 从对象中创建Map

```
let obj = {
	name: "John",
	age: 30,
}
let map = new Map(Object.entries(obj));
```
`Object.entries` 返回键/值对数组：`[ ["name","John"], ["age", 30] ]`。这就是 `Map` 所需要的格式。


### entries方法
这个方法，传入进里面的对象中的属性会被转换为["键"，值]这样的数组，然后整体组成一个二维数组。



## 从Map中创建对象

```
let map =new Map();
map.set("bannaa0",1);

let obj = Object.fromEntries(map.entries());

alert(obj.banana1);//2
```
上面的代码作用也是一样的，因为 `Object.fromEntries` 期望得到一个可迭代对象作为参数，而不一定是数组。并且 `map` 的标准迭代会返回跟 `map.entries()` 一样的键/值对。因此，我们可以获得一个普通对象（plain object），其键/值对与 `map` 相同。
# Set

Set是一个特殊的集合，没有键只有一个值，他的每一个值只能出现一次
- `new Set(iterable)` —— 创建一个 `set`，如果提供了一个 `iterable` 对象（通常是数组），将会从数组里面复制值到 `set` 中。
- `set.add(value)` —— 添加一个值，返回 set 本身
- `set.delete(value)` —— 删除值，如果 `value` 在这个方法调用的时候存在则返回 `true` ，否则返回 `false`。
- `set.has(value)` —— 如果 `value` 在 set 中，返回 `true`，否则返回 `false`。
- `set.clear()` —— 清空 set。
- `set.size` —— 返回元素个数