

### 1. 最基础的用法 (默认模式)

如果不加任何配置，它就是把对象变成 `key=value` 的形式，用 `&` 连接。

JavaScript

```
import qs from "qs";

const params = { name: "liutao", age: 18 };

// 基础转换
const result = qs.stringify(params);
// 结果: "name=liutao&age=18"
```

_这就像把一张“名片”变成了一行“电报代码”。_

---

### 2. 进阶：你的代码里配置了什么？

你的代码里加了两个“特殊指令”，我们一个个拆解看它的厉害之处：

TypeScript

```
qs.stringify(obj, { 
    arrayFormat: "repeat",             // 指令1：数组怎么处理？
    sort: (a, b) => a.localeCompare(b) // 指令2：顺序怎么排？
})
```

#### 指令 A：`arrayFormat: "repeat"` (数组格式化)

后端对数组的接收格式千奇百怪，这个配置决定了数组变成什么样。

假设数据是：`{ ids: [1, 2] }`

- **默认 (indices)**: `ids[0]=1&ids[1]=2` (PHP常用)
    
- **brackets**: `ids[]=1&ids[]=2` (Node/Express常用)
    
- **YOUR CODE (repeat)**: **`ids=1&ids=2`** (Java/Spring Boot常用)
    

**你的选择：** 你选了 `repeat`，这意味着如果参数里有数组，它会生成多个同名的 key。这是通用性很强的一种格式。

#### 指令 B：`sort` (排序规则)

这是防抖的核心。

假设数据是：`{ b: 2, a: 1 }`

- **默认**: `"b=2&a=1"` (保留原对象顺序)
    
- **YOUR CODE (Sorted)**: **`"a=1&b=2"`** (强制按字母顺序重排)
    

**你的选择：** 你传入了一个排序函数 `(a, b) => a.localeCompare(b)`，这保证了无论属性怎么乱序，生成的字符串永远是 **a 在前，b 在后**。

---

### 3. 实战模拟：它在你的项目中如何工作？

让我们把你定义的 `sortedStringify` 函数跑一遍，看看效果。

**场景：** 用户在一个列表页筛选了状态，并发起了一个 POST 请求。

**输入对象 (`config.data`)：**

JavaScript

```
const postData = {
    status: "active",
    ids: [101, 102],
    keyword: "admin"
};
```

**执行 `sortedStringify(postData)` 的过程：**

1. **第一步：排序**
    
    系统先给 Key 排序：`ids` -> `keyword` -> `status`。
    
    _(注：i 在 k 前，k 在 s 前)_
    
2. **第二步：格式化数组**
    
    识别到 `ids` 是数组，应用 `repeat` 规则。
    
3. **第三步：生成最终字符串**
    
    Plaintext
    
    ```
    "ids=101&ids=102&keyword=admin&status=active"
    ```
    

### 总结

你在代码里这样使用它：

TypeScript

```
// 写法模板
qs.stringify(你要转换的对象, { 配置项 })
```

**它的作用总结：**

它不仅仅是转换，它是一个 **“强迫症转换器”** —— 它强迫所有的参数必须**按字母排好队**，强迫数组必须**按重复格式展开**。

正是这种“强迫症”，保证了两个内容相同的请求生成的“身份证号”绝对一模一样，从而让你的拦截功能精准生效！