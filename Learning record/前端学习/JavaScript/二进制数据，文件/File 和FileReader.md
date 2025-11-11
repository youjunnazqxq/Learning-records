
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

