# settimeout

```
let timerId = setTimeout(fun,[],[],...)
```

`func|code`

想要执行的函数或代码字符串。 一般传入的都是函数。由于某些历史原因，支持传入代码字符串，但是不建议这样做。

`delay`

执行前的延时，以毫秒为单位（1000 毫秒 = 1 秒），默认值是 0；

`arg1`，`arg2`…

要传入被执行函数（或代码字符串）的参数列表（IE9 以下不支持


# 用cleartimeout来取消调度

```
clearTimeout(timerID);
```

# setInterval

语法与settimeout类似，但是他说每隔一段时间就勋兴一次


```
let timerId = setInerval(()=>alert('tikc'),2000);

setTimeout(()=>clearInterval(timerId),5000);
```
