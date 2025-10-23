# try...catch语法

```
try {
	
} catch(err){

}
```

1. 首先，执行 `try {...}` 中的代码。
2. 如果这里没有错误，则忽略 `catch (err)`：执行到 `try` 的末尾并跳过 `catch` 继续执行。
3. 如果这里出现错误，则 `try` 执行停止，控制流转向 `catch (err)` 的开头。变量 `err`（我们可以使用任何名称）将包含一个 error 对象，该对象包含了所发生事件的详细信息。

## try...catch 
和类似于时间器的时候，catch并不会抛出异常，因为当他执行的时候，代码早跑完了，如何解决，在内部使用这个。


# Error对象 
对于所有内建的 error，error 对象具有两个主要属性：

`name`

Error 名称。例如，对于一个未定义的变量，名称是 `"ReferenceError"`。

`message`

关于 error 的详细文字描述。

还有其他非标准的属性在大多数环境中可用。其中被最广泛使用和支持的是：

`stack`

当前的调用栈：用于调试目的的一个字符串，其中包含有关导致 error 的嵌套调用序列的信息。
## 创建error对象

```
let error = new Error("message");
```

# throw

当我们想要自定义错误的时候，可以这样在try中尝试抛出错误：
```
if(!user.name){
	throw new Error(错误)；
}
```


# finally

