
`TextDecoder`（文本解码器）和 `TextEncoder`（文本编码器）是 JavaScript 内置的工具，专门用来**在“二进制数据”和“文本字符串”之间进行转换**。


# TextDecoder（解码过程）

内建的 [TextDecoder](https://encoding.spec.whatwg.org/#interface-textdecoder) 对象在给定缓冲区（buffer）和编码格式（encoding）的情况下，允许将值读取为实际的 JavaScript 字符串。

### 生成解码器
`let decoder = new TextDecoder([label],[options])`

- **`label`** —— 编码格式，默认为 `utf-8`，但同时也支持 `big5`，`windows-1251` 等许多其他编码格式。
- **`options`** —— 可选对象：
    - **`fatal`** —— 布尔值，如果为 `true` 则为无效（不可解码）字符抛出异常，否则（默认）用字符 `\uFFFD` 替换无效字符。
    - **`ignoreBOM`** —— 布尔值，如果为 `true` 则忽略 BOM（可选的字节顺序 Unicode 标记），很少需要使用
### 选中解码对象
` let str = decoder.decode([input],[options])`

- **`input`** —— 要被解码的 `BufferSource`。
- **`options`** —— 可选对象：
    - **`stream`** —— 对于解码流，为 true，则将传入的数据块（chunk）作为参数重复调用 `decoder`。在这种情况下，多字节的字符可能偶尔会在块与块之间被分割。这个选项告诉 `TextDecoder` 记住“未完成”的字符，并在下一个数据块来的时候进行解码。

其本质就是个解码器，给定字节的特定解码


# TextEncoder(编码)

`let encoder = new TexctEncoder()`4

只支持 `utf-8` 编码。

它有两种方法：

- **`encode(str)`** —— 从字符串返回 `Uint8Array`。
- **`encodeInto(str, destination)`** —— 将 `str` 编码到 `destination` 中，该目标必须为 `Uint8Array`。
```
let encoder = new TextEncoder();

let uint8Array = encoder.encode("Hello");
alert(uint8Array); // 72,101,108,108,111
```