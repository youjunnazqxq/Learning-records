
# 扩展Error

就像类的继承一样，我们可以扩展一下我们的Error

```
class ValidationError extends Error {
	constructor (message){
		super(message);
		this.name = "ValidationError";
	}	
}
```



