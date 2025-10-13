
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




# Set

Set是一个特殊的集合，没有键只有一个值，他的每一个值只能出现一次
- `new Set(iterable)` —— 创建一个 `set`，如果提供了一个 `iterable` 对象（通常是数组），将会从数组里面复制值到 `set` 中。
- `set.add(value)` —— 添加一个值，返回 set 本身
- `set.delete(value)` —— 删除值，如果 `value` 在这个方法调用的时候存在则返回 `true` ，否则返回 `false`。
- `set.has(value)` —— 如果 `value` 在 set 中，返回 `true`，否则返回 `false`。
- `set.clear()` —— 清空 set。
- `set.size` —— 返回元素个数