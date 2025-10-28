# 基本语法
```
funcion* generateSequence（）{
	yield 1;
	return 3;
}
```

generator函数会返回一个迭代器，
其通过方法`next()`来执行到最近的next（），然后函数停止运行，并讲yield的值返回。
`next()` 的结果始终是一个具有两个属性的对象：

- `value`: 产出的（yielded）的值。
- `done`: 如果 generator 函数已执行完成则为 `true`，否则为 `false`。

- 当 Generator 函数执行到  return  语句时，后续调用  next()  会返回  {value: 返回值, done: true} ，其中  done: true  明确表示迭代器已结束。

# 迭代

我们可以移动`for of`语句来运行这个函数，当函数运行到return语句的时候，done：true判定，然后不会执行value的值。

generator的迭代写法

```
let range = {
	from: 1,
	to: 5;
	*[Symbol.iterator](){
		for(let value = this.from;value <= this.ture ;value++){
			yield value;
		}
	}

}
```

# generator组合 

在迭代器中，如果我们想要在内部的迭代器再启用一次，那么可以用到`yield*`语法，这个指令将委托到另一个迭代器。然后将值传递给外部。如果不用的话，返回的只是一个迭代器而已。



# yield可以接受外部的值

```
function* gen(){
	let result = yield "2 + 2 ="
	alert(result);

}
 let generator = gen();
 let question = generator.next().value;
 generator.next(4);
```


## generator.throw

要向 `yield` 传递一个 error，我们应该调用 `generator.throw(err)`。在这种情况下，`err` 将被抛到对应的 `yield` 所在的那一行。

## generator.return 
