# 方法示例编写 

## 直接在内部编写

```
let user = {
	name： “John”，
	age： 30
	sayHi: function(){
		alert("Hello");
	}
	satHi(){
	
	}//简写
}
```



# 方法中的this对象

例如
```
//接上面的例子 
say(){
	alert(this.name);
}
user.say();
```
在这里,say()方法被调用，this指向的是点之前的实例，这是动态绑定的
这个规则很简单：如果 `obj.f()` 被调用了，则 `this` 在 `f` 函数调用期间是 `obj`。所以在上面的例子中 this 先是 `user`，之后是 `admin`。




 ##  在没有对象下的情况
 >[!note]
 在没有对象的情况下调用：`this == undefined`
>
>```javascript
function sayHi() {
  alert(this);
}
>
>sayHi(); // undefined
>```
在这种情况下，严格模式下的 `this` 值为 `undefined`。如果我们尝试访问 `this.name`，将会报错。
>
在非严格模式的情况下，`this` 将会是 **全局对象**（浏览器中的 `window`，我们稍后会在 [全局对象](https://zh.javascript.info/global-object) 一章中学习它）。这是一个历史行为，`"use strict"` 已经将其修复了。



# 箭头函数的this

箭头函数没有自己的this，他的this取决于外部正常函数的this