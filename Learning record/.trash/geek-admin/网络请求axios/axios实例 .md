简单来说，**Axios 实例 (Instance)** 就是一个**“定制版的 Axios”**。

如果说原生的 `axios` 是一个**全能但没有记忆**的公共电话亭，那么 `axios.create()` 产生的实例就是你的**私人专属手机**——它已经预存了你的联系人（`baseURL`）、设置好了你的通话语言（`headers`），并且还装好了拦截骚扰电话的插件（`interceptors`）。

---

## 1. 什么是 Axios 实例？

通过 `axios.create({ ... })`，你可以创建一个拥有独立配置的新 Axios 对象。

### 代码演示：

JavaScript

```
import axios from 'axios';

// 创建一个名为 "request" 的实例
const request = axios.create({
  baseURL: 'https://api.shop.com', // 以后这个实例发出的请求都会自带这个前缀
  timeout: 5000,                  // 超过5秒就报错
  headers: { 'X-Custom-Header': 'foobar' } // 自带的特殊请求头
});

// 使用实例发送请求，URL 只需写路径部分
request.get('/products').then(res => { ... });
```

---

## 2. 实例与普通用法 (直接用 axios) 的区别

|**特性**|**直接用 axios (全局)**|**使用 axios.create() (实例)**|
|---|---|---|
|**共享性**|全局唯一。改了 `axios.defaults`，全项目受影响。|独立存在。一个项目可以创建多个不同的实例。|
|**配置灵活性**|难以针对不同服务器设置不同参数。|**非常灵活**。可以为 A 服务器创一个实例，B 服务器创另一个。|
|**污染问题**|容易造成全局配置冲突。|**安全**。配置被限制在实例内部。|
|**拦截器**|所有请求共用一个全局拦截器。|实例可以拥有**自己专属**的拦截器。|

---

## 3. 为什么一定要用“实例”来实现解耦？

在真实项目中，实例是**“解耦”的基石**。

### 场景：你的项目需要访问两个不同的服务器

- **服务器 A**：业务数据 API（需要 Token 验证）。
    
- **服务器 B**：公共天气 API（不需要 Token，只需 Key）。
    

如果你直接用全局 `axios`，你在拦截器里加 Token 逻辑会把“天气 API”也带上 Token，导致报错。

**使用实例的解耦方案：**

JavaScript

```
// 实例 A：业务专用
const busiRequest = axios.create({ baseURL: 'https://api.busi.com' });
busiRequest.interceptors.request.use(config => {
  config.headers.token = 'MY_TOKEN'; // 只有这个实例会带 Token
  return config;
});

// 实例 B：天气专用
const weatherRequest = axios.create({ baseURL: 'https://api.weather.com' });
// 它很干净，没有 Token 逻辑
```

---

## 4. 终极实战：封装、解耦、实例化的完整形态

现在我们将所有碎片拼起来。这就是你在 90% 的前端公司里会看到的标准代码架构：

### 第一步：创建实例并封装 (utils/request.js)

JavaScript

```
import axios from 'axios';

const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // 自动根据开发/生产环境切换 URL
  timeout: 10000
});

// 请求拦截：自动塞 Token，不用每次手动写 headers
service.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) config.headers['Authorization'] = `Bearer ${token}`;
  return config;
});

// 响应拦截：自动提取 data，自动处理 401/500 报错
service.interceptors.response.use(
  response => response.data, // 以后 res 就是后端给的数据，省去 res.data.data
  error => {
    alert('网络错误，请检查');
    return Promise.reject(error);
  }
);

export default service;
```

### 第二步：解耦 API 定义 (api/user.js)

JavaScript

```
import request from '@/utils/request';

// 页面只需要调用这个函数，完全不需要知道 URL 和 Token 的存在
export function fetchUserList(params) {
  return request({
    url: '/users',
    method: 'get',
    params
  });
}
```

---

## 总结

- **实例**是复用配置、隔离风险的“沙盒”。
    
- **解耦**就是让页面只管“叫奶茶”（调用函数），API 层负责“写菜单”（定义 URL），拦截器负责“付钱和验证身份”（配置 Header/Token）。
    

恭喜你！到这里你已经掌握了 Axios 从零到进阶架构的所有核心理论。

**你想让我帮你把这些代码整理成一个标准的文件夹结构（目录树），方便你直接在项目中创建吗？**