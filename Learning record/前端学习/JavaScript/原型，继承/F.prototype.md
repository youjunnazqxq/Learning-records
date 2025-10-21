基本语法：
```
let animal = {
	eats: true;
};
function Rabbit(name){
	this.name = name;
}
Rabbit.prototype = animal;
let rabbit = new Rabbit("hahah");
```
这里的f为构造函数，后面的是构造函数的属性，其意义在与为构造函数创建的对象绑定他的原型。
主要，这里的隐藏环境的赋值是直接的引用赋值，也就是浅拷贝。也就是说，构造函数中的prototype属性存储着原型的地址，他是将地址传递给了新的对象的隐藏属性
	
# 构造器

每个函数都有 `"prototype"` 属性，即使我们没有提供它。

默认的 `"prototype"` 是一个只有属性 `constructor` 的对象，属性 `constructor` 指向函数自身。

## 手动修复constructor属性

当我们对构造函数的prototype进行赋值的时候，他的constructor就会被覆盖，我们需要手动存储constructor的值。这个constructor的值会存储在新的对象之中。