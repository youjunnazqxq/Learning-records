基本语法：

```
class User{
	constructor(name){
		this.name = name;
	}
	sayHi(){
		alert(this.name);
	}

}

let user = new User("John");
user.sayHi();
```

# class本质

class本质是一个构造函数函数，当创建它的时候会自动调用其constructor属性，用其方法是时候也是会自动沿着原型链来寻找方法。



# 类表达式 

```
let User = class MyClass{
	sayHi(){
		alert("Hello");
	}
};
```



# class 字段


我们可以这样

```
class User{
	name = "John";
}

let user = new User();
alert(user.name);John
alert(User.prototype.name);//undefined
```
类字段的重要区别在于，它们会被挂在实例对象上，而非 `User.prototype` 上：


# 使用类字段制作的绑定方法

与之类似，类方法中的this指针是运行时候绑定的，会丢失this，class提供了一个特殊的方法

```
class Button {
	constructor(value){
		this.name = value;
	}
	click = =>{
		alert(this.value);//就是外面嵌套了一层函数，不是直接调用函数，而是通过实例调用罢了
	}
}
```



