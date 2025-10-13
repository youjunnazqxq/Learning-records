
## `append()` 方法的介绍

`append()` 是 Python 中列表（List）的一个内置方法，用于在列表的**末尾**添加一个元素。

### 基本语法

Python

```
list.append(item)
```

- `list`: 你想要添加元素的列表对象。
    
- `item`: 任何你想要添加到列表末尾的元素。这个元素可以是任何数据类型（数字、字符串、布尔值、甚至是另一个列表、元组、字典等）。
    

`append()` 方法**没有返回值**（或者说返回 `None`），它会**直接修改**原始列表。

**示例：**

Python

```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # 输出: [1, 2, 3, 4]

my_list.append("hello")
print(my_list) # 输出: [1, 2, 3, 4, 'hello']

another_list = [5, 6]
my_list.append(another_list)
print(my_list) # 输出: [1, 2, 3, 4, 'hello', [5, 6]]
```

---

## `append()` 方法的原理

`append()` 方法的实现原理相对直接，主要涉及以下几点：

1. **内存分配：** 当你使用 `append()` 方法向列表中添加一个元素时，Python 可能会重新分配内存。列表在内部通常实现为动态数组。这意味着当列表的当前容量不足以容纳新元素时，Python 会在内存中找到一块更大的连续空间，将现有元素复制过去，然后添加新元素。这个过程是自动处理的，对用户透明。
    
2. **效率：** 由于 `append()` 是在列表末尾添加元素，通常这是一个非常高效的操作，其时间复杂度平均为 **O(1)** (常数时间)。这是因为通常会有预留的内存空间来避免每次添加都重新分配内存。但在少数情况下，当列表需要扩容时，复制所有元素会导致时间复杂度变为 **O(n)** (线性时间)，但这种情况分摊下来仍然是 O(1)。
    
3. **引用而非复制：** 如果你 `append()` 的是一个可变对象（如另一个列表或字典），那么列表中存储的将是对该对象的**引用**，而不是该对象的一个新副本。这意味着如果你修改了被添加的原始对象，列表中的元素也会随之改变。
    

**原理示例：**

Python

```
original_inner_list = [10, 20]
main_list = ['A', 'B']

main_list.append(original_inner_list)
print(main_list) # 输出: ['A', 'B', [10, 20]]

original_inner_list.append(30) # 修改了原始的 inner_list

print(main_list) # 输出: ['A', 'B', [10, 20, 30]] - main_list 中的元素也随之改变
```

---

## 注意事项

在使用 `append()` 方法时，需要注意以下几点：

1. **修改原始列表：** `append()` 方法会**直接修改**你调用的列表，而不是返回一个新的列表。如果你需要保留原始列表不变，可以先创建一个副本（例如使用 `list.copy()` 或切片 `[:]`），然后对副本进行操作。
    
    Python
    
    ```
    original = [1, 2]
    new_list = original.copy() # 创建副本
    new_list.append(3)
    print(original) # 输出: [1, 2] (原始列表未变)
    print(new_list)  # 输出: [1, 2, 3]
    ```
    
2. **一次添加一个元素：** `append()` 每次只能添加一个元素。如果你想添加多个元素，或者添加一个可迭代对象（如另一个列表）中的所有元素，你应该使用 `extend()` 方法或列表拼接操作符 `+`。
    
    Python
    
    ```
    my_list = [1, 2]
    my_list.append([3, 4])
    print(my_list) # 输出: [1, 2, [3, 4]] (整个列表 [3, 4] 作为单个元素添加)
    
    my_list = [1, 2]
    my_list.extend([3, 4])
    print(my_list) # 输出: [1, 2, 3, 4] (元素 3 和 4 分别添加)
    
    # 或者使用拼接
    my_list = [1, 2] + [3, 4]
    print(my_list) # 输出: [1, 2, 3, 4]
    ```
    
3. **返回值为 `None`：** 由于 `append()` 会修改原始列表，它的返回值是 `None`。因此，不要尝试将 `append()` 的结果赋值给变量，除非你明确想要赋值 `None`。
    
    Python
    
    ```
    my_list = [1, 2]
    result = my_list.append(3)
    print(result) # 输出: None
    print(my_list) # 输出: [1, 2, 3]
    ```
    
4. **在循环中追加：** 在循环中动态构建列表时，`append()` 是非常常用的方法。
    
    Python
    
    ```
    squares = []
    for i in range(5):
        squares.append(i * i)
    print(squares) # 输出: [0, 1, 4, 9, 16]
    ```
    