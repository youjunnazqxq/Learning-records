好的，我们来详细了解一下 `extend()` 函数。

---

## `extend()` 方法的介绍

`extend()` 是 Python 中列表（List）的一个内置方法，它用于将一个**可迭代对象**（如另一个列表、元组、字符串、集合等）中的**所有元素**逐个添加到当前列表的**末尾**。

**核心思想：** 将一个序列的所有元素“展开”并合并到当前列表的末尾。

### 基本语法

Python

```
list.extend(iterable)
```

- `list`: 你想要添加元素的列表对象。
    
- `iterable`: 任何可迭代对象，其内部的所有元素都将被添加到 `list` 的末尾。
    

`extend()` 方法**没有返回值**（或者说返回 `None`），它会**直接修改**原始列表。

**示例 1：扩展一个列表**

Python

```
my_list = [1, 2, 3]
another_list = [4, 5]

my_list.extend(another_list)
print(my_list) # 输出: [1, 2, 3, 4, 5]
```

**示例 2：扩展一个元组**

Python

```
my_list = ['a', 'b']
my_tuple = ('c', 'd', 'e')

my_list.extend(my_tuple)
print(my_list) # 输出: ['a', 'b', 'c', 'd', 'e']
```

**示例 3：扩展一个字符串（字符串也是可迭代的）**

注意，字符串会被视为字符的序列。

Python

```
my_list = ['hello']
my_string = "world"

my_list.extend(my_string)
print(my_list) # 输出: ['hello', 'w', 'o', 'r', 'l', 'd']
```

**示例 4：与 `append()` 的区别**

这是一个理解 `extend()` 的关键点。

Python

```
list_append = [1, 2]
list_extend = [1, 2]

# append() 将整个可迭代对象作为一个单一元素添加
list_append.append([3, 4])
print(list_append) # 输出: [1, 2, [3, 4]]

# extend() 将可迭代对象中的每个元素逐个添加
list_extend.extend([3, 4])
print(list_extend) # 输出: [1, 2, 3, 4]
```

---

## `extend()` 方法的原理

`extend()` 方法的原理与 `append()` 在底层内存管理上相似，但在处理多元素时表现不同：

1. **逐个添加：** `extend()` 会遍历传入的 `iterable`，并将其中的每个元素逐个添加到当前列表的末尾。
    
2. **内存分配：** 类似 `append()`，当当前列表的容量不足以容纳来自 `iterable` 的所有新元素时，Python 可能会重新分配一块更大的内存空间，将现有元素和新元素一起复制过去。
    
3. **效率：** `extend()` 操作的平均时间复杂度通常是 **O(k)**，其中 `k` 是要添加的 `iterable` 中元素的数量。这是因为 `extend()` 实际上是循环地调用内部的“添加元素”逻辑，对于每个要添加的元素，平均操作是常数时间的。
    

---

## 注意事项

在使用 `extend()` 方法时，请注意以下几点：

1. **修改原始列表：** `extend()` 方法会**直接修改**你调用的列表，而不是返回一个新的列表。如果你需要保留原始列表不变，可以先创建一个副本（例如使用 `list.copy()` 或切片 `[:]`），然后对副本进行操作。
    
    Python
    
    ```
    original = [1, 2]
    new_list = original.copy()
    new_list.extend([3, 4])
    print(original) # 输出: [1, 2] (原始列表未变)
    print(new_list)  # 输出: [1, 2, 3, 4]
    ```
    
2. **接受任何可迭代对象：** `extend()` 不仅仅接受列表，还可以接受元组、集合、字符串、字典的键（`dict.keys()`）、生成器表达式等任何可迭代对象。它会遍历这些对象并将它们的元素逐一添加。
    
    Python
    
    ```
    my_list = [10]
    my_set = {20, 30} # 集合无序，添加顺序不确定
    my_list.extend(my_set)
    print(my_list) # 可能输出: [10, 20, 30] 或 [10, 30, 20]
    
    my_list_2 = [1]
    my_dict = {'a': 1, 'b': 2}
    my_list_2.extend(my_dict.keys()) # 默认迭代字典的键
    print(my_list_2) # 输出: [1, 'a', 'b']
    ```
    
3. **与列表拼接操作符 `+` 的对比：**
    
    - `list1 + list2`: 这个操作符会创建并返回一个**新的列表**，包含了 `list1` 和 `list2` 的所有元素。它不会修改原始列表。
        
    - list1.extend(list2): 这个方法会原地修改 list1，将 list2 的元素添加到 list1 的末尾，没有返回值。
        
        当你不需要创建新列表，只想在现有列表上添加元素时，extend() 通常更高效，因为它避免了创建中间列表的开销。
        
    
    Python
    
    ```
    list_a = [1, 2]
    list_b = [3, 4]
    
    # 使用 + 创建新列表
    result_list = list_a + list_b
    print(result_list) # 输出: [1, 2, 3, 4]
    print(list_a)      # 输出: [1, 2] (list_a 未变)
    
    # 使用 extend 原地修改
    list_c = [1, 2]
    list_d = [3, 4]
    list_c.extend(list_d)
    print(list_c)      # 输出: [1, 2, 3, 4] (list_c 已修改)
    print(list_d)      # 输出: [3, 4] (list_d 未变)
    ```
    
4. **返回值为 `None`：** 由于 `extend()` 会修改原始列表，它的返回值是 `None`。因此，不要尝试将 `extend()` 的结果赋值给变量，除非你明确想要赋值 `None`。
    

---

希望这次对 `extend()` 方法的详细解释对您有所帮助！您还有其他想了解的 Python 函数或概念吗？