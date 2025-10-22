
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

![[Screenshot_20251022_192054_mark.via.png]]