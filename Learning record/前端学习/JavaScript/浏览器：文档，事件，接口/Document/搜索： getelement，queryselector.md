
# document.getElementByld（‘ID’） 或者只用id（查找ID的时候最快）

```
	let elem = document.getElementById('elem');
	elem.style.background = 'red';
```

# querySelectorAll（'CSS选择器'）（查询-选择-全部/最为通用）

到目前为止，最通用的方法是 `elem.querySelectorAll(css)`，它返回 `elem` 中与给定 CSS 选择器匹配的所有元素。

```
let elements = document.querySelectorAll('ul > li:last-chi');
```

# querySelector（同上）
`elem.querySelector(css)` 调用会返回给定 CSS 选择器的第一个元素。
换句话说，结果与 `elem.querySelectorAll(css)[0]` 相同，但是后者会查找 **所有** 元素，并从中选取一个，而 `elem.querySelector` 只会查找一个。因此它在速度上更快，并且写起来更短。

其返回的是一个Nodelist，节点列表，类似于伪数组。

# matches

elem.matches(css) 不会查找任何内容，它只会检查 `elem` 是否与给定的 CSS 选择器匹配。它返回 `true` 或 `false`。


# closest

元素的祖先（ancestor）是：父级，父级的父级，它的父级等。祖先们
`elem.closest(css)` 方法会查找与 CSS 选择器匹配的最近的祖先。`elem` 自己也会被搜索。一起组成了从元素到顶端的父级链。

# getElementsBy

- `elem.getElementsByTagName(tag)` 查找具有给定标签的元素，并返回它们的集合。`tag` 参数也可以是对于“任何标签”的星号 `"*"`。
- `elem.getElementsByClassName(className)` 返回具有给定CSS类的元素。
- `document.getElementsByName(name)` 返回在文档范围内具有给定 `name` 特性的元素。很少使用

# 实时的集合 
所有的 `"getElementsBy*"` 方法都会返回一个 **实时的（live）** 集合。这样的集合始终反映的是文档的当前状态，并且在文档发生更改时会“自动更新”。
相反，`querySelectorAll` 返回的是一个 **静态的** 集合。就像元素的固定数组。

|方法名|搜索方式|可以在元素上调用？|实时的？|
|---|---|---|---|
|`querySelector`|CSS-selector|✔|-|
|`querySelectorAll`|CSS-selector|✔|-|
|`getElementById`|`id`|-|-|
|`getElementsByName`|`name`|-|✔|
|`getElementsByTagName`|tag or `'*'`|✔|✔|
|`getElementsByClassName`|class|✔|✔|

