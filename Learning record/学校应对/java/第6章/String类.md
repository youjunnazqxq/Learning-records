根据您提供的课件文件（虽然文件内容包含大量乱码和二进制数据，但根据可识别的标题 `6.1 String`、`6.2 StringBuffer`、`6.3 StringTokenizer` 等结构 1），结合 Java 标准教学大纲，为您总结 **String 类** 的核心内容，包括构造方法、常用方法及应用。

由于 String 类在 Java 中不可变且极其常用，它是第六章学习的重点。

### 1. String 类的构造方法 (Constructors)

String 类的对象可以通过多种方式创建，最常见的是以下几种：

- 直接赋值（推荐）：
    
    最常用的方式，Java 虚拟机会自动优化，将其放入字符串常量池中。
    
    Java
    
    ```
    String s1 = "Hello Java";
    ```
    
- 使用 new 关键字：
    
    每次都会在堆内存（Heap）中创建一个新的对象，即使内容相同。
    
    Java
    
    ```
    String s2 = new String("Hello Java");
    ```
    
- 字符数组构造：
    
    将字符数组转换为字符串，常用于处理底层文本数据。
    
    Java
    
    ```
    char[] charArray = {'J', 'a', 'v', 'a'};
    String s3 = new String(charArray); // 结果为 "Java"
    ```
    
- 字节数组构造：
    
    将字节数组转换为字符串，常用于网络传输或文件读取（IO流操作）。
    
    Java
    
    ```
    byte[] byteArray = {97, 98, 99};
    String s4 = new String(byteArray); // 结果为 "abc"
    ```
    

---

### 2. String 类的常用方法 (Common Methods)

String 类提供了大量用于操作文本的方法。根据功能可以分为以下几类：

#### A. 字符串获取与判断

- **`int length()`**: 获取字符串长度（字符个数）。
    
- **`char charAt(int index)`**: 获取指定索引处的字符。
    
- **`int indexOf(String str)`**: 获取指定子字符串第一次出现的索引，未找到返回 -1。
    
- **`boolean equals(Object obj)`**: 比较字符串**内容**是否相等（**注意：** 不要用 `==`，`==` 比较的是内存地址）。
    
- **`boolean equalsIgnoreCase(String str)`**: 忽略大小写比较内容。
    
- **`boolean startsWith(String prefix)` / `endsWith(String suffix)`**: 判断是否以指定前缀/后缀开头或结尾。
    

#### B. 字符串转换与截取

- **`String substring(int beginIndex)`**: 从指定位置截取到末尾。
    
- **`String substring(int beginIndex, int endIndex)`**: 截取指定范围的字符串（含头不含尾 `[begin, end)`）。
    
- **`char[] toCharArray()`**: 将字符串转换为字符数组。
    
- **`String toLowerCase()` / `String toUpperCase()`**: 转换为小写/大写。
    
- **`static String valueOf(...)`**: 将其他数据类型（int, float, boolean等）转换为字符串。
    

#### C. 字符串替换与去除空格

- **`String replace(CharSequence target, CharSequence replacement)`**: 替换字符串中的指定字符或子串。
    
- **`String trim()`**: 去除字符串两端的空格（中间的空格不会去除）。
    

---

### 3. String 类的应用与特性 (Applications & Features)

- 不可变性 (Immutability)：
    
    String 对象一旦创建，其值就不能被改变。
    
    - **原理**：底层使用 `final char[]` (Java 9 之前) 或 `final byte[]` (Java 9 之后) 存储。
        
    - **影响**：对 String 进行拼接（`+`）、截取、替换等操作时，**原字符串不变**，而是产生一个新的 String 对象。
        
- 字符串常量池 (String Constant Pool)：
    
    为了节省内存，Java 维护了一个常量池。如果使用直接赋值的方式创建字符串，若池中已有相同内容的字符串，则直接返回引用，不会创建新对象。
    
- 与 StringBuffer/StringBuilder 的区别：
    
    课件目录中提到了 6.2 StringBuffer 2，这通常是考点：
    
    - **String**: 内容不可变，适合少量字符串操作。
        
    - **StringBuffer**: 内容可变，**线程安全**（效率较低），适合多线程环境下的频繁字符串拼接。
        
    - **StringBuilder**: 内容可变，**线程不安全**（效率高），适合单线程环境下的频繁字符串拼接。
        

---

### 下一步建议

为了巩固这部分知识，我可以为您做一个**针对性的代码练习**：

