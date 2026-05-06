基于你上传的复习重点图片，`Connection` 是 **JDBC (Java Database Connectivity)** 中最基础、最重要的接口之一。

简单来说，**`Connection` 就是 Java 程序和数据库之间的一座“桥梁”**。如果不先建立这个连接，你就没法给数据库发送任何命令（SQL）。

以下是关于它的核心知识点，也是考试经常涉及的内容：

### 1. 它的角色 (是什么？)

- **定义**：它是 `java.sql` 包下的一个接口。
    
- **作用**：它代表与特定数据库的**物理连接**（会话）。
    
- **地位**：它是 JDBC 操作的第一步。只有拿到了 `Connection` 对象，你才能创建后续的 `Statement` 对象来执行 SQL 语句。
    

### 2. 怎么获取它？ (代码怎么写)

通常是通过 `DriverManager` 这个“包工头”来获取。你需要提供数据库的 URL、用户名和密码。

Java

```
// 1. 加载驱动 (有时候新版JDK可以省略)
Class.forName("com.mysql.cj.jdbc.Driver");

// 2. 建立连接 (这就是获取 Connection 对象)
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydb", // URL
    "root",                               // 用户名
    "123456"                              // 密码
);
```

### 3. 它有什么用？ (常用方法)

拿到 `conn` 对象后，你主要用它做三件事：

1. **创建执行者 (`Statement`)**：
    
    - `Statement stmt = conn.createStatement();`
        
    - 或者预编译的 `PreparedStatement pstmt = conn.prepareStatement(sql);`
        
    - _（这是最常用的功能，用来发送 SQL）_
        
2. **管理事务 (Transaction)**：
    
    - 默认情况下，JDBC 是自动提交的（Auto-commit）。
        
    - `conn.setAutoCommit(false);` // 开启事务（手动提交）
        
    - `conn.commit();` // 提交事务
        
    - `conn.rollback();` // 回滚事务（出错了撤销）
        
3. **关闭连接 (释放资源)**：
    
    - `conn.close();`
        
    - _（注意：数据库连接是非常昂贵的资源，用完**必须**关闭，否则会导致数据库崩溃）_
        

### 总结一张图 (JDBC 三巨头关系)

为了方便记忆，你可以这样理解图片里提到的三个类 的关系：

1. **`Connection` (路)**：先修好路，连通 Java 和 数据库。
    
2. **`Statement` (车)**：在路上跑的车，负责把 SQL 语句运过去。
    
3. **`ResultSet` (货)**：车运回来的结果（比如查出来的 10 行数据）。