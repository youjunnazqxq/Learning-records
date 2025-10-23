
# instanceof 操作符

基本语法：
```
obj instanceof Class
```
属于返回true，不属于返回false。


# 使用Object.prototype.toString方法来展示类型

```
let bojectToString = Object.prototype.toString;

let arr = [];

alert(pbjectToString.call(arr));//[object Array];
```
```
let user = {
	[Symbol.toStringTag]: "User"
};

alert({}.toString.call(user));
```

对于正常的类型检查来说我们使用`{}.toString.call(obj)`
即可检查他的类型，其中我们也可以自定义类型，例如：
```
let user = {
	[Symbol.toStringTag] = "User"
};
	alert({}.toString.call(user));//[object User];
```