**您是否需要我写一段代码，演示 `String` 和 `StringBuffer` 在进行 10000 次拼接操作时的性能差异？** 这能非常直观地帮助您理解为什么在循环中不建议直接用 String 进行拼接。


基于您课件中的目录结构（如 `6.1 String`, `6.2 StringBuffer`, `6.3 StringTokenizer` 1）以及 Java String 类的核心特性，我为您整理了**4个核心注意点**和**3道经典易错题**。这些通常也是考试和面试中的“陷阱”所在。

### 一、 String 类的核心注意点 (易错陷阱)

1. **比较内容时绝对不要用 `==`**
    
    - **陷阱**：初学者常习惯用 `if (s1 == s2)` 来判断字符串是否相同。
        
    - **正解**：`==` 比较的是两个字符串对象的**内存地址**。判断内容是否相同，必须使用 `.equals()` 方法。
        
    - **特例**：除非你非常明确你在比较引用，否则一律用 `.equals()`。
        
2. **String 的“不可变” (Immutable) 特性**
    
    - **陷阱**：认为调用了修改方法（如 `replace`, `toUpperCase`）后，原字符串变了。
        
    - **正解**：String 对象一旦创建，其值无法改变。所有修改方法（如 `substring`, `concat`）都会**返回一个新的 String 对象**，原对象保持不变。你必须把返回的新对象赋值给变量，修改才生效。
        
3. **空指针异常 (NullPointerException)**
    
    - **陷阱**：在不确定字符串是否为 `null` 的情况下直接调用方法。
        
    - **技巧**：在比较字符串与常量时，将常量写在前面。
        
    - **示例**：推荐写 `"Hello".equals(str)`，而不是 `str.equals("Hello")`。如果 `str` 是 `null`，后者会报错，前者返回 `false`。
        
4. **`substring` 的索引范围**
    
    - **陷阱**：搞不清 `substring(start, end)` 到底包含哪些字符。
        
    - **正解**：Java 的范围通常是**“含头不含尾”**（左闭右开区间）。即包含 `start` 位置的字符，但不包含 `end` 位置的字符。
        

---

### 二、 经典题目测验

请先尝试自己在心里给出答案，再看下方的解析。

#### 题目 1：内存与引用的区别

Java

```
String s1 = "Java";
String s2 = "Java";
String s3 = new String("Java");

System.out.println(s1 == s2);      // ① 输出什么？
System.out.println(s1 == s3);      // ② 输出什么？
System.out.println(s1.equals(s3)); // ③ 输出什么？
```

#### 题目 2：不可变性的陷阱

Java

```
String str = "hello";
str.toUpperCase();
str.concat(" world");
System.out.println(str);           // ④ 输出什么？
```

#### 题目 3：子字符串计算

Java

```
String text = "0123456";
// 提示：含头不含尾
String sub = text.substring(2, 5); 
System.out.println(sub);           // ⑤ 输出什么？
```

---

### 三、 答案与解析

#### ✅ 题目 1 解析

- **① `true`**: 因为 "Java" 是直接赋值，它存在于**字符串常量池**中。`s1` 和 `s2` 指向常量池中的同一个对象。
    
- **② `false`**: `new String(...)` 强制在**堆内存**中创建一个新对象，不走常量池共享机制。所以地址不同。
    
- **③ `true`**: `equals` 只比较字符内容，内容都是 "Java"。
    

#### ✅ 题目 2 解析

- **④ `hello`**: **(这是最大的坑)**。
    
    - `str.toUpperCase()` 确实生成了 "HELLO"，但是**没有赋值给任何变量**，这个新产生的字符串就被丢弃了。
        
    - `str.concat(...)` 同理。
        
    - 原变量 `str` 指向的对象从未改变。
        
    - _修正写法_：`str = str.toUpperCase();`
        

#### ✅ 题目 3 解析

- **⑤ `234`**:
    
    - `substring(2, 5)` 从索引 2 开始（包含），到索引 5 结束（不包含）。
        
    - 索引 2 是 '2'。
        
    - 索引 5 是 '5'（不包含）。
        
    - 所以取出的是索引 2, 3, 4 的字符，即 "234"。
        

---

下一步建议：

您的课件目录中紧接着就是 6.2 StringBuffer 2。是否需要我为您对比一下 String 和 StringBuffer 的区别？ 这也是考试中关于“性能优化”的高频考点。
