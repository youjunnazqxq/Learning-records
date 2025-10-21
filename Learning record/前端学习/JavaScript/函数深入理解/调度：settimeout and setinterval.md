# setTimeout

```
let timerId = setTimeout(fun,[],[],...)
```
我们可以通过后面传递参数来给函数传递参数，但更为常用的是我们在fun那直接再嵌套一个箭头函数，例如
```
let timerId = setTimeout( () => func(...arg),ms);
```
这样使用最为常见。




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


# 嵌套调用

## setTimeout

```
let timerId = setTimeout(function tick(){
	timerId = setTimeout(tick,2000)
},2000);
```






# setTimeout的运行实际


## js的运行环境

JavaScript 的运行环境（如浏览器）使用“事件循环”模型来管理异步任务。这个过程涉及四个关键部分：

1. **调用栈 (Call Stack)**：JS 引擎**真正执行**同步代码的地方。
    
2. **Web API (浏览器 API)**：浏览器的功能，如 `setTimeout` 的**计时器**、DOM 事件等。
    
3. **回调队列 (Callback Queue)**：一个“排队区”，存放所有_已到时间_、_等待被执行_的回调函数。
    
4. **事件循环 (Event Loop)**：一个“协调员”，不断检查“调用栈”是否为空。

## 执行流程 


- **1. 分派任务 (Dispatch)**
    
    - JS 引擎在**调用栈**上遇到 `setTimeout(func, ms)`。
        
    - JS 引擎不会自己计时，它把 `func` 和 `ms` 交给**浏览器 API (Web API)**，说：“请在 `ms` 毫秒后叫醒这个 `func`”。
        
    - `setTimeout` 函数本身执行完毕，从调用栈弹出。
        
    - JS 引擎**立即继续**执行栈中的下一行代码（比如 `console.log('同步代码')`）。
        
- **2. 后台计时 (Timer)**
    
    - **Web API** 在后台**独立**进行 `ms` 毫秒的倒计时。
        
    - 这与 JS 引擎的主线程**同时**发生，互不干扰。
        
- **3. 入队等待 (Enqueue)**
    
    - `ms` 毫秒后，Web API 的倒计时结束。
        
    - Web API 将 `func`（回调函数）**放入“回调队列 (Callback Queue)”** 中，让它开始排队。
        
    - **注意：** 此时 `func` 只是_获得了排队资格_，**不代表**立即执行。
        
- **4. 出队执行 (Execute)**
    
    - **事件循环 (Event Loop)** 在一旁持续不断地检查：“**调用栈**是否空了？”
        
    - **一旦**调用栈中所有的同步代码都执行完毕（栈空了），事件循环就会去“回调队列”的队首取出一个任务（即 `func`）。
        
    - 事件循环将 `func` **推入“调用栈”**。
        
    - JS 引擎在调用栈中执行 `func`。