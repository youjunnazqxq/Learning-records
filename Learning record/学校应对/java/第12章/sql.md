这是一个关于 **SQL（结构化查询语言）** 最核心的四大操作的知识点，通常被称为 **CRUD** (Create, Read, Update, Delete)。

在你复习 JDBC 考试时，这部分是必考的，因为 Java 程序连上数据库后，干的也就是这四件事。

我为你把这四种操作分为 **“查”** 和 **“改”** 两大类来解析，因为它们在 JDBC 里的写法是不一样的。

---

### 第一类：查询操作 (Read) —— 最常用的

对应你图片里的 **“查询操作”**。

- **SQL 关键字**：**`SELECT`**
    
- **JDBC 方法**：`executeQuery()`
    
- **返回值**：`ResultSet` (结果集)
    
- **作用**：从数据库里把数据找出来，**不会修改**数据库里的内容。
    

**代码示例 (必背模版)：**

SQL

```
-- SQL 语句：查找所有年龄大于 18 岁的学生
SELECT * FROM student WHERE age > 18;
```

---

### 第二类：更新、插入与删除 (Create, Update, Delete) —— 会改变数据的

对应你图片里的 “更新、插入与删除操”。

在 JDBC 里，这三者被归为一类，统称为 “更新” (Update)，因为它们都会改变数据库里的数据。

#### 1. 插入操作 (Insert)

- **SQL 关键字**：**`INSERT INTO`**
    
- **作用**：往表里增加一条新数据。
    
- **代码示例**：
    
    SQL
    
    ```
    -- 给 student 表加个叫“王五”的人
    INSERT INTO student (name, age) VALUES ('王五', 22);
    ```
    

#### 2. 更新操作 (Update)

- **SQL 关键字**：**`UPDATE`**
    
- **作用**：修改表里已经存在的数据。
    
- **代码示例**：
    
    SQL
    
    ```
    -- 把学号是 101 的学生名字改成“赵六”
    UPDATE student SET name = '赵六' WHERE id = 101;
    ```
    
    - **注意**：一定要加 `WHERE` 条件，否则全表的人都会被改名！
        

#### 3. 删除操作 (Delete)

- **SQL 关键字**：**`DELETE FROM`**
    
- **作用**：从表里删掉数据。
    
- **代码示例**：
    
    SQL
    
    ```
    -- 删掉学号是 101 的学生
    DELETE FROM student WHERE id = 101;
    ```
    
    - **注意**：同样一定要加 `WHERE`，否则整个表会被清空！
        

---

### ⚠️ JDBC 中的关键区别 (考试考点)

在写 Java 代码时，这两类操作调用的方法是不同的，千万别搞混：

|**操作类型**|**SQL 关键字**|**JDBC 方法**|**返回值**|**含义**|
|---|---|---|---|---|
|**查询**|`SELECT`|**`executeQuery()`**|`ResultSet`|返回查到的数据表格|
|**增 / 删 / 改**|`INSERT`, `UPDATE`, `DELETE`|**`executeUpdate()`**|`int`|返回**有几行数据被改变了**|

**一句话总结：**

- 想看数据用 **SELECT**。
    
- 想加数据用 **INSERT**。
    
- 想改数据用 **UPDATE**。
    
- 想删数据用 **DELETE**。
    
- 在 Java 里，除了 SELECT 用 `executeQuery`，其他三个全用 `executeUpdate`。


`WHERE` 关键字在 SQL 里的作用非常关键，你可以把它理解为 **“过滤器”** 或者 **“精准定位器”**。

在你的这张图片 代码中：

SQL

```
DELETE FROM student WHERE id = 101;
```

这里的 `WHERE` 就像是一个**安检员**，对着表里的每一行数据问：“你的 id 是 101 吗？”

- 如果是，就放行（执行删除）。
    
- 如果不是，就跳过（不删）。
    

以下是关于 `WHERE` 你必须知道的三个核心点：

### 1. 它的作用：控制范围 (防误伤)

`WHERE` 后面跟的是**条件**。它告诉数据库：“我只想对**满足这些条件**的数据下手，别动其他人。”

- 如果没有 WHERE：
    
    SQL 语句默认对整张表生效。
    
    - `DELETE FROM student;` $\rightarrow$ **删光全校学生！** (极度危险)
        
    - `UPDATE student SET name = '张三';` $\rightarrow$ **全校人都改名叫张三！**
        
- 有了 WHERE：
    
    操作被限制在特定范围内。
    
    - `DELETE FROM student WHERE id = 101;` $\rightarrow$ 只删学号是 101 的那个倒霉蛋。
        

### 2. 它的语法结构

语法通常是：`WHERE 列名 运算符 值`

- **列名**：你要检查哪一列（比如 `id`, `age`, `name`）。
    
- **运算符**：怎么比？
    
    - `=` (等于)
        
    - `>` (大于) / `<` (小于)
        
    - `<>` 或 `!=` (不等于)
        
    - `AND` (并且) / `OR` (或者)
        
- **值**：比对的标准（比如 `101`, `'张三'`, `18`）。
    

### 3. 三大场景演示

- **查 (SELECT)**：只看一部分
    
    SQL
    
    ```
    -- 只把“成年人”找出来
    SELECT * FROM student WHERE age >= 18;
    ```
    
- **改 (UPDATE)**：只改一部分
    
    SQL
    
    ```
    -- 只把“id为5”的学生名字改成李四
    UPDATE student SET name = '李四' WHERE id = 5;
    ```
    
- **删 (DELETE)**：只删一部分 (你图片里的例子)
    
    SQL
    
    ```
    -- 只删“id为101”的数据
    DELETE FROM student WHERE id = 101;
    ```
    

一句话总结：

在写 UPDATE 和 DELETE 语句时，手写 WHERE 之前，绝对不要按回车！ 它是保护你数据库不被清空的最后一道防线。