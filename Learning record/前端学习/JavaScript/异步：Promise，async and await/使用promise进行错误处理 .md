# 错误的传递理解

在js中，错误也会跟着then链条进行传递，一旦遇到相关的then有处理error的结果就会开始处理这个error。

# 隐式 try...catch
promise 的执行者（executor）和 promise 的处理程序周围有一个“隐式的 `try..catch`”。如果发生异常，它就会被捕获，并被视为 rejection 进行处理。

隐式`try...catch`会自动捕获error，并将其变为rejected promise。
这不仅仅发生在 executor 函数中，同样也发生在其处理程序中。如果我们在 `.then` 处理程序中 `throw`，这意味着 promise rejected，因此控制权移交至最近的 error 处理程序。

## 注意
这里的隐式只能处理同步的错误，会抛出同步的错误，但是异步需要我们手动来抛出


# rethrowing

- 若  catch  内部未抛出错误、也未返回 rejected 的 Promise，则  catch  返回  resolved  状态的 Promise，后续  then  会执行。


- 若  catch  内部抛出了错误、或返回 rejected 的 Promise，则  catch  返回  rejected  状态的 Promise，后续  then  会被跳过，直接传递到下一个  catch 。


# 未处理的rejection
如果出现 error，promise 的状态将变为 “rejected”，然后执行应该跳转至最近的 rejection 处理程序。但上面这个例子中并没有这样的处理程序。因此 error 会“卡住”。没有代码来处理它。


