
基本语法：
`le如果提供了 HTML `form` 元素，它会自动捕获 `form` 元素字段。

`FormData` 的特殊之处在于网络方法（network methods），例如 `fetch` 可以接受一个 `FormData` 对象作为 body。它会被编码并发送出去，带有 `Content-Type: multipart/form-data`。t formData = new FormData([form])`

```
form.Elem.onsubmit = async(e) => {
	e.preventDefault();

	let response = await fetch(url,{
		method: 'POST',
		body: new FormData(formElem)
	});
	let result = await response.json();
	alert(result.message);
}
```

# FromData方法


我们可以使用以下方法修改 `FormData` 中的字段：

- `formData.append(name, value)` —— 添加具有给定 `name` 和 `value` 的表单字段，
- `formData.append(name, blob, fileName)` —— 添加一个字段，就像它是 `<input type="file">`，第三个参数 `fileName` 设置文件名（而不是表单字段名），因为它是用户文件系统中文件的名称，
- `formData.delete(name)` —— 移除带有给定 `name` 的字段，
- `formData.get(name)` —— 获取带有给定 `name` 的字段值，
- `formData.has(name)` —— 如果存在带有给定 `name` 的字段，则返回 `true`，否则返回 `false`。


# 发送带有文件的表单 


表单始终以 `Content-Type: multipart/form-data` 来发送数据，这个编码允许发送文件。因此 `<input type="file">` 字段也能被发送，类似于普通的表单提交。



## 应用
上传一个文件
```
// 假设你有一个 <input type="file" id="fileInput">
const fileInput = document.getElementById('fileInput');
const file = fileInput.files[0]; // 获取用户选择的第一个文件

const formData = new FormData();
// 使用 .append() 手动添加文件
formData.append('avatar', file, 'user-avatar.png'); // (键, 文件对象, [可选的文件名])
formData.append('userId', '12345'); // 也可以同时添加其他文本数据

fetch('/api/upload/avatar', {
  method: 'POST',
  body: formData
  // 注意：此处【不要】设置 Content-Type 头部！
  // fetch 会自动为 FormData 设置正确的 'multipart/form-data' 头部
});
```
上传整个HTML表单

```
const myForm = document.getElementById('profile-form');

myForm.addEventListener('submit', async (e) => {
  e.preventDefault(); // 阻止页面刷新

  // 一键打包表单中的所有数据
  const formData = new FormData(myForm);
  
  // formData 现在包含了表单里所有的 name=value 对
  const response = await fetch('/api/user/update', {
    method: 'POST',
    body: formData
  });

  const result = await response.json();
  alert(result.message);
});
```


