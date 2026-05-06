`qs` (Query String) 是前端最经典、最强大的 URL 参数解析和序列化库。哪怕你不用它做防抖，在对接复杂的 GET 请求参数，或者发送 `application/x-www-form-urlencoded` 表单数据时，它也是企业级项目里的必备神器。

它对外暴露的接口极其精简，核心就是一正一反两个方法：**`qs.stringify`** 和 **`qs.parse`**。

### 1. `qs.stringify(object, [options])` —— “对象转字符串”（你当前最需要的）

**作用：** 把一个 JavaScript 对象，按照规则序列化成 URL 后面拼接的那串字符（也就是 `key=value&key=value` 的格式）。

**需要传入什么：**

- **参数 1：`object` (必传)**：你要转换的 JS 对象或数组。
    
- **参数 2：`options` (可选)**：配置对象，这是 `qs` 的灵魂所在，用来精细控制转换的规则。
    

**最常用、最强大的 `options` 配置项：**

- **`sort` (排序规则)：** 这就是刚才完美解决你“指纹特征一致性”问题的核心参数！你可以传入一个比较函数，强制让对象里的 Key 按照字母表顺序转换。
    
    JavaScrip
    
    ```
    qs.stringify({ c: 1, a: 2, b: 3 }, { sort: (a, b) => a.localeCompare(b) });
    // 无论原始对象顺序如何，结果严格按照 a, b, c 排列："a=2&b=3&c=1"
    ```
    
- **`arrayFormat` (数组转译格式)：** 后端对数组的接收偏好各不相同。假设前端传一个 `{ ids: [1, 2] }`，你可以通过这个参数一键切换格式：
    
    - `indices` (默认)：`"ids[0]=1&ids[1]=2"`
        
    - `brackets`：`"ids[]=1&ids[]=2"`
        
    - `repeat` (企业开发最常见，Java/Go 极度偏好)：`"ids=1&ids=2"`
        
    - `comma`：`"ids=1,2"`
        
- **`skipNulls` (忽略空值)：** 设为 `true` 后，对象里那些值为 `null` 或 `undefined` 的字段会被彻底当做透明人，不会拼装出 `name=undefined` 这种给后端添堵的脏数据。
    

### 2. `qs.parse(string, [options])` —— “字符串转对象”

**作用：** 它的逻辑是反过来的，把一段 URL 查询字符串，反序列化成一个方便你提取数据的 JavaScript 对象。

**需要传入什么：**

- **参数 1：`string` (必传)**：待解析的字符串（例如 `"a=1&b=2"`）。
    
- **参数 2：`options` (可选)**：用来控制解析深度的配置。
    

**例子：**

JavaScript

```
qs.parse("a=1&b=2&c[]=3&c[]=4");
// 结果：{ a: '1', b: '2', c: ['3', '4'] }
```
