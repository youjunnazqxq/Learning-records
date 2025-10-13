# [[list]]

## Q1

class Link:
    """一个链表。"""
    empty = ()  # 代表空链表

    def __init__(self, first, rest=empty):
        # 断言 rest 必须是 Link.empty 或者 Link 的一个实例
        assert rest is Link.empty or isinstance(rest, Link), "rest 必须是 Link 实例或 Link.empty"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty: # 修正：原版是 if self.rest: 这在Link.empty是()时为True
            rest_repr = ''
        else:
            rest_repr = ', ' + repr(self.rest)
        return f'Link({repr(self.first)}{rest_repr})'

    # __str__ 方法的定义如之前所示，但对于这些片段的直接输出，主要依赖 __repr__ 或值的直接表示。


Python

```
>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
```

**输出**:

```
1
```

- `link = Link(1)` 创建 `link` 为 `Link(1, Link.empty)`。
- `link.rest = link` 使 `link` 的 `rest` 指向 `link` 本身，形成一个循环链表：`link` 指向 `Link(1, points_to_itself)`。
- `link.rest` 是 `link`。
- `link.rest.rest` 也是 `link`。
- 无论多少个 `.rest`，结果都是 `link` 本身。
- 所以 `link.rest.rest.rest.rest.first` 等同于 `link.first`，即 `1`



## Q2
```
##递归版本
def convert_link(link):
	if link is link.empty:
		return []
	else:
		return [link.first]+convert_link(link.rest)


##循环版本
def convert_link(link):
	t=[]
	while(link is not link.empty):
		t+=[link.first]
		link=link.rest	
	return t
def convert_link(link):
	if link is link.empty:
		return []
	if type(link.first) == link:
		return convert_link(link.first)+convert_link(link.rest)
	return [link.first]+ convert_link(link.rest)
```


## Q3

```
def duplicate_link(link, val):
	if link is link.empyt:
		return 
	if link.first==val:
		link.rest=link(val,link.rest)
		duplicate_link(link.rest.rest, val)
	else:
	     duplicate_link(link.rest, val)
```


## Q4

```
def multiply_lnks(lst_of_lnks):
	sum=1
	for i in lst_of_lnks:
		if i is link.empty:
			return link.empty
		sum*=i.first
	lst_of_lnks=[i.rest for i in lst_of_lnks ]
	return link(sum,multiply_lnks(lst_of_lnks))
		
	

```


## Q5

```
def flip_two(s):
	if s is link.empty or s.rest is link.empty:
		return 
	s.first,s.rest.first=s.rest.first,s.first
	flip_two(s.rest.rest)
```

## [[Efficiency]]


好的，这是图片内容的中文翻译：

---

## 效率 (Efficiency)

当我们讨论一个函数的效率时，我们通常关注以下方面：随着输入规模的增长，函数的运行时间是如何变化的？以及我们所说的“运行时间”指的是什么？

**示例 1**: `square(1)` 需要一次原始操作：乘法。`square(100)` 也同样需要一次。无论我们给 `square` 函数传入什么输入 `n`，它总是执行**恒定**数量的操作 (1)。换句话说，这个函数的运行时复杂度是 O(1)。

为了说明，请看下表：

|   |   |   |   |
|---|---|---|---|
|**输入**|**函数调用**|**返回值**|**操作次数**|
|1|square(1)|1*1|1|
|2|square(2)|2*2|1|
|...|...|...|...|
|100|square(100)|100*100|1|
|...|...|...|...|
|n|square(n)|n*n|1|

**示例 2**: `factorial(1)` 需要一次乘法，但 `factorial(100)` 需要 100 次乘法。随着输入规模 `n` 的增加，运行时间（乘法运算的次数）与输入**线性相关**地增加。换句话说，这个函数的运行时复杂度是 O(n)。

为了说明，请看下表：

|   |   |   |   |
|---|---|---|---|
|**输入**|**函数调用**|**返回值**|**操作次数**|
|1|factorial(1)|1*1|1|
|2|factorial(2)|2*1*1|2|
|...|...|...|...|
|100|factorial(100)|100*99*... *1*1|100|
|...|...|...|...|
|n|factorial(n)|n*(n-1)*... *1*1|n|

**示例 3**: 考虑以下函数定义：`def bar(n): for a in range(n): for b in range(n): print(a,b)`。

`bar(1)` 需要 1 次打印语句，而 `bar(100)` 需要 `100*100 = 10000` 次打印语句（每次内部循环都会执行打印）。因此，运行时间与输入成**二次方**比例增长。换句话说，这个函数的运行时复杂度是 O(n2)。

|   |   |   |
|---|---|---|
|**输入**|**函数调用**|**操作次数 (打印)**|
|1|bar(1)|1|
|2|bar(2)|4|
|...|...|...|
|100|bar(100)|10000|
|...|...|...|
|n|bar(n)|n2|

---

## Q7

```
def find_paths(t, entry):
	paths=[]
	if t.label== entry:
		return paths.append([t.label])
	for b in t.branches:
		for path in find_pasths(b,entry)
			path.append([t.label]+path)
		return paths
```