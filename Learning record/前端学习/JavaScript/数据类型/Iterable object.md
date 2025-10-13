
# Symbol.iteraror

这是一个返回迭代器的方法，属于一个内建的symbol

例如：
```
let range = {
	from: 1,
	to: 5,
};
range[Symbol.iterator] = function(){
	return {
	current: this.from,
	last: this.to,
		next(){
		if(this.current <= this.last)｛
		return {done: false,value:this.current++};
		}else{
		return {done: true}};
	}

}
```

- 当for..of循环启动的时候，它会自动调用我们提供的方法来找到一个`iterator`
- 当for..of循环喜欢获得以下一个数值的时候他会调用next（）方法，
- next（）方法的返回结果必须是｛done：Boolean,value: any｝
- 当done= true的时候，循环结束，否则value是下一个值。

# Array.from
```
let array = Array.from(arrayLike);
```
在 `(*)` 行的 `Array.from` 方法接受对象，检查它是一个可迭代对象或类数组对象，然后创建一个新数组，并将该对象的所有元素复制到这个新数组