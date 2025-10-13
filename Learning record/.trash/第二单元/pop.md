`pop()` 函数在 Python 中主要用于从列表 (list) 或字典 (dictionary) 中移除元素，并返回被移除的元素。它的具体行为取决于它作用的对象类型。

**1. 对于列表 (list):**

`list.pop([index])`

- **不带参数时 `list.pop()`:**
    
    - 移除列表中的 **最后一个** 元素。
    - 返回被移除的那个元素的值。
    - 如果列表为空，调用 `pop()` 会引发 `IndexError` 异常。
    
    示例：
    
    Python
    
    ```
    my_list = [10, 20, 30, 40]
    removed_element = my_list.pop()
    print(f"被移除的元素: {removed_element}") # 输出: 被移除的元素: 40
    print(f"列表更新后: {my_list}")       # 输出: 列表更新后: [10, 20, 30]
    
    empty_list = []
    # empty_list.pop() # 这行会引发 IndexError
    ```
    
- **带索引参数时 `list.pop(index)`:**
    
    - 移除列表中 **指定索引 (index)** 处的元素。
    - 返回被移除的那个元素的值。
    - 如果指定的索引超出了列表的范围，会引发 `IndexError` 异常。
    
    示例：
    
    Python
    
    ```
    my_list = [10, 20, 30, 40]
    removed_element = my_list.pop(1) # 移除索引为 1 的元素 (即 20)
    print(f"被移除的元素: {removed_element}") # 输出: 被移除的元素: 20
    print(f"列表更新后: {my_list}")       # 输出: 列表更新后: [10, 30, 40]
    
    # my_list.pop(5) # 这行会引发 IndexError，因为索引 5 超出范围
    ```
    

**2. 对于字典 (dictionary):**

`dict.pop(key[, default])`

- **`dict.pop(key)`:**
    
    - 移除字典中指定 **键 (key)** 及其对应的值。
    - 返回与该键关联的 **值 (value)**。
    - 如果指定的键在字典中不存在，会引发 `KeyError` 异常。
    
    示例：
    
    Python
    
    ```
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    removed_value = my_dict.pop('age')
    print(f"被移除的值: {removed_value}") # 输出: 被移除的值: 30
    print(f"字典更新后: {my_dict}")   # 输出: 字典更新后: {'name': 'Alice', 'city': 'New York'}
    
    # my_dict.pop('country') # 这行会引发 KeyError，因为 'country' 键不存在
    ```
    
- **`dict.pop(key, default)`:**
    
    - 移除字典中指定键 (key) 及其对应的值。
    - 返回与该键关联的值。
    - 如果指定的键在字典中不存在，它 **不会引发 `KeyError`**，而是返回你提供的 **`default` 值**。字典本身不会被修改（因为键不存在）。
    
    示例：
    
    Python
    
    ```
    my_dict = {'name': 'Alice', 'city': 'New York'}
    removed_value = my_dict.pop('age', 'N/A') # 'age' 键不存在，返回默认值 'N/A'
    print(f"被移除/获取的值: {removed_value}") # 输出: 被移除/获取的值: N/A
    print(f"字典更新后: {my_dict}")      # 输出: 字典更新后: {'name': 'Alice', 'city': 'New York'}
    
    removed_value_existing = my_dict.pop('name', 'N/A') # 'name' 键存在
    print(f"被移除/获取的值: {removed_value_existing}") # 输出: 被移除/获取的值: Alice
    print(f"字典更新后: {my_dict}")      # 输出: 字典更新后: {'city': 'New York'}
    ```
    

**总结：**

`pop()` 函数的核心作用是“移除并返回”。

- 在列表中，它基于元素的位置（索引）操作。
- 在字典中，它基于键来操作。 它会直接修改原始的列表或字典。