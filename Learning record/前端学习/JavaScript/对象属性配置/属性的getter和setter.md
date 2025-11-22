这份笔记旨在帮你**一眼看懂** JavaScript 中 Getter 和 Setter 的核心机制，以及它们在 Vue 中的实际作用。

---

# 🛡️ JavaScript 核心机制：Getter 与 Setter

### 1. 一句话理解

Getter (读) 和 Setter (写) 是给对象属性安装的**“智能门卫”**。

它们把简单的 “属性读写” 变成了 “函数执行”，让你能控制数据进出的全过程。

### 2. 核心职能图解

|**角色**|**英文**|**触发动作**|**职责与作用**|**形象比喻**|
|---|---|---|---|---|
|**Getter**|`get`|当你 **使用/读取** 变量时<br><br>  <br><br>`console.log(obj.name)`|**加工数据**<br><br>  <br><br>返回经过计算或处理后的值|**“翻译官”**<br><br>  <br><br>(你要A，他加工成A+给你)|
|**Setter**|`set`|当你 **赋值/修改** 变量时<br><br>  <br><br>`obj.name = 'xx'`|**监控数据**<br><br>  <br><br>做校验、发通知、触发副作用|**“安检员”**<br><br>  <br><br>(你要进门，先检查合不合格)|

---

### 3. 标准语法 (ES6 写法)

最常见的写法，直接在对象里定义：

JavaScript

```
let person = {
    firstName: '张',
    lastName: '三',

    // Getter: 并没有 fullName 这个属性，是现算出来的
    get fullName() {
        return this.firstName + this.lastName;
    },

    // Setter: 拦截赋值操作
    set fullName(value) {
        console.log('有人要把名字改成：', value);
        // 拆分姓名，更新内部数据
        const arr = value.split('');
        this.firstName = arr[0];
        this.lastName = arr[1];
    }
};

// ✅ 测试 Getter
console.log(person.fullName); // 输出 "张三" (自动调用 get)

// ✅ 测试 Setter
person.fullName = '李四';     // (自动调用 set)
console.log(person.firstName); // 输出 "李" (内部数据已更新)
```

---

### 4. Vue 中的应用 (底层原理)

Vue 2 使用 `Object.defineProperty()` 强制给 `data` 里的每个属性加上了这两个门卫。

- **Getter 的作用**：**依赖收集**。
    
    - _Vue 会记账_：“页面上的 `<h1>` 标签用了 `name` 这个数据，记下来。”
        
- **Setter 的作用**：**派发更新 (响应式核心)**。
    
    - _Vue 会报警_：“`name` 被改成了 '新值'！刚才记账的那些 `<h1>` 标签，赶紧刷新显示！”
        

---

### ⚠️ 避坑指南 (注意事项)

1. 不要死循环：
    
    在 set age(val) 函数内部，千万不要再写 this.age = val，否则会无限触发 Setter 导致栈溢出。通常需要配合一个内部变量（如 _age）来存值。
    
2. 伪装性：
    
    对使用者来说，obj.fullName 看起来就是一个普通属性，看不出它是函数。这正是封装的精髓。
    

---

### 🧠 记忆口诀

> 读数据走 Get，加工一下再给；
> 
> 改数据走 Set，监控变化无悔。
> 
> Vue 靠它做劫持，响应原理最美。