`Math` 类是 Java 提供的一个**工具类**，专门用来做数学计算。

它有两个最大的特点：

1. **不用 `new`**：它的构造方法是私有的，你不能创建它的对象。
    
2. **全是 `static`**：所有方法直接用 **`Math.方法名()`** 调用即可。
    

为了方便记忆，我们可以把它的常用方法分为 **5 大类**：

### 1. 取整三剑客 (必考)

这三个方法处理小数的方式不同，非常容易混淆，请务必分清：

- **`double ceil(double a)`** (天花板)
    
    - **含义**：**向上取整**。只要有小数（哪怕是 0.1），就往大了算。
        
    - `Math.ceil(10.1)` $\rightarrow$ `11.0`
        
    - `Math.ceil(-10.1)` $\rightarrow$ `-10.0` (注意负数向大取整是接近0)
        
- **`double floor(double a)`** (地板)
    
    - **含义**：**向下取整**。哪怕是 0.9，也直接抹掉。
        
    - `Math.floor(10.9)` $\rightarrow$ `10.0`
        
    - `Math.floor(-10.1)` $\rightarrow$ `-11.0`
        
- **`long round(double a)`** (四舍五入)
    
    - **含义**：标准的**四舍五入**。
        
    - **原理**：实际上是 `Math.floor(a + 0.5)`。
        
    - `Math.round(10.5)` $\rightarrow$ `11`
        
    - `Math.round(10.4)` $\rightarrow$ `10`
        

---

### 2. 比较与绝对值 (最基础)

- **`int abs(int a)`**
    
    - **含义**：取**绝对值**（Absolute Value）。不管正负，出来都是正数。
        
    - `Math.abs(-10)` $\rightarrow$ `10`
        
- **`int max(int a, int b)`**
    
    - **含义**：取两个数中的**最大值**。
        
    - `Math.max(10, 20)` $\rightarrow$ `20`
        
- **`int min(int a, int b)`**
    
    - **含义**：取两个数中的**最小值**。
        
    - `Math.min(10, 20)` $\rightarrow$ `10`
        

---

### 3. 指数与开方 (高级运算)

- **`double pow(double a, double b)`**
    
    - **含义**：计算 **a 的 b 次方** ($a^b$)。
        
    - `Math.pow(2, 3)` $\rightarrow$ `8.0` ($2^3$)
        
    - `Math.pow(3, 2)` $\rightarrow$ `9.0` ($3^2$)
        
- **`double sqrt(double a)`**
    
    - **含义**：计算 **平方根** (Square Root, $\sqrt{a}$)。
        
    - `Math.sqrt(16)` $\rightarrow$ `4.0`
        
    - `Math.sqrt(2)` $\rightarrow$ `1.414...`
        

---

### 4. 随机数 (最常用)

- **`double random()`**
    
    - **含义**：生成一个 **[0.0, 1.0)** 之间的随机小数。
        
    - **范围**：包含 0.0，**不包含** 1.0（比如可能是 0.99999）。
        
    - **场景**：通常用来生成指定范围的随机整数。
        
    - _公式：生成 1 到 100 之间的随机整数_
        
        Java
        
        ```
        int num = (int)(Math.random() * 100) + 1;
        ```
        

---

### 5. 重要常量

- **`Math.PI`**：圆周率 $\pi$ (3.1415926...)
    
- **`Math.E`**：自然对数的底数 $e$ (2.71828...)
    

---

### 总结一张速查表

|**方法**|**作用**|**记忆技巧**|**返回值类型**|
|---|---|---|---|
|**`abs`**|绝对值|负变正|int/double|
|**`max`** / **`min`**|最大/最小|PK 二选一|int/double|
|**`ceil`**|向上取整|往天花板靠|**double** (带.0)|
|**`floor`**|向下取整|往地板靠|**double** (带.0)|
|**`round`**|四舍五入|+0.5 再 floor|**long/int** (整数)|
|**`random`**|随机数|[0, 1)|double|
|**`pow`**|次方|Power (力量)|double|
|**`sqrt`**|开根号|Square Root|double|