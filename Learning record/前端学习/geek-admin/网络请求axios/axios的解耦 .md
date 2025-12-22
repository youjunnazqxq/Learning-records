**解耦 (Decoupling)** 是软件工程中最重要的原则之一，简单概括就是八个字：**“各司其职，互不干扰”**。

在前端网络请求的语境下，解耦的核心目的是：**把“怎么发请求”、“请求去哪里”和“页面怎么用数据”这三件事彻底分开。**

如果不解耦，你的代码就像一团乱麻；解耦后，你的代码就像积木一样清晰。

---

### 1. 为什么要解耦？（对比现场）

#### ❌ 耦合的写法（糟糕的代码）

想象一下，如果你在每一个 `.vue` 或 React 组件里都直接写 `axios.get`：

JavaScript

```
// UserProfile.vue (组件)
methods: {
  getUserData() {
    // 坏处 1: URL 散落在各个页面，后端改地址你要翻遍几十个文件修改
    // 坏处 2: 如果想给所有请求加 Token，你得去每个页面复制粘贴代码
    axios.get('https://api.example.com/v1/user/info?id=123')
      .then(res => { this.info = res.data })
      .catch(err => { alert('出错啦') });
  }
}
```

- **问题**：页面组件既要负责渲染 UI，又要负责处理 HTTP 细节（URL、Token、错误处理）。一旦接口变动，维护起来简直是灾难。
    

#### ✅ 解耦的写法（优雅的代码）

我们将代码拆分为三层结构，每一层只负责一件事。

---

### 2. 解耦的三层架构

为了实现解耦，我们通常会建立以下目录结构：

Plaintext

```
src/
  ├── utils/       # 【工具层】负责“怎么发请求” (基础配置)
  │    └── request.js
  ├── api/         # 【接口层】负责“请求去哪里” (API 定义)
  │    └── user.js
  └── views/       # 【视图层】负责“什么时候要数据” (UI 组件)
       └── UserProfile.vue
```

#### 第一层：工具层 (utils/request.js) —— “基建部门”

它不关心具体的业务，只管修路（配置 Axios）。

- **职责**：创建 Axios 实例、设置 BaseURL、统一拦截 Token、统一报错。
    
- **产出**：我们在上一节封装好的那个 `request` 对象。
    

#### 第二层：接口层 (api/user.js) —— “通讯录/菜单”

它不知道页面长什么样，也不知道 Token 怎么存，它只记录后端给了哪些接口。

- **职责**：把具体的 URL 和请求方法封装成一个个**函数**。
    

JavaScript

```
// src/api/user.js
import request from '@/utils/request'; // 引入封装好的“专线”

// 定义接口：获取用户信息
export function getUserInfo(id) {
  return request({
    url: '/user/info',
    method: 'get',
    params: { id }
  });
}

// 定义接口：修改密码
export function changePassword(data) {
  return request({
    url: '/user/password',
    method: 'post',
    data
  });
}
```

#### 第三层：视图层 (views/UserProfile.vue) —— “指挥官”

它完全不知道 `axios` 库的存在，也不知道 URL 是什么。它只管调用函数。

- **职责**：在用户点击按钮或页面加载时，调用 API 函数，拿到数据更新页面。
    

JavaScript

```
// src/views/UserProfile.vue
import { getUserInfo } from '@/api/user'; // 引入接口函数

export default {
  methods: {
    async initData() {
      // 极其清爽：只关注业务，没有 URL，没有 headers 配置
      const res = await getUserInfo(123);
      this.info = res.data;
    }
  }
}
```

---

### 3. 解耦的具体好处

1. **维护性极高（牵一发不动全身）**
    
    - 如果后端把域名改了，你只需要改 `utils/request.js` 里的 `baseURL`。
        
    - 如果后端把“获取用户信息”的接口路径从 `/user/info` 改成了 `/u/profile`，你只需要改 `api/user.js` 这一个文件。**你的几十个页面组件完全不需要动！**
        
2. **代码复用**
    
    - `getUserInfo` 这个接口可能在“个人中心”页面用，也可能在“首页顶部”用。解耦后，直接引入函数即可，不用到处复制粘贴 URL。
        
3. **可读性强**
    
    - 页面代码里看到的是语义化的 `getUserInfo()`，而不是冷冰冰的 `axios.get('/api/v1/...')`。
        
4. **分工合作**
    
    - 你在写页面（View）时，可以不用管接口具体的实现细节；甚至可以在接口没开发好时，在 `api/user.js` 里写个假数据先跑起来。
        

---

### 总结

**解耦就是把复杂的网络请求拆解成流水线：**

1. **View 层**说：“我要用户信息！”（调用函数）
    
2. **API 层**说：“收到，地址是 `/user/info`，方法是 `GET`。”（传入配置）
    
3. **Utils 层**说：“收到，我来加上 Token，处理好超时设置，然后发给服务器。”（执行请求）
    

理解了解耦，你的前端架构能力就上了一个台阶。

**接下来，你想实际动手试一个例子，比如“如何把一个具体的登录功能按照这个三层架构写出来”吗？**