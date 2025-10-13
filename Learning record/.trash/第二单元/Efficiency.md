## [Measuring Efficiency][时间复杂度]
```
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1 # 访问并增加属性
        return f(n)
    counted.call_count = 0    # 初始化属性
    return counted
```
对于 count函数来说，这是一个嵌套函数，他返回一个内置函数，当我们执行fib=count(fib)的时候，fib指向counted，而counter中的f函数指向原先的fib，调用fib，返回f（n），而fib.call_count调用这回指向次数（原先所有加的累和）

## [Memoization][记忆化]
```
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
```
对于这个函数来说，当我使用fib=memo（fib）的时候，memo帧内部的f（）指向原先的fib函数地址，当他返回fib（n-1）+fib（n-2）的时候，这里的fib指向的是包装后的fib，所以调用fib（5）的时候，计算多个fib（3）的时候他已经被保存，只会被计算一次
==注意==以上三个函数可以嵌套，无非就是执行的顺序不同罢


## [时间复杂度]

![[Pasted image 20250528173024.png]]

![[Pasted image 20250528173233.png]]

## [space]

空间，一般指的是占用的内存

## [[link]]
对于这样的数据结构来说，当我们执行这样t=s（一个链表）的时候，t只是换个名称，指向的是同一个内存地址，这一点需要注意！
例如

```ef without(s, i):

    """Return a new linked list like s but without the element at index i.

  

    >>> s = Link(3, Link(5, Link(7, Link(9))))

    >>> without(s, 0)

    Link(5, Link(7, Link(9)))

    >>> without(s, 2)

    Link(3, Link(5, Link(9)))

    >>> without(s, 4)           # There is no index 4, so all of s is retained.

    Link(3, Link(5, Link(7, Link(9))))

    >>> without(s, 4) is not s  # Make sure a copy is created

    True

    """

    "*** YOUR CODE HERE ***"

    if s==Link.empty:

        return s

    if i ==0:

        return s.rest

    t=Link(s.first,without(s.reset,i-1))

    return t
```
对于上面的s.rest来说，还是指向一个相同的内存地址
