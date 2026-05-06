根据《Java大学实用教程》第四章的知识体系，`import` 语句是连接不同包（package）的桥梁。虽然它看起来很简单，但在实际编写代码时有几个非常关键的**注意点**，这也是考试和面试中容易踩坑的地方。

我为您总结了以下 5 个核心注意点：

### 1. 位置必须“前不着村，后不着店”

- **规则**：`import` 语句必须写在 **`package` 语句之后**，**类定义（class）之前**。
    
- **顺序**：
    
    1. `package ...;` （如果有，必须是第一行）
        
    2. `import ...;` （可以有多行）
        
    3. `public class ...`
        

### 2. `java.lang` 包是“免签”的

- **规则**：Java 语言的核心类库 `java.lang` 包下的所有类（如 `String`, `System`, `Math`, `Object`, `Thread` 等）是由编译器**默认自动导入**的。
    
- **注意**：你不需要写 `import java.lang.*;`，写了也不报错，但会被视为多余代码。
    

### 3. 通配符 `*` 的误区

- **用法**：`import java.util.*;` 表示导入 `java.util` 包下所有的**类**。
    
- **坑点**：
    
    - **不包含子包**：它只管 `java.util` 这一层，不管 `java.util.zip` 这种子包里的类。如果你要用子包里的类，必须单独再导入：`import java.util.zip.*;`
        
    - **性能影响**：使用 `*` **不会**影响程序运行时的速度（JVM 加载类是按需加载），但可能会稍微拖慢一点**编译**速度（编译器要花时间去找）。
        
    - **推荐**：为了代码清晰，规范开发中（如阿里巴巴开发手册）通常建议**显式导入具体类**（如 `import java.util.List;`），尽量少用 `*`，以免发生命名冲突。
        

### 4. “同名类”打架怎么办？

- **场景**：假设 `java.util` 包里有个 `Date` 类，`java.sql` 包里也有个 `Date` 类。如果你同时写了：
    
    Java
    
    ```
    import java.util.*;
    import java.util.sql.*;
    ```
    
- **冲突**：当你代码里写 `Date d = new Date();` 时，编译器会懵圈，报错“reference to Date is ambiguous”（引用不明确）。
    
- **解决**：这种情况下，**必须使用全限定名（完整包名）** 来指定其中一个：
    
    Java
    
    ```
    java.util.Date date1 = new java.util.Date();
    java.sql.Date date2 = new java.sql.Date();
    ```
    

### 5. 同包无需导入

- **规则**：如果类 A 和类 B 在**同一个包**下（同一个文件夹里），类 A 使用类 B 时**不需要**写 `import`。
    

---

### 专项练习题

Java Import 语句专项测试

1月10日 15:05