这是一份为你量身定制的 **Axios 基础使用指南**。

结合你正在学习 Vue3 + TypeScript 的背景，我不仅仅会教你“怎么发请求”，还会教你企业开发中**“怎么优雅地发请求”**（即二次封装）。

---

### 🚀 1. 快速开始

#### 安装

在你的 Vue 项目目录下运行：

PowerShell

```
npm install axios
```

#### 最简单的用法 (不推荐在项目中直接这样到处写)

这是最原始的用法，适合测试接口。

TypeScript

```
import axios from 'axios'

// GET 请求 (查询参数)
// 等同于: /user?ID=12345
axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response.data); // 后端返回的真实数据
  })
  .catch(function (error) {
    console.log(error);
  });

// POST 请求 (提交表单/JSON)
axios.post('/user', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  .then(function (response) {
    console.log(response);
  });
```

---

### 🛠 2. 进阶：Axios 的二次封装 (企业级写法)

在实际开发中，我们不会在每个组件里都写一遍 `axios.get`。我们需要一个**统一管理**的地方。

通常我们会新建一个文件，比如 `src/utils/request.ts`。

#### 第一步：创建实例 (Instance)

为什么要创建实例？因为不同的后端服务可能有不同的 `baseURL` 或超时时间。

TypeScript

```
// src/utils/request.ts
import axios from 'axios'

// 1. 创建 axios 实例
const service = axios.create({
  // 基础路径：所有的请求都会自动拼接这个前缀
  // 例如：请求 '/login' 会自动变成 'http://localhost:8080/api/login'
  baseURL: 'http://localhost:8080/api', 
  
  // 超时时间：如果请求超过 5秒 没响应，就报错
  timeout: 5000 
})
```

#### 第二步：配置拦截器 (Interceptors)

这是 Axios 最强大的功能。它是两个“门卫”：

1. **请求拦截器**：请求发出去**之前**做的事（比如：给所有请求戴上 Token）。
    
2. **响应拦截器**：数据回来**之后**，组件拿到数据**之前**做的事（比如：剥离外层数据结构，统一处理报错）。
    

TypeScript

```
// 2. 请求拦截器 (Request Interceptor)
service.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么
    // 例如：从 localStorage 获取 token 并添加到 headers
    const token = localStorage.getItem('token')
    if (token) {
      // 这里的 Authorization 是后端要求的字段名
      config.headers.Authorization = `Bearer ${token}` 
    }
    return config
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error)
  }
)

// 3. 响应拦截器 (Response Interceptor)
service.interceptors.response.use(
  (response) => {
    // 2xx 范围内的状态码都会触发该函数
    // 简化数据：直接返回 data，组件里就不用写 response.data.data 了
    return response.data 
  },
  (error) => {
    // 超出 2xx 范围的状态码都会触发该函数
    // 统一处理错误：比如 token 过期跳转登录页，或者提示网络错误
    if (error.response && error.response.status === 401) {
      console.log('Token过期，请重新登录')
      // router.push('/login')
    }
    return Promise.reject(error)
  }
)

// 导出实例
export default service
```

---

### 📦 3. 在 API 层管理接口

不要在组件 (.vue) 里直接写 URL 字符串（如 /api/user/list），不好维护。

建议创建一个 src/api 文件夹，按模块管理。

例如 `src/api/user.ts`:

TypeScript

```
import request from '@/utils/request'

// 定义接口返回的数据类型 (TypeScript 的优势)
interface UserInfo {
  id: number
  name: string
  avatar: string
}

// 登录
export const login = (data: { username: string; password: string }) => {
  return request.post('/login', data)
}

// 获取用户信息 (使用泛型 <UserInfo> 提示返回数据的结构)
export const getUserInfo = () => {
  return request.get<any, UserInfo>('/user/info')
}
```

---

### 💻 4. 在 Vue 组件中使用

现在，你在组件里的代码会非常干净：

代码段

```
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { getUserInfo } from '@/api/user' // 引入 API

const userInfo = ref()

onMounted(async () => {
  try {
    // 1. 发起请求 (不需要写 url，不需要配置 headers，拦截器都做好了)
    const res = await getUserInfo()
    
    // 2. 赋值 (因为响应拦截器处理过，这里的 res 直接就是真实数据)
    userInfo.value = res
    console.log('获取成功', res.name)
    
  } catch (error) {
    console.error('获取失败', error)
  }
})
</script>
```

### 🧠 总结一下流程

1. **安装 Axios**。
    
2. **创建 `request.ts`**：配置 `baseURL` 和 `拦截器`（这是核心）。
    
3. **创建 `api/xxx.ts`**：把 URL 封装成函数。
    
4. **组件调用**：使用 `async/await` 调用 API 函数。
    

这就是目前前端开发中最标准、最主流的 Axios 使用模式。