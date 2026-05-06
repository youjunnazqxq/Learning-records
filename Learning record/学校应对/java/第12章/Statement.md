基于你提供的复习重点图片，`Statement` 是 JDBC 中用来**“执行 SQL 语句”**的核心接口。

如果把 `Connection` 比作**路**，那 `Statement` 就是路上跑的**车**。它的任务就是把写好的 SQL 语句运送到数据库里去执行。

以下是关于它的 **3 个核心考点** 和 **1 个致命缺陷**：

### 1. 怎么创建它？

它必须由 `Connection` 对象产生，不能直接 new。

Java

```
Statement stmt = conn.createStatement();
```

### 2. 怎么用它？（核心方法二选一）

这是考试最容易混淆的地方，一定要分清什么时候用哪个方法：

- **`ResultSet executeQuery(String sql)`**
    
    - **用途**：专门用来执行 **查询 (SELECT)** 语句。
        
    - **返回值**：返回一个 `ResultSet`（结果集），里面装着查出来的数据。
        
    - _记忆口诀：查东西，要结果。_
        
- **`int executeUpdate(String sql)`**
    
    - **用途**：用来执行 **增、删、改 (INSERT, UPDATE, DELETE)** 语句。
        
    - **返回值**：返回一个 `int`，表示**“有几行数据受到了影响”**（比如删掉了 3 行，就返回 3）。
        
    - _记忆口诀：改东西，看行数。_
        

### 3. 代码示例

Java

```
Statement stmt = conn.createStatement();

// 场景 1：插入一条数据 (用 executeUpdate)
String sql1 = "INSERT INTO student (name, age) VALUES ('张三', 20)";
int rows = stmt.executeUpdate(sql1);
System.out.println("插入成功，影响了 " + rows + " 行");

// 场景 2：查询数据 (用 executeQuery)
String sql2 = "SELECT * FROM student";
ResultSet rs = stmt.executeQuery(sql2); // 拿到结果集
```

---

### ⚠️ 致命缺陷：SQL 注入攻击

这是面试和高阶考试必问点。`Statement` 在处理带参数的 SQL 时非常危险。

- **问题**：它是通过**字符串拼接**来生成 SQL 的。
    
- **例子**：如果你写 `"SELECT * FROM user WHERE name = '" + name + "'"`。
    
    - 如果坏人输入的 `name` 是 `' OR '1'='1`。
        
    - 整句 SQL 就变成了 `SELECT * FROM user WHERE name = '' OR '1'='1'`。
        
    - **结果**：条件永远为真，坏人不需要密码就能登录你的系统！
        

### 💡 更好的替代者：PreparedStatement

为了解决上面的安全问题，实际开发（以及考试中的进阶题）通常推荐使用 `PreparedStatement`。

- 它是 `Statement` 的子接口。
    
- **特点**：安全（防注入）、预编译（速度快）。
    
- **写法**：SQL 里用 `?` 占位，比如 `SELECT * FROM user WHERE name = ?`。
    

一句话总结：

Statement 是用来搬运 SQL 的，查数据用 executeQuery，改数据用 executeUpdate，但要注意它有SQL 注入的安全隐患。