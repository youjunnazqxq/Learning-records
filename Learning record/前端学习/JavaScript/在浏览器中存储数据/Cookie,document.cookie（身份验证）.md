
# 从document.cookie中读取
`document.cookie` 的值由 `name=value` 对组成，以 `;` 分隔。每一个都是独立的 cookie。



# 写入 document.cookie

我们可以写入 `document.cookie`。但这不是一个数据属性，它是一个 [访问器（getter/setter）](https://zh.javascript.info/property-accessors)。对其的赋值操作会被特殊处理。

**对 `document.cookie` 的写入操作只会更新其中提到的 cookie，而不会涉及其他 cookie。**

Cookie 有几个选项，其中很多都很重要，应该设置它。

选项被列在 `key=value` 之后，以 `;` 分隔

#### path

url 路径前缀必须是绝对路径。它使得该路径下的页面可以访问该 cookie。默认为当前路径。

如果一个 cookie 带有 `path=/admin` 设置，那么该 cookie 在 `/admin` 和 `/admin/something` 下都是可见的，但是在 `/home` 或 `/adminpage` 下不可见


# domain 

`domain = site.com`

domain 控制了可访问 cookie 的域。但是在实际中，有一些限制。我们无法设置任何域。

**无法从另一个二级域访问 cookie，因此 `[other.com](http://other.com/)` 永远不会收到在 `[site.com](http://site.com/)` 设置的 cookie。**


# expires，max-age
默认情况下，如果一个 cookie 这两个参数都没有设置，那么在关闭浏览器之后，它就会消失。此类 cookie 被称为 "session cookie”

1.  expires ：设置“具体的过期日期”
​
- 作用：指定一个GMT时区的具体时间点，到了这个时间，浏览器会自动删除该 Cookie。
​
- 注意：日期格式必须是 GMT 标准（比如  Tue, 19 Jan 2038 03:14:07 GMT ），所以代码里要通过  date.toUTCString()  转换格式（避免时区错乱）。
​
- 特殊用法：如果把  expires  设为过去的时间，Cookie 会被立即删除（常用于“手动清除Cookie”）。
​
2.  max-age ：设置“距离当前时间的秒数”
​
- 作用：指定 Cookie 从“当前时刻”开始，存活多少秒后过期（更直观、不用处理日期格式）。

### secure 
Cookie 应只能被通过 HTTPS 传输。

**默认情况下，如果我们在 `[http://site.com](http://site.com/)` 上设置了 cookie，那么该 cookie 也会出现在 `[https://site.com](https://site.com/)` 上，反之亦然。**

# XSRF 攻击 


- **`HttpOnly`**
    
    - **作用**：禁止 JavaScript 访问这个 Cookie。
        
    - **后果**：如果服务器设置了 `HttpOnly`（所有 Session ID **都应该**设置），你在浏览器控制台里运行 `alert(document.cookie)` **根本看不到**那个 Session ID。
        
    - **重要性**：**极高**。这是防止 **XSS 攻击**（跨站脚本攻击）窃取用户登录状态的核心手段。
        
- **`Secure`**
    
    - **作用**：只允许 Cookie 通过 **HTTPS**（加密）连接发送。
        
    - **后果**：如果用户处于不安全的 HTTP 连接（比如公共 Wi-Fi），浏览器**不会**发送这个 Cookie，防止被**中间人窃听**。
        
    - **重要性**：**高**。
        
- **`SameSite`** (Strict / Lax / None)
    
    - **作用**：控制 Cookie 是否可以随**跨站请求**一起发送。
        
    - **后果**：这决定了当你在网站 A 点击一个链接跳转到网站 B 时，网站 B 的请求是否能带上网站 A 的 Cookie。
        
    - **重要性**：**高**。这是防止 **CSRF 攻击**（跨站请求伪造）的主要手段。