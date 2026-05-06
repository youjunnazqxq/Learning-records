### 最核心的方法：`getTime()`

这是 `Date` 类中**最有用、最常用**的方法，没有之一。

- **`long getTime()`**
    
    - **作用**：获取当前时间距离 **1970年1月1日 00:00:00** （格林威治时间）的**毫秒数**。
        
    - **专业术语**：这叫 **“时间戳” (Timestamp)**。
        
    - **场景**：通常用于计算一段代码跑了多久，或者在两个系统之间传递时间。
        
    - **代码示例**：
        
        Java
        
        ```
        Date date = new Date(); // 获取当前时间
        long time = date.getTime(); 
        System.out.println(time); // 输出类似 1705324... 的一大串数字
        ```
        

### 2. 比较时间先后 (谁前谁后？)

除了获取时间戳，`Date` 最擅长的就是比较。

- **`boolean before(Date when)`**：判断当前日期是否在参数日期**之前**。
    
- **`boolean after(Date when)`**：判断当前日期是否在参数日期**之后**。
    
- **`int compareTo(Date anotherDate)`**：
    
    - 返回 `0`：两个时间相等。
        
    - 返回 `<0`：当前时间早。
        
    - 返回 `>0`：当前时间晚。
        

### 3. 它的好搭档：`SimpleDateFormat` (必考)

Date 类自己打印出来的格式非常难看（类似 Tue Jan 13 09:00:00 CST 2026）。

为了把它变成我们习惯的 "2026-01-13 09:00:00"，必须配合 SimpleDateFormat 类使用。

这通常是**成对出现**的考点：

- **格式化 (Format)**： Date对象 $\rightarrow$ String
    
- **解析 (Parse)**： String $\rightarrow$ Date对象
    

Java

```
// 1. 创建格式化工具（指定模板）
// yyyy:年, MM:月, dd:日, HH:24小时制, mm:分, ss:秒
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

// 2. Date -> String (格式化)
Date date = new Date();
String str = sdf.format(date); 
System.out.println(str); // 输出：2026-01-13 09:25:10

// 3. String -> Date (解析)
String timeStr = "2008-08-08 20:00:00";
try {
    Date d2 = sdf.parse(timeStr); // 注意：这里必须处理异常 ParseException
} catch (ParseException e) {
    e.printStackTrace();
}
```

---

### ⚠️ 严重警告：Date 类的两大“天坑”

很多初学者会在以下两个地方栽跟头，这也是为什么 Java 要淘汰它的原因：

1. **月份是从 0 开始的！**
    
    - 如果你调用（虽然已废弃）`getMonth()`，**1月会返回 0**，12月返回 11。
        
    - _一定要记住：月份 = 实际月份 - 1。_
        
2. **年份是从 1900 开始的！**
    
    - `getYear()` 返回的是当前年份减去 1900 的值。这极其反人类。
        

**由于这些设计缺陷，`getYear()`, `getMonth()`, `getDate()` 等方法都已经被打上了 `@Deprecated`（已废弃）标签，千万不要在作业或项目里用它们！**