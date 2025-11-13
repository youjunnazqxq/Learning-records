
# async

语法：
```
async function f(){

		return 1;
}
```

async” 这个单词表达了一个简单的事情：即这个函数总是返回一个 promise。其他值将自动被包装在一个 resolved 的 promise 中。

# await 
关键字 `await` 让 JavaScript 引擎等待直到 promise 完成（settle）并返回结果

让我们强调一下：`await` 实际上会暂停函数的执行，直到 promise 状态变为 settled，然后以 promise 的结果继续执行。这个行为不会耗费任何 CPU 资源，因为 JavaScript 引擎可以同时处理其他任务：执行其他脚本，处理事件等。
```
let value = await promise;
```



# Error 处理 
如果一个 promise 正常 resolve，`await promise` 返回的就是其结果。但是如果 promise 被 reject，它将 throw 这个 error，就像在这一行有一个 `throw` 语句那样。


```
async function showAvatar() {

  // 读取我们的 JSON
  let response = await fetch('/article/promise-chaining/user.json');
  let user = await response.json();

  // 读取 github 用户信息
  let githubResponse = await fetch(`https://api.github.com/users/${user.name}`);
  let githubUser = await githubResponse.json();

  // 显示头像
  let img = document.createElement('img');
  img.src = githubUser.avatar_url;
  img.className = "promise-avatar-example";
  document.body.append(img);

  // 等待 3 秒
  await new Promise((resolve, reject) => setTimeout(resolve, 3000));

  img.remove();

  return githubUser;
}

showAvatar();
```

