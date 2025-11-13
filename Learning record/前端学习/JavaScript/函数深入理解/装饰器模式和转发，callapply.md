---
aliases:
  - 装饰器模式和转发，call/apply
---
# 透明缓存 

```
function slow(x) {
  // 这里可能会有重负载的 CPU 密集型工作
  alert(`Called with ${x}`);
  return x;
}

function cachingDecorator(func) {
  let cache = new Map();

  return function(x) {
    if (cache.has(x)) { // 如果缓存中有对应的结果
      return cache.get(x); // 从缓存中读取结果
    }

    let result = func(x); // 否则就调用 func

    cache.set(x, result); // 然后将结果缓存（记住）下来
    return result;
  };
}

slow = cachingDecorator(slow);

alert( slow(1) ); // slow(1) 被缓存下来了，并返回结果
alert( "Again: " + slow(1) ); // 返回缓存中的 slow(1) 的结果

alert( slow(2) ); // slow(2) 被缓存下来了，并返回结果
alert( "Again: " + slow(2) ); // 返回缓存中的 slow(2) 的结果
```

以上的外层的函数相当于缓存了这个内存函数传递了结果，这个map变量不会消失，因为此内存函数调被创建了，他的词法环境中有一个变量绑定了此词法环境。



# func.call设定上下文 

```
func.call(obj,arg1...argn)；
```
主要作用：将函数中的this指针绑定到对象

## func.apply

```
func.apply(obj,arr);
```

与func.call的功能基本一致，主要区别在于其接受的是参数数组这里的arr和call中的`...args`一样




## 对于多值的处理 

如果函数有多个参数的话，这样外面可以依据哈希表的原理来，将多个参数交给hash函数进行处理，得到哈希值，之后再绑定即可。



## arguments

本身相当于一个类数组对象，他记录着函数所传入的所有的参数。当请注意，他是一个类数组，数组的一些方法不能直接使用。
我们可以进行这样的转换
Array.from将其转换为数组再直接应用就行。

# 节流器包装器的实现 
节流装饰器的本质是 “基于高阶函数的函数增强工具”——它通过包装目标函数
```
fuction throttle(fun,ms){
	 let isThrottle = false;//判断是否在冷却，true为在冷却
	 let saverArgs，saverThis；
	 function wrapper(){
		if(isThrottle){
			savedArgs = arguments;
			saverThis = this;
			return;
		}
		isThrottled = true;
		func.apply(this,arguments);
		setTimeout(function{
			isThrottled = false ;
			if(savedArgs){
				wrapper.apply(savedThis,savedArgs);
				savedArgs=savedThis=null;
			}
		},ms);
		return wrapper;
	 }
}

```


# 防抖装饰器 
防抖的本质就是只执行最后一次操作


```
function debounce(func,ms){
	let timeout;
	return function(){
		clearTimeout(timeout);
		timeout = setTimeout(() => func.apply(this,arguments),ms)
	}

}
```