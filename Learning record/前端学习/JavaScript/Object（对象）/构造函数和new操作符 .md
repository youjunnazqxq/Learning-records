# 构造函数 

构造函数与常规函数类似，不过有两个约定

- 他们的命名以大写字母开头
- 他们只能由“new”操作符来执行

实例：

```
function User(name){
	this.name=name;
	this.isAdmin=false;
}
let user = new User("Jack");
```

当一个函数被使用new来执行的时候，有以下步骤：
-  一个新的空对象被分配给this
- 函数体执行。修改this，为其添加属性
- 返回this的值

# 构造器的return语句

规则：
-  如果return返回的是一个对象，则返回这个对象，而不是this
- 如果返回的是一个原始类型，则忽略

# 实际背后的逻辑

当使用`let user = new User("jack");`后，函数中的this会绑定到创建的这个对象`user`中，