**`File` 对象 _就是_ 一个 `Blob` 对象，只不过它额外多带了** 3 **个来自你电脑（操作系统）的“元数据”（metadata）：**

[File](https://www.w3.org/TR/FileAPI/#dfn-file) 对象继承自 `Blob`，并扩展了与文件系统相关的功能。

有两种方式可以获取它

第一种，与 `Blob` 类似，有一个构造器：

`new File (fileParts,fileName,[otions])`


- **`fileParts`** —— Blob/BufferSource/String 类型值的数组。
- **`fileName`** —— 文件名字符串。
- **`options`** —— 可选对象：
    - **`lastModified`** —— 最后一次修改的时间戳（整数日期）。


第二种，更常见的是，我们从 `<input type="file">` 或拖放或其他浏览器接口来获取文件。在这种情况下，file 将从操作系统（OS）获得 this 信息。

由于 `File` 是继承自 `Blob` 的，所以 `File` 对象具有相同的属性，附加：

- `name` —— 文件名，
- `lastModified` —— 最后一次修改的时间戳。

# FileReader

[FileReader](https://www.w3.org/TR/FileAPI/#dfn-filereader) 是一个对象，其唯一目的是从 `Blob`（因此也从 `File`）对象中读取数据。

它使用事件来传递数据，因为从磁盘读取数据可能比较费时间

`let reader = new FileReader();`


- **`readAsArrayBuffer(blob)`** —— 将数据读取为二进制格式的 `ArrayBuffer`。
- **`readAsText(blob, [encoding])`** —— 将数据读取为给定编码（默认为 `utf-8` 编码）的文本字符串。
- **`readAsDataURL(blob)`** —— 读取二进制数据，并将其编码为 base64 的 data url。
- **`abort()`** —— 取消操作。

`read*` 方法的选择，取决于我们喜欢哪种格式，以及如何使用数据。

- `readAsArrayBuffer` —— 用于二进制文件，执行低级别的二进制操作。对于诸如切片（slicing）之类的高级别的操作，`File` 是继承自 `Blob` 的，所以我们可以直接调用它们，而无需读取。
- `readAsText` —— 用于文本文件，当我们想要获取字符串时。
- `readAsDataURL` —— 当我们想在 `src` 中使用此数据，并将其用于 `img` 或其他标签时。正如我们在 [Blob](https://zh.javascript.info/blob) 一章中所讲的，还有一种用于此的读取文件的替代方案：`URL.createObjectURL(file)`。

读取过程中，有以下事件：

- `loadstart` —— 开始加载。
- `progress` —— 在读取过程中出现。
- `load` —— 读取完成，没有 error。
- `abort` —— 调用了 `abort()`。
- `error` —— 出现 error。
- `loadend` —— 读取完成，无论成功还是失败。

读取完成后，我们可以通过以下方式访问读取结果：

- `reader.result` 是结果（如果成功）
- `reader.error` 是 error（如果失败）。

