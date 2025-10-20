在js中，我们可以将文件转化为JSON格式，以便进行传输。

# JSON转化
可以用 JSON.stringify()进行转化

## 忽略的东西 

- 函数属性（方法）。
- Symbol 类型的键和值。
- 存储 `undefined` 的属性。

# JavaScript to JSON 转换规则 (`JSON.stringify`)

以下是关于 `JSON.stringify()` 如何转换不同 JavaScript 数据类型的详细规则笔记。

---

### 转换规则详情表

| JavaScript 类型 (Type) | `JSON.stringify()` 转换结果        | 备注 (Notes)                                                                                |
| :------------------- | :----------------------------- | :---------------------------------------------------------------------------------------- |
| **String**           | JSON 字符串 (用双引号包裹)              | 例如: `'hello'` 变为 `"hello"`                                                                |
| **Number**           | JSON 数字                        | 例如: `123` 变为 `123`, `3.14` 变为 `3.14`                                                      |
|                      | `NaN`, `Infinity`, `-Infinity` | 转换为 `null`                                                                                |
| **Boolean**          | `true` 或 `false` (无引号)         | 例如: `true` 变为 `true`                                                                      |
| **`null`**           | `null` (无引号)                   | 例如: `null` 变为 `null`                                                                      |
| **Object**           | JSON 对象 (`{...}`)              | 属性名和字符串属性值都会被双引号包裹。                                                                       |
| **Array**            | JSON 数组 (`[...]`)              | 数组中的每个元素会根据其类型递归地进行转换。                                                                    |
| **Date**             | ISO 8601 日期格式的字符串              | `new Date()` 会被转换为类似 `"2025-10-13T14:30:00.000Z"` 的字符串。                                   |
| **`undefined`**      | (见备注)                          | - 单独转换: 返回 `undefined`。<br>- **在对象中**: 该属性会被**忽略**（完全跳过）。<br>- **在数组中**: 该元素会被转换为 `null`。 |
| **Function**         | (见备注)                          | 规则同 `undefined`。                                                                          |
| **Symbol**           | (见备注)                          | 规则同 `undefined`。                                                                          |
| **BigInt**           | 抛出 `TypeError` 错误              | JSON 规范不支持 BigInt。                                                                        |

---

> [!TIP] 核心要点总结
> - **有损转换**: `JSON.stringify` 是一种有损转换，`undefined`、`Function`、`Symbol` 等类型的信息会丢失或改变。
> - **数据纯粹性**: JSON 是一种纯粹的数据交换格式，不包含任何可执行代码（如函数）。
> - **数组与对象的关键区别**: 注意 `undefined` 在数组中变为 `null`，而在对象中则直接被忽略，这是最常见的陷阱之一。
## JSON.stringfiy


```
let json = JSON.stringify(value[,replacer,space]);
```

value

要编码的值。

replacer

要编码的属性数组或映射函数 `function(key, value)`。
repalce接受两个参数，key和value，对于符合它条件的对象，它会进行操作（认为定义），

space

用于格式化的空格数量
replacer：函数的编写
```
function replacer(key, value) {
  // 1. 分析当前处理的属性
  console.log(`处理属性: ${key}, 值:`, value);
  
  // 2. 根据业务逻辑决定如何处理
  if (需要排除该属性) {
    return undefined;
  } else if (需要转换该值) {
    return 转换后的值;
  } else {
    // 3. 默认情况：正常序列化
    return value;
  }
}
```
>[!note]
不得有循环引用，这样会直接报错，不过我们可以通过这个方法来规避这样的错误


这个方法呢，他接受（key，value），然后返回重新定义的值，。


# JSON.parse

解码JSON字符串

但是这只能进行基本解码，要解析为其它对象的话要函数

例如
```
let str = "";
let meetup = JSON.parse(str,function(key,value){
	if(key == 'date') return new Date(value);
	return value;
})
```


对于map和set来说，他们在 序列化的时候就已经转化为一个小数组了例如

```
let map = new Map();
map.set("youjun",优君)；

let json = JSON.stringjgf(map);

// [[youjun,优君]]；
```

这样我们就需要这种特殊的方法来进行转化
