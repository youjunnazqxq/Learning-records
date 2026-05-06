`String` 类是 Java 中使用最频繁，但也是**面试陷阱最多**、**性能坑最深**的一个类。

因为它太常用了，Java 对它做了很多特殊的优化。如果不了解这些底层机制，很容易写出“功能没问题，但性能极差”的代码。

以下是你需要注意的 **5 个核心知识点**：

### 1. 核心特性：不可变性 (Immutability)

这是 String 最本质的特征。**String 对象一旦被创建，其内容就永远无法改变。**

- **误区**：
    
    Java
    
    ```
    String s = "Hello";
    s = s + " World"; // 你以为你在修改原来的 s 吗？
    ```
    
- 真相：
    
    你并没有修改原来的 "Hello" 对象。
    
    1. Java 创建了一个新的 StringBuilder。
        
    2. 拼接了 "Hello" 和 " World"。
        
    3. **new** 了一个全新的 String 对象 `"Hello World"`。
        
    4. 让 `s` 指向这个新对象。
        
    
    - 原来的 `"Hello"` 对象还在内存里，变成了垃圾。
        

### 2. 比较陷阱：`==` vs `equals` (必死题)

这是新手写 Bug 的第一大来源。

- **`==`**：比较的是 **内存地址**（是不是同一个对象）。
    
- **`equals()`**：比较的是 **内容**（长得是不是一样）。
    

**代码演示**：

Java

```
String s1 = "hello";
String s2 = new String("hello");

System.out.println(s1 == s2);      // false (地址不同，一个是常量池，一个是堆)
System.out.println(s1.equals(s2)); // true  (内容都是 "hello")
```

> 老手技巧：
> 
> 在做字符串比较时，把常量写在前面，防止空指针异常 (NPE)。
> 
> - ❌ `if (name.equals("admin"))` // 如果 name 是 null，这就崩了
>     
> - ✅ `if ("admin".equals(name))` // 就算 name 是 null，这也只返回 false，不会崩
>     

### 3. 字符串常量池 (String Pool)

为了省内存，Java 搞了个“缓存池”。

- **字面量赋值** (`String s = "abc"`)：
    
    - Java 会先去池子里找有没有 "abc"。
        
    - 有就直接给你地址（复用）；没有就创建一个放进去。
        
- **`new` 关键字** (`String s = new String("abc")`)：
    
    - **强制**在堆内存（Heap）里创建一个新对象，**不走常量池的复用逻辑**（虽然它内部维护的字符数组可能指向池里的）。
        

### 4. 拼接的效率（StringBuilder 的出场时刻）

由于 String 不可变，每次 `+` 都会产生新对象。

- **场景**：如果你在**循环**里拼接字符串。
    
    Java
    
    ```
    String str = "";
    for (int i = 0; i < 1000; i++) {
        str += i; // ❌ 极度消耗内存！产生了 1000 个垃圾对象
    }
    ```
    
- **正确做法**：使用 **`StringBuilder`**。
    
    - `StringBuilder` 是可变的（Mutable），它像一个容器，你可以一直往里面 `append` 内容，最后再一次性转成 String。
        
    
    Java
    
    ```
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < 1000; i++) {
        sb.append(i); // ✅ 全程只操作这一个对象，速度快几百倍
    }
    String result = sb.toString();
    ```
    

**三者对比（面试常问）：**

1. **`String`**：不可变，适合少量操作。
    
2. **`StringBuilder`**：可变，**快**，线程不安全（绝大多数情况用这个）。
    
3. **`StringBuffer`**：可变，**慢**（因为它加了锁，线程安全），现在很少用了。
    

### 5. 常用 API 的小坑

- **`split()`**：
    
    - 如果你用 `.` 切割，必须写成 `split("\\.")`。因为 `split` 接收的是正则表达式，而在正则里 `.` 代表“任意字符”。
        
- **`substring(start, end)`**：
    
    - 它是 **“左闭右开”** 区间。
        
    - `"01234".substring(1, 3)` 结果是 `"12"`（取索引 1 和 2，不包含 3）。
        
- **`trim()` vs `strip()`** (Java 11+)：
    
    - `trim()` 只能去掉普通的 ASCII 空格。
        
    - `strip()` 更强大，能去掉各种 Unicode 空白字符（比如中文全角空格）。
        

### 总结

1. 比较内容**一定要用 `equals`**。
    
2. 循环拼接**一定要用 `StringBuilder`**。
    
3. 字面量赋值优于 `new String()`。