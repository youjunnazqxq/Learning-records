# 窗口的width/height

我们可以使用 `document.documentElement` 的 `clientWidth/clientHeight`：
![[Pasted image 20251102095753.png]]


- **`document.documentElement.clientWidth` 和 `document.documentElement.clientHeight`**
    
    - 这组属性获取的是浏览器视口（viewport）的**可用宽度和高度**。
        
    - 关键点：它**不包括**滚动条（scrollbar）所占用的空间。
        
    - 如图所示，它指的是可用于显示网页内容的实际区域。
        
- **`window.innerWidth` 和 `window.innerHeight`**
    
    - 这组属性获取的是浏览器视口的**完整宽度和高度**。
        
    - 关键点：它**包括**滚动条所占用的空间（如果滚动条存在的话）。


# 获取当前滚动



# 滚动：  scrollTo，scrollBy，scrollIntoView



