
`Blob` 由一个可选的字符串 `type`（通常是 MIME 类型）和 `blobParts` 组成 —— 一系列其他 `Blob` 对象，字符串和 `BufferSource`。
![[Screenshot_20251111_085521_mark.via.png]]



语法为 ：
` new Blob(blobParts,options);`


- **`blobParts`** 是 `Blob`/`BufferSource`/`String` 类型的值的数组。
- **`options`** 可选对象：
    - **`type`** —— `Blob` 类型，通常是 MIME 类型，例如 `image/png`，
    - **`endings`** —— 是否转换换行符，使 `Blob` 对应于当前操作系统的换行符（`\r\n` 或 `\n`）。默认为 `"transparent"`（啥也不做），不过也可以是 `"native"`（转换）



# Blob用作URL
Blob 可以很容易用作 `<a>`、`<img>` 或其他标签的 URL，来显示它们的内容。

多亏了 `type`，让我们也可以下载/上传 `Blob` 对象，而在网络请求中，`type` 自然地变成了 `Content-Type`。
浏览器内部为每个通过 `URL.createObjectURL` 生成的 URL 存储了一个 URL → `Blob` 映射。因此，此类 URL 很短，但可以访问 `Blob`。

生成的 URL（即其链接）仅在当前文档打开的状态下才有效。它允许引用 `<img>`、`<a>` 中的 `Blob`，以及基本上任何其他期望 URL 的对象。

不过它有个副作用。虽然这里有 `Blob` 的映射，但 `Blob` 本身只保存在内存中的。浏览器无法释放它。

在文档退出时（unload），该映射会被自动清除，因此 `Blob` 也相应被释放了。但是，如果应用程序寿命很长，那这个释放就不会很快发生
**因此，如果我们创建一个 URL，那么即使我们不再需要该 `Blob` 了，它也会被挂在内存中。**

`URL.revokeObjectURL(url)` 从内部映射中移除引用，因此允许 `Blob` 被删除（如果没有其他引用的话），并释放内存。

# Blob转换为base64

[“data-url”](https://developer.mozilla.org/zh/docs/Web/http/Data_URIs) 的形式为 `data:[<mediatype>][;base64],<data>`。我们可以在任何地方使用这种 url，和使用“常规” url 一样。

我们使用内建的 `FileReader` 对象来将 `Blob` 转换为 base64。它可以将 `Blob` 中的数据读取为多种格式。在[下一章](https://zh.javascript.info/file) 我们将更深入地介绍它。



# Image转换为blob


我们可以创建一个图像（image）的、图像的一部分、或者甚至创建一个页面截图的 `Blob`。这样方便将其上传至其他地方。

图像操作是通过 `<canvas>` 元素来实现的：

1. 使用 [canvas.drawImage](https://developer.mozilla.org/zh/docs/Web/api/CanvasRenderingContext2D/drawImage) 在 canvas 上绘制图像（或图像的一部分）。
2. 调用 canvas 方法 [.toBlob(callback, format, quality)](https://developer.mozilla.org/zh/docs/Web/api/HTMLCanvasElement/toBlob) 创建一个 `Blob`，并在创建完成后使用其运行 `callback`

