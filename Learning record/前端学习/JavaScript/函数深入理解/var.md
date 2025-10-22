
# var没有块级作用域

用var声明的变量，不是函数作用域就是全局作用域。
```
if(true){
	var test = true ;
}

alert(test);
```


# var 允许重新声明 

```
var user = "Pete"
var user = "John"

alert(user);
```

# var 声明的变量，可以放在其声明语句前被使用

这种行为被称为“提升”，所有的`var`变量都被提升到了函数的顶部

## 声明会被提升，但是赋值不会


# IIFE

函数表达式：