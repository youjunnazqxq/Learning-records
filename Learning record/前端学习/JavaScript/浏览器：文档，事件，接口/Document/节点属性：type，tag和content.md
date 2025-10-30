# DOM 节点类 
每个 DOM 节点都属于相应的内建类。
层次结构（hierarchy）的根节点是 [EventTarget](https://dom.spec.whatwg.org/#eventtarget)，[Node](https://dom.spec.whatwg.org/#interface-node) 继承自它，其他 DOM 节点继承自 Node。

- [EventTarget](https://dom.spec.whatwg.org/#eventtarget) —— 是一切的根“抽象（abstract）”类。
    
    该类的对象从未被创建。它作为一个基础，以便让所有 DOM 节点都支持所谓的“事件（event）”，我们会在之后学习它。
    
- [Node](http://dom.spec.whatwg.org/#interface-node) —— 也是一个“抽象”类，充当 DOM 节点的基础。
    
    它提供了树的核心功能：`parentNode`，`nextSibling`，`childNodes` 等（它们都是 getter）。`Node` 类的对象从未被创建。但是还有一些继承自它的其他类（因此继承了 `Node` 的功能）。
    
- [Document](https://dom.spec.whatwg.org/#interface-document) 由于历史原因通常被 `HTMLDocument` 继承（尽管最新的规范没有规定）—— 是一个整体的文档。
    
    全局变量 `document` 就是属于这个类。它作为 DOM 的入口。
    
- [CharacterData](https://dom.spec.whatwg.org/#interface-characterdata) —— 一个“抽象”类，被下述类继承：
    
    - [Text](https://dom.spec.whatwg.org/#interface-text) —— 对应于元素内部文本的类，例如 `<p>Hello</p>` 中的 `Hello`。
    - [Comment](https://dom.spec.whatwg.org/#interface-comment) —— 注释类。它们不会被展示出来，但每个注释都会成为 DOM 中的一员。
- [Element](http://dom.spec.whatwg.org/#interface-element) —— 是 DOM 元素的基础类。
    
    它提供了元素级导航（navigation），如 `nextElementSibling`，`children`，以及搜索方法，如 `getElementsByTagName` 和 `querySelector`。
    
    浏览器不仅支持 HTML，还支持 XML 和 SVG。因此，`Element` 类充当的是更具体的类的基础：`SVGElement`，`XMLElement`（我们在这里不需要它）和 `HTMLElement`。
    
- 最后，[HTMLElement](https://html.spec.whatwg.org/multipage/dom.html#htmlelement) —— 是所有 HTML 元素的基础类。我们大部分时候都会用到它。


>[!note ]
>大多数浏览器在其开发者工具中都支持这两个命令：`console.log` 和 `console.dir`。它们将它们的参数输出到控制台中。对于 JavaScript 对象，这些命令通常做的是相同的事。
>
>- `console.log(elem)` 显示元素的 DOM 树。
>- `console.dir(elem)` 将元素显示为 DOM 对象，非常适合探索其属性。



# nodeType 属性 

`nodeType` 属性提供了另一种“过时的”用来获取 DOM 节点类型的方法。

它有一个数值型值（numeric value）：

- 对于元素节点 `elem.nodeType == 1`，
- 对于文本节点 `elem.nodeType == 3`，
- 对于 document 对象 `elem.nodeType == 9`，
- 在 [规范](https://dom.spec.whatwg.org/#node) 中还有一些其他值。

# 标签：nodename和tagname

- `tagName` 属性仅适用于 `Element` 节点。
- `nodeName` 是为任意 `Node` 定义的：
    - 对于元素，它的意义与 `tagName` 相同。
    - 对于其他节点类型（text，comment 等），它拥有一个对应节点类型的字符串。
在HTML下，tagName总是大写的。

# innerHTML： 内容 
读取当前区域的所有DOM对象，并将其转化为字符串，
同时，我们也可以对其进行替换，同样以字符串的形式。

如果 `innerHTML` 将一个 `<script>` 标签插入到 document 中 —— 它会成为 HTML 的一部分，但是不会执行。
### “innerhtml+= 会进行完全重写”


1. 先移除旧内容：浏览器会先把元素原来的所有 HTML 内容（包括子节点、文本等）全部删除。
​
2. 再写入“新旧结合的新内容”：把原来的  innerHTML  字符串和新添加的字符串拼接起来，然后作为新的  innerHTML  重新解析并渲染。






# outerHTML：元素的完整HTML


`outerHTML` 属性包含了元素的完整 HTML。就像 `innerHTML` 加上元素本身一样。

outerHTML替换的时候会发生如下过程
- 原有内容从document中删除
- 另一个HTML片段被插入到其位置
- 原先引用的值仍然有其旧值不变化



# nodvalue/date ：文本节点内容 


文本节点，具有它们的对应项：`nodeValue` 和 `data` 属性。这两者在实际使用中几乎相同，只有细微规范上的差异。因此，我们将使用 `data`



# textContent ：纯文本 

返回一个元素中的文本，无论是否被标签包裹 

**写入 `textContent` 要有用得多，因为它允许以“安全方式”写入文本。**




# hidden 属性 

“hidden” 特性（attribute）和 DOM 属性（property）指定元素是否可见。

“hidden” 特性（attribute）和 DOM 属性（property）指定元素是否可见。
