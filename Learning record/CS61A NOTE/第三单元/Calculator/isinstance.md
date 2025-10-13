好的，这里是 `isinstance()` 的笔记形式总结。

---

### **Python `isinstance()` 核心笔记**

#### **1. 核心功能**

- 判断一个对象是否是指定类（或其子类）的实例。

#### **2. 语法**

- `isinstance(object, classinfo)`
    - `object`: 要检查的对象。
    - `classinfo`: 一个类，或是一个包含多个类的元组 `(class1, class2, ...)`。

#### **3. 关键特性**

- **考虑继承**：子类的实例也被认为是父类的实例。这是它与 `type()` 的最大区别。
- **检查多类型**：`classinfo` 可以是一个元组，只要对象属于元组中任意一个类型，就返回 `True`。
- **返回值**：布尔值 (`True` / `False`)。

#### **4. `isinstance()` vs `type()`**

- `isinstance()`: 关注 **"是一个..."** 的关系 (is-a relationship)，推荐使用。
    - `isinstance(Dog(), Animal)` => `True`
- `type()`: 进行精确类型匹配，不考虑继承。
    - `type(Dog()) == Animal` => `False`

#### **5. 快速示例**

Python

```
# 定义类
class Animal: pass
class Dog(Animal): pass

my_dog = Dog()
num = 100

# 检查继承关系
print(isinstance(my_dog, Animal))  # True

# 检查精确类型
print(isinstance(num, int))        # True

# 检查是否为多种类型之一
print(isinstance(num, (str, list, int))) # True
```


## [[is,isinstance,type, =]]

