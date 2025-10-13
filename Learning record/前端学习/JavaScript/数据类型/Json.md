在js中，我们可以将文件转化为JSON格式，以便进行传输。

# JSON转化
可以用 JSON.stringify()进行转化

```
const data = {
  normal: "正常值",
  undefinedProp: undefined,      // 被忽略
  functionProp: function() {},   // 被忽略
  date: new Date(),              // 转为字符串 "2023-...T..."
  regex: /abc/g,                 // 转为 {}
  nullProp: null,               // 保留为 null
  arrayWithUndefined: [1, undefined, 3] // [1, null, 3]
};

console.log(JSON.stringify(data));
// 结果：{"normal":"正常值","date":"2023-...T...","regex":{},"nullProp":null,"arrayWithUndefined":[1,null,3]}
```

## 忽略的东西 

- 函数属性（方法）。
- Symbol 类型的键和值。
- 存储 `undefined` 的属性。


## JSON.strngfit

```
let json = JSON.stringift(value[,replacer,space]);
```

value

要编码的值。

replacer

要编码的属性数组或映射函数 `function(key, value)`。

space

用于格式化的空格数量
replacer：函数的编写
```
function replacer(key, value) {
  // 1. 分析当前处理的属性
  console.log(`处理属性: ${key}, 值:`, value);
  
  // 2. 根据业务逻辑决定如何处理
  if (需要排除该属性) {
    return undefined;
  } else if (需要转换该值) {
    return 转换后的值;
  } else {
    // 3. 默认情况：正常序列化
    return value;
  }
}
```



# JSON.parse

解码JSON字符串

但是这只能进行基本解码，要解析为其它对象的话要函数

例如
```
let str = "";
let meetup = JSON.parse(str,function(key,value){
	if(key == 'date') return new Date(value);
	return value;
})
```



