
# Symbol.iteraror

这是一个返回迭代器的方法，属于一个内建的symbol

例如：
```
let range = {
	from: 1,
	to: 5,
};
range[Symbol.iterator] = function(){
	return {
	current: this.from,
	last: this.to,
		next(){
		if(this.current <= this.last)｛
		return {done: false,value:this.current++};
		}else{
		return {done: true}};
	}

}
```
#### **. 可迭代协议 (The Iterable Protocol)**

此协议定义了任何一个对象要成为“可迭代 (iterable)”所必须满足的条件。

- **实现方式**：对象必须实现一个 `[Symbol.iterator]` 方法。即该对象必须拥有一个以 `Symbol.iterator` 这个“众所周知”的 Symbol 作为键的属性。
    
- **方法职责**：这个 `[Symbol.iterator]` 方法本身是一个**迭代器工厂 (Iterator Factory)**。它是一个无参数的函数，其唯一的职责是创建并返回一个遵循**迭代器协议**的**迭代器 (Iterator)** 对象。
    

#### **3. 迭代器协议 (The Iterator Protocol)**

此协议定义了迭代器对象的标准结构，它规定了从一个可迭代对象中逐个获取值的标准方式。

- **实现方式**：一个对象要成为“迭代器 (iterator)”，它必须实现一个 `next()` 方法。
    
- **`next()` 方法职责**：
    
    - 该方法是一个无参数的函数。
        
    - 它必须返回一个包含以下两个属性的对象：
        
        1. `done` (布尔值)：
            
            - 若为 `false`，表示迭代尚未结束，可以继续获取下一个值。
                
            - 若为 `true`，表示迭代已经完成，后续不应再有值。
                
        2. `value` (任意类型)：
            
            - 当 `done` 为 `false` 时，`value` 是迭代序列中的当前元素值。
                
            - 当 `done` 为 `true` 时，`value` 是迭代器结束时可选的返回值。
                

#### **4. 协议的协同工作流程**

以 `for...of` 循环为例，其工作流程完美地展示了两种协议的协同：

1. `for...of` 循环开始时，它首先调用**可迭代对象**的 `[Symbol.iterator]` 方法（迭代器工厂）。
    
2. 该工厂方法返回一个**迭代器**对象。
    
3. `for...of` 循环在内部保存这个迭代器，并在每一轮循环开始时，调用该迭代器的 `next()` 方法。
    
4. 循环检查 `next()` 方法返回的结果对象。
    
    - 如果 `done` 为 `false`，则将其 `value` 属性的值赋给循环变量，并执行循环体。
        
    - 如果 `done` 为 `true`，则立即终止循环。



# Array.from 

Array.from方法接受一个对象，检查它是一个可迭代对象或类数组对象，然后再创建一个新数组(新数组只保护值)，当然它还有第二个参数，这个参数接受一个函数，对其中的值进行运算。
