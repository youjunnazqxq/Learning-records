`type()` 是 Python 中的一个内置函数，它有两种主要的用法，取决于你给它传递多少个参数。

### 1. `type(object)` - 获取对象的类型 (一个参数)

当 `type()` 函数只接收一个参数时，它会返回该参数对象的类型。这是最常见的用法。

**作用**:

- 检查一个变量或值是什么类型。
- 这在调试或需要根据不同类型执行不同操作时很有用。

**示例**:

Python

```
a = 5
print(type(a))  # 输出: <class 'int'>

b = 4.5
print(type(b))  # 输出: <class 'float'>

c = "Hello"
print(type(c))  # 输出: <class 'str'>

d = [1, 2, 3]
print(type(d))  # 输出: <class 'list'>

e = (1, 2, 3)
print(type(e))  # 输出: <class 'tuple'>

f = {"key": "value"}
print(type(f))  # 输出: <class 'dict'>

g = True
print(type(g))  # 输出: <class 'bool'>

def my_function():
    pass
print(type(my_function)) # 输出: <class 'function'>

class MyClass:
    pass
my_instance = MyClass()
print(type(my_instance)) # 输出: <class '__main__.MyClass'> (或模块名.MyClass)
print(type(MyClass))     # 输出: <class 'type'> (类本身也是对象，其类型是 'type')
```

**用于类型检查**: 你可以使用 `type()` 来检查一个对象的类型是否是你期望的特定类型：

Python

```
x = 10
if type(x) == int:
    print("x 是一个整数")
else:
    print("x 不是一个整数")
```

**注意**: 对于类型检查，通常更推荐使用 `isinstance()` 函数，因为它能正确处理继承关系。`type(obj) == SomeClass` 只会在 `obj` 是 `SomeClass` 的直接实例时返回 `True`，而不会考虑 `obj` 是否是 `SomeClass` 的子类的实例。