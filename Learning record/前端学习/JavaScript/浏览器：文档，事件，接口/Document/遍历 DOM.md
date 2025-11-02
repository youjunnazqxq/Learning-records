
对 DOM 的所有操作都是以 `document` 对象开始。它是 DOM 的主“入口点”。从它我们可以访问任何节点。
![[Pasted image 20251029222336.png]]

## 解析机制 
**HTML 的解析（构建 DOM 树）和 JavaScript 的执行是“同步”且“互相阻塞”的。**

- 浏览器按顺序解析 HTML。
    
- 遇到 `<script>`（默认情况下），**必须先执行完 JS**，才能继续解析后面的 HTML。
    
- 因此，在特定 `<script>` 中能访问到哪些 DOM 元素，**完全取决于那个 `<script>` 标签之前，有多少 HTML 已经被浏览器解析了**。

# 子节点：childNodes，firstChild，lastChild

- **子节点（或者叫作子）** —— 对应的是直系的子元素。换句话说，它们被完全嵌套在给定的元素中。例如，`<head>` 和 `<body>` 就是 `<html>` 元素的子元素。
- **子孙元素** —— 嵌套在给定元素中的所有元素，包括子元素，以及子元素的子元素等。

**`hildNodes` 集合列出了所有子节点，包括文本节点。**
**`firstChild` 和 `lastChild` 属性是访问第一个和最后一个子元素的快捷方式。**

## **`children`**：

- 返回一个 `HTMLCollection`。
    
- 只包含**元素节点** (Element nodes)，比如 `<h1>`, `<p>`, `<div>`。
    
- 它会**自动忽略**文本节点（比如空格、换行）和注释节点。


## **`childNodes`**：

- 返回一个 `NodeList`。
    
- 包含**所有类型**的子节点，包括**元素节点**、**文本节点** (Text nodes) 和**注释节点** (Comment nodes) 等。

>[!note]
>一般来说，我们在写html的时候都会换行，所以first和last都会访问到第一个文本节点，就显得没有作用，所以我们才会泳只包含元素节点的来使用
>、
>





# DOM集合 

一个 **集合** —— 一个类数组的可迭代对象。

- 我们可以用`for ...of`来迭代其,因为其是可迭代的有（Symbol.iterator）;
-  无法使用数组的方法，因为它不是一个数组
- 
不要使用 `for..in` 来遍历集合,可以使用 `for..of` 对集合进行迭代。但有时候人们会尝试使用 `for..in` 来迭代集合。

请不要这么做。`for..in` 循环遍历的是所有可枚举的（enumerable）属性
DOM 集合是只读的

DOM 集合，甚至可以说本章中列出的 **所有** 导航（navigation）属性都是只读的。

我们不能通过类似 `childNodes[i] = ...` 的操作来替换一个子节点。

修改子节点需要使用其它方法。我们将会在下一章中看到它们。

## DOM 集合是实时的

除小部分例外，几乎所有的 DOM 集合都是 **实时** 的。换句话说，它们反映了 DOM 的当前状态。

如果我们保留一个对 `elem.childNodes` 的引用，然后向 DOM 中添加/移除节点，那么这些节点的更新会自动出现在集合中。

## 不要使用 `for..in` 来遍历集合

可以使用 `for..of` 对集合进行迭代。但有时候人们会尝试使用 `for..in` 来迭代集合。

请不要这么做。`for..in` 循环遍历的是所有可枚举的（enumerable）属性。集合还有一些“额外的”很少被用到的属性，通常这些属性也是我们不期望得到的：

```markup
<body>
<script>
  // 显示 0，1，length，item，values 及其他。
  for (let prop in document.body.childNodes) alert(prop);
</script>
</body>
```

# 兄弟节点 
下一个兄弟节点在 `nextSibling` 属性中，上一个是在 `previousSibling` 属性中。



