这是“心脏”部位。我们将实现：

1. **创建实例**：配置基础 URL 和超时。
    
2. **请求拦截**：自动携带 Token。
    
3. **响应拦截**：自动剥离数据、统一处理业务错误（如 401 过期）。
    

JavaScript

```
import axios from 'axios';

// 1. 创建 Axios 实例
const service = axios.create({
  // 根据环境设置基础地址 (通常配置在 .env 文件中)
  // 开发环境可能是 '/api'，生产环境可能是 'https://api.pro.com'
  baseURL: process.env.VUE_APP_BASE_API || '/api', 
  timeout: 10000 // 请求超时时间：10秒
});

// 2. 请求拦截器 (Request Interceptor)
service.interceptors.request.use(
  config => {
    // 每次发送请求之前，自动携带 Token
    const token = localStorage.getItem('token');
    if (token) {
      // 按后端要求格式配置，常见是 Bearer
      config.headers['Authorization'] = `Bearer ${token}`; 
    }
    return config;
  },
  error => {
    console.error('请求发送失败:', error);
    return Promise.reject(error);
  }
);

// 3. 响应拦截器 (Response Interceptor)
service.interceptors.response.use(
  response => {
    // response.data 是后端返回的真实 JSON 数据
    const res = response.data;

    // --- 业务逻辑错误处理 ---
    // 假设后端约定：code === 200 代表成功，其他都是失败
    if (res.code !== 200) {
      // 统一弹出错误提示
      alert(res.message || '系统繁忙');

      // 特殊错误处理：登录失效 (401)
      if (res.code === 401) {
        // 清除过期 Token 并跳转登录页
        localStorage.removeItem('token');
        window.location.href = '/login';
      }
      
      // 抛出错误，中断后续操作
      return Promise.reject(new Error(res.message || 'Error'));
    } else {
      // --- 成功 ---
      // 核心：直接返回 data，页面拿到的就是纯净数据
      return res; 
    }
  },
  error => {
    // --- HTTP 网络错误处理 (如 404, 500) ---
    console.log('网络异常' + error);
    let msg = '网络连接超时';
    if (error.response) {
      switch (error.response.status) {
        case 404: msg = '接口地址不存在'; break;
        case 500: msg = '服务器内部错误'; break;
        case 403: msg = '拒绝访问'; break;
      }
    }
    alert(msg);
    return Promise.reject(error);
  }
);

export default service;
```