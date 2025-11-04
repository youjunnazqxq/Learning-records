
# Keydown和keyup

当一个按键被按下时，会触发 `keydown` 事件，而当按键被释放时，会触发 `keyup` 事件。

#### event.code && event.key

例如，同一个按键 Z，可以与或不与 `Shift` 一起按下。我们会得到两个不同的字符：小写的 `z` 和大写的 `Z`。

`event.key` 正是这个字符，并且它将是不同的。但是，`event.code` 是相同的：

|Key|`event.key`|`event.code`|
|---|---|---|
|Z|`z`（小写）|`KeyZ`|
|Shift+Z|`Z`（大写）|`KeyZ`|
#### 大小写敏感：`"KeyZ"`，不是 `"keyZ 
这是显而易见的，但人们仍会搞错。

请规避错误类型：它是 `KeyZ`，而不是 `keyZ`。像 `event.code=="keyZ"` 这样的检查不起作用：`"Key"` 的首字母必须大写。

|Key|`event.key`|`event.code`|
|---|---|---|
|F1|`F1`|`F1`|
|Backspace|`Backspace`|`Backspace`|
|Shift|`Shift`|`ShiftRight` 或 `ShiftLeft`|

event.key: 实际输入的内容

event.code : 键盘敲打的位置的内容


# 自动重复 

如果按下一个键足够长的时间，它就会开始“自动重复”：`keydown` 会被一次又一次地触发，然后当按键被释放时，我们最终会得到 `keyup`。因此，有很多 `keydown` 却只有一个 `keyup` 是很正常的。

对于由自动重复触发的事件，`event` 对象的 `event.repeat` 属性被设置为 `true`。


# 默认行为 

