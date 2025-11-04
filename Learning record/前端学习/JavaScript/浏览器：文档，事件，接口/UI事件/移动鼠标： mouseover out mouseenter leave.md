
简单来说：每次鼠标触发  mouseover  或  mouseout  事件时， relatedTarget  都会根据鼠标的移动方向（从哪个元素来、到哪个元素去）重新赋值。只有当鼠标再次移动时，它才会跟着变化~

[[]()]()
对于 `mouseover`：

- `event.target` —— 是鼠标移过的那个元素。
- `event.relatedTarget` —— 是鼠标来自的那个元素（`relatedTarget` → `target`）。

`mouseout` 则与之相反：

- `event.target` —— 是鼠标离开的元素。
- `event.relatedTarget` —— 是鼠标移动到的，当前指针位置下的元素（`target` → `relatedTarget`）。


>[!relatedTarget可以为null]
>relatertarget 的属性可以为null
>这是正常现象，仅仅是意味着鼠标不是来自另一个元素，而是来自窗口之外。或者它离开了窗口。
》
当我们在代码中使用 `event.relatedTarget` 时，我们应该牢记这种可能性。如果我们访问 `event.relatedTarget.tagName`，那么就会出现错误


# 跳过元素 


​当鼠标移动时，就会触发 `mousemove` 事件。但这并不意味着每个像素都会导致一个事件。

浏览器会一直检查鼠标的位置。如果发现了变化，就会触发事件。

这意味着，如果访问者非常快地移动鼠标，那么某些 DOM 元素就可能被跳过
![[Screenshot_20251104_090049_md.obsidian.png]]




# 当移动到一个子元素时 mouseout


当鼠标指针从 `#parent` 元素移动到 `#child` 时，会在父元素上触发两个处理程序：`mouseout` 和 `mouseover`：

**如果我们不检查处理程序中的 `event.target`，那么似乎鼠标指针离开了 `#parent` 元素，然后立即回到了它上面。**

但是事实并非如此！鼠标指针仍然位于父元素上，它只是更深入地移入了子元素。

如果离开父元素时有一些行为（action），例如一个动画在 `parent.onmouseout` 中运行，当鼠标指针深入 `#parent` 时，我们并不希望发生这种行为。

为了避免它，我们可以在处理程序中检查 `relatedTarget`，如果鼠标指针仍在元素内，则忽略此类事件。

# 事件：mouseenter和mouselaeve

事件 `mouseenter/mouseleave` 类似于 `mouseover/mouseout`。它们在鼠标指针进入/离开元素时触发。

但是有两个重要的区别：

1. 元素内部与后代之间的转换不会产生影响。
2. 事件 `mouseenter/mouseleave` 不会冒泡。

# 事件委托 
