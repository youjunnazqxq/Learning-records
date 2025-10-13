 好的，我很乐意为你介绍 SQL 中 **`聚合函数（Aggregate Functions）`** 的基本用法。

聚合函数在 SQL 中扮演着非常重要的角色，它们用于对一组行（通常是某个列的所有值）进行计算，并返回一个单一的汇总值。这与常规函数（如 `UPPER()` 或 `SUBSTRING()`）不同，后者是对每行数据独立进行操作。

最常见的聚合函数包括：

- `COUNT()`：计算行数。
    
- `SUM()`：计算某一列的总和。
    
- `AVG()`：计算某一列的平均值。
    
- `MAX()`：找出某一列的最大值。
    
- `MIN()`：找出某一列的最小值。
    

### 基本用法

聚合函数通常与 `SELECT` 语句一起使用。下面我们通过一些例子来介绍它们的基本用法。

假设我们有一个名为 `employees` 的表，其中包含以下列：`id`, `name`, `department`, `salary`, `hire_date`。

|id|name|department|salary|hire_date|
|---|---|---|---|---|
|1|Alice|Sales|50000|2020-01-15|
|2|Bob|IT|70000|2019-05-20|
|3|Carol|Sales|60000|2021-03-10|
|4|David|IT|80000|2018-11-01|
|5|Eve|HR|55000|2022-07-25|

#### 1. `COUNT()`

`COUNT()` 函数用于计算行数。

- **计算表中的总行数：**
    
    SQL
    
    ```
    SELECT COUNT(*) FROM employees;
    ```
    
    - **结果：** 5
        
    - `COUNT(*)` 计算的是所有行，包括包含 NULL 值的行。
        
- **计算非空值的行数：**
    
    SQL
    
    ```
    SELECT COUNT(hire_date) FROM employees;
    ```
    
    - 如果 `hire_date` 列中有 NULL 值，`COUNT(hire_date)` 将只计算非 NULL 值的行数。
        

#### 2. `SUM()`

`SUM()` 函数用于计算数值列的总和。

- **计算所有员工的总薪水：**
    
    SQL
    
    ```
    SELECT SUM(salary) FROM employees;
    ```
    
    - **结果：** 315000
        

#### 3. `AVG()`

`AVG()` 函数用于计算数值列的平均值。

- **计算所有员工的平均薪水：**
    
    SQL
    
    ```
    SELECT AVG(salary) FROM employees;
    ```
    
    - **结果：** 63000 (`315000 / 5`)
        

#### 4. `MAX()` 和 `MIN()`

`MAX()` 和 `MIN()` 分别用于找出某一列的最大值和最小值。

- **找出最高薪水：**
    
    SQL
    
    ```
    SELECT MAX(salary) FROM employees;
    ```
    
    - **结果：** 80000
        
- **找出最低薪水：**
    
    SQL
    
    ```
    SELECT MIN(salary) FROM employees;
    ```
    
    - **结果：** 50000
        

### 结合 `GROUP BY` 使用

聚合函数最强大的用法是与 `GROUP BY` 子句结合使用。`GROUP BY` 子句将表中的行分组，然后对每个组应用聚合函数。

#### 示例：

- **按部门计算员工数量：**
    
    SQL
    
    ```
    SELECT department, COUNT(*) AS number_of_employees
    FROM employees
    GROUP BY department;
    ```
    
    - 结果：
        
        | department | number_of_employees |
        
        |------------|---------------------|
        
        | Sales | 2 |
        
        | IT | 2 |
        
        | HR | 1 |
        
    - **解释：** 这个查询将员工按 `department` 分组，然后对每个部门组内的员工数量进行计数。
        
- **按部门计算平均薪水和总薪水：**
    
    SQL
    
    ```
    SELECT department, AVG(salary) AS avg_salary, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department;
    ```
    
    - 结果：
        
        | department | avg_salary | total_salary |
        
        |------------|------------|--------------|
        
        | Sales | 55000 | 110000 |
        
        | IT | 75000 | 150000 |
        
        | HR | 55000 | 55000 |
        

### 结合 `HAVING` 使用

`HAVING` 子句用于过滤 `GROUP BY` 后的分组结果。它类似于 `WHERE` 子句，但 `WHERE` 是在分组之前过滤行，而 `HAVING` 是在分组之后过滤组。

- **找出平均薪水高于 60000 的部门：**
    
    SQL
    
    ```
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 60000;
    ```
    
    - 结果：
        
        | department | avg_salary |
        
        |------------|------------|
        
        | IT | 75000 |
        

**总结：**

|函数|作用|
|---|---|
|`COUNT()`|计数|
|`SUM()`|求和|
|`AVG()`|求平均值|
|`MAX()`|求最大值|
|`MIN()`|求最小值|

聚合函数是 SQL 中进行数据分析和报表生成的基础。掌握它们与 `GROUP BY` 和 `HAVING` 的结合使用，能够帮助你从数据中提取有价值的汇总信息。


##[[group]]

