
当用户点击某个元素或使用键盘上的 Tab 键选中时，该元素将会获得聚焦（focus）。还有一个 HTML 特性（attribute）`autofocus` 可以让焦点在网页加载时默认落在一个元素上，此外还有其它途径可以获得焦点

聚焦到一个元素通常意味着：“准备在此处接受数据”，所以，这正是我们可以运行代码以初始化所需功能的时刻。

失去焦点的时刻（“blur”）可能更为重要。它可能发生在用户点击页面的其它地方，或者按下 Tab 键跳转到下一个表单字段，亦或是其它途径的时候。

失去焦点通常意味着：“数据已经输入完成”，所以我们可以运行代码来检查它，甚至可以将其保存到服务器上，或进行其他操作。

当处理焦点事件时，有一些重要的特性。我们将尽力把这些内容介绍完整。


# focus/blur 事件

当元素聚焦时，会触发 `focus` 事件，当元素失去焦点时，会触发 `blur` 事件.
```
<style>
  .invalid { border-color: red; }
  #error { color: red }
</style>

Your email please: <input type="email" id="input">
<div id="error"></div>

<script>
input.onblur = function() {
  if (!input.value.includes('@')) { // not email
    input.classList.add('invalid');
    error.innerHTML = 'Please enter a correct email.';
  }
};

input.onfocus = function() {
  if (this.classList.contains('invalid')) {
    // 移除 "error" 指示，因为用户想要重新输入一些内容
    this.classList.remove('invalid');
    error.innerHTML = "";
  }
};
</script>

```



# focus/blur 方法 

`elem.focus()` 和 `elem.blur()` 方法可以设置和移除元素上的焦点。

如果我们在 `input` 中输入一些内容，然后尝试使用 Tab 键或点击远离 `<input>` 的位置，那么 `onblur` 事件处理程序会把焦点重新设置到这个 `input` 字段上。

请注意，我们无法通过在 `onblur` 事件处理程序中调用 `event.preventDefault()` 来“阻止失去焦点”，因为 `onblur` 事件处理程序是在元素失去焦点 **之后** 运行的。

但在实际中，在实现这样的功能之前应该认真考虑一下，因为我们通常 **应该将报错展示给用户**，但 **不应该阻止用户在填写我们的表单时的进度**。用户可能会想先填写其他表单项。


# 允许在任何元素上聚焦：tabindex

任何具有 `tabindex` 特性的元素，都会变成可聚焦的。该特性的 `value` 是当使用 Tab（或类似的东西）在元素之间进行切换时，元素的顺序号。

也就是说：如果我们有两个元素，第一个具有 `tabindex="1"`，第二个具有 `tabindex="2"`，然后当焦点在第一个元素的时候，按下 Tab 键，会使焦点移动到第二个元素身上。

切换顺序为：从 `1` 开始的具有 `tabindex` 的元素排在前面（按 `tabindex` 顺序），然后是不具有 `tabindex` 的元素（例如常规的 `<input>`）。

不具有 `tabindex` 的元素按文档源顺序（默认顺序）切换。

这里有两个特殊的值：

- `tabindex="0"` 会使该元素被与那些不具有 `tabindex` 的元素放在一起。也就是说，当我们切换元素时，具有 `tabindex="0"` 的元素将排在那些具有 `tabindex ≥ 1` 的元素的后面。
    
    通常，它用于使元素具有焦点，但是保留默认的切换顺序。使元素成为与 `<input>` 一样的表单的一部分。
    
- `tabindex="-1"` 只允许以编程的方式聚焦于元素。Tab 键会忽略这样的元素，但是 `elem.focus()` 有效。

# focus/blur 委托 
`focus` 和 `blur` 事件不会向上冒泡。
[]()