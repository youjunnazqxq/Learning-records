## [[Inheritance]]
例子
```
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True   # 它还活着！！！
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " 吃了一个 " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print(self.name + ' 说 汪！')
```
继承，这里的dog继承了pet的属性，而dog中的talk又重写了这个原talk。[[super]]函数意在调用父级函数
`super()` 函数的主要作用，尤其是在子类中重写（override）了父类的方法时，就是让你能够**在子类的这个重写方法中调用父类中那个被重写的方法**。

这样做的主要好处是：

1. **扩展而非完全替换**：你可以在父类方法的基础上添加新的功能，而不是完全从头开始写。子类可以先执行父类的通用逻辑，然后再执行自己特有的逻辑（或者反过来）。
    
    - 例如，在之前的 `Dog` 和 `Pet` 的例子中，`Dog` 的 `talk` 方法通过 `super().talk()` 先调用了 `Pet` 的 `talk` 方法（打印名字），然后再打印自己特有的 "汪！"。
2. **代码重用**：避免在子类中重复编写父类已经实现过的代码。
    
3. **维护性**：如果父类的方法实现发生改变，只要接口不变，子类通过 `super()` 调用就能自动获得更新，而不需要修改子类代码（除非子类特有的逻辑依赖于父类旧的实现细节）。
    
4. **处理复杂继承关系**：尤其是在多重继承中，`super()` 会按照方法解析顺序（MRO - Method Resolution Order）来正确地调用“下一个”父类的方法，避免了直接写死父类名可能带来的问题。

## Q1

**`super().__init__()`**

- **理解**：
    - `super()`：正确地调用了 `super` 函数，它返回一个临时对象，该对象解析方法时会查找父类 (`Butterfly`)。
    - `.__init__()`：通过这个临时对象调用 `__init__` 方法。这会自动将当前 `Monarch` 实例 (`self`) 作为第一个参数传递给 `Butterfly` 的 `__init__` 方法。由于我们没有传递 `wings` 参数，`Butterfly` 的 `__init__` 方法会使用其默认值 `wings=2`。
- **评价**：这种写法是**正确**的 (在Python 3中是推荐的方式)。它会使得 `Monarch` 实例拥有

**`Butterfly.__init__(self)`**

- **理解**：这是直接通过父类的类名来调用其 `__init__` 方法，并且显式地将当前 `Monarch` 实例 (`self`) 作为第一个参数传递进去。由于没有传递 `wings` 参数，`Butterfly` 的 `__init__` 方法会使用其默认值 `wings=2`。
- **评价**：这种写法是**正确**的。这是在旧版本Python (Python 2) 中以及某些特定情况下仍然有效的方式来调用父类方法。它会使得 `Monarch` 实例拥有 `self.wings = 2`。

```
class MimicButterfly(Butterfly)
	def __init__(self,mimic_animal):
		super().__init__()
		self.minic_animal=mimic_animal
```


## Q2
```
class Circle(Shape):
	def __init__(self,name,radius)
		super.__init__(name)
		

```
## [[repr]]&&[[str]]


|函数|用途|输出风格|适合场景|
|---|---|---|---|
|`str()`|面向用户的“可读性强”的表示|更简洁、直观|打印展示给用户看|
|`repr()`|面向开发者的“精确”表示|更详细，尽可能是合法 Python 表达式|调试或日志记录时使用|```

```
s = "hello"

repr(s)      # 输出：'"hello"'（外层多一层引号，表示这是一个字符串对象）
s            # 输出：'hello'（repr 的简化展示）
print(repr(s))  # 输出：hello（只打印内容，引号被去掉）
str(s)       # 输出：'hello'
print(s)     # 输出：hello（str 方法，直接展示内容）
print函数会直接调用str（）函数，而在交互式中会直接调用repr（）方法

