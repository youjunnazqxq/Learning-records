好的，我们来详细介绍一下 SQL 中的 `GROUP BY` 子句。

### `GROUP BY` 子句

`GROUP BY` 子句用于将 `SELECT` 语句的结果集按照一个或多个列的值进行分组。它的主要目的是将具有相同值的行汇总在一起，以便对每个组应用聚合函数（如 `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`）。

**简单来说，`GROUP BY` 的作用就是 "把相同的东西分到一组"**。

### 基本语法

`GROUP BY` 总是跟在 `FROM` 或 `WHERE` 子句之后，在 `ORDER BY` 子句之前。

SQL

```
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1, column3...
ORDER BY some_column;
```

**重要规则：**

- **在 `SELECT` 列表中，所有非聚合列（即没有被聚合函数包裹的列）都必须出现在 `GROUP BY` 子句中。**
    
- 你不能在 `WHERE` 子句中使用聚合函数，因为 `WHERE` 是在分组之前过滤行。如果你需要过滤分组后的结果，请使用 `HAVING` 子句。
    

### 例子

让我们继续使用之前的 `employees` 表：

|id|name|department|salary|hire_date|
|---|---|---|---|---|
|1|Alice|Sales|50000|2020-01-15|
|2|Bob|IT|70000|2019-05-20|
|3|Carol|Sales|60000|2021-03-10|
|4|David|IT|80000|2018-11-01|
|5|Eve|HR|55000|2022-07-25|

#### 1. 按单个列分组

**需求：** 统计每个部门的员工人数。

- **没有 `GROUP BY`：** 如果你直接使用 `COUNT(*)`，你只会得到一个总数，无法按部门区分。
    
    SQL
    
    ```
    SELECT COUNT(*) FROM employees; -- 结果是 5
    ```
    
- **使用 `GROUP BY`：**
    
    SQL
    
    ```
    SELECT department, COUNT(*) AS employee_count
    FROM employees
    GROUP BY department;
    ```
    
    - **执行过程：**
        
        1. 数据库扫描 `employees` 表。
            
        2. 找到 `department` 列中的所有不同值：'Sales', 'IT', 'HR'。
            
        3. 将所有 `department` 为 'Sales' 的行分到一组，所有 'IT' 的行分到一组，所有 'HR' 的行分到一组。
            
        4. 对每个分组（`Sales`, `IT`, `HR`）分别执行 `COUNT(*)` 聚合函数。
            
    - 结果：
        
        | department | employee_count |
        
        |------------|----------------|
        
        | Sales | 2 |
        
        | IT | 2 |
        
        | HR | 1 |
        

#### 2. 按多个列分组

**需求：** 统计每个部门中，不同薪水范围的员工人数。

假设我们添加一个 `gender` 列。

|id|name|department|gender|salary|
|---|---|---|---|---|
|1|Alice|Sales|F|50000|
|2|Bob|IT|M|70000|
|3|Carol|Sales|F|60000|
|4|David|IT|M|80000|
|5|Eve|HR|F|55000|
|6|Frank|Sales|M|70000|

**需求：** 统计每个部门中，男性和女性员工的人数。

SQL

```
SELECT department, gender, COUNT(*) AS employee_count
FROM employees
GROUP BY department, gender;
```

- **执行过程：**
    
    1. 数据库按 `(department, gender)` 组合进行分组。
        
    2. 找到所有独特的组合：('Sales', 'F'), ('Sales', 'M'), ('IT', 'M'), ('HR', 'F')。
        
    3. 对每个组合分别进行计数。
        
- 结果：
    
    | department | gender | employee_count |
    
    |------------|--------|----------------|
    
    | Sales | F | 2 |
    
    | Sales | M | 1 |
    
    | IT | M | 2 |
    
    | HR | F | 1 |
    

#### 3. 与 `WHERE` 和 `HAVING` 的配合使用

**需求：** 统计薪水高于 60000 的员工中，每个部门的平均薪水。

SQL

```
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE salary > 60000
GROUP BY department;
```

- **解释：**
    
    1. **`WHERE salary > 60000`**: 首先，`WHERE` 子句会过滤掉所有薪水不高于 60000 的行。
        
    2. **`GROUP BY department`**: 然后，对剩下的行（Bob, David, Frank）按 `department` 分组。
        
    3. **`SELECT ... AVG(salary)`**: 最后，对每个分组计算平均薪水。
        
- 结果：
    
    | department | avg_salary |
    
    |------------|------------|
    
    | IT | 75000 |
    
    | Sales | 70000 |
    

**需求：** 统计员工人数超过 1 人的部门的平均薪水。

SQL

```
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;
```

- **解释：**
    
    1. **`GROUP BY department`**: 首先，按部门进行分组。
        
    2. **`HAVING COUNT(*) > 1`**: 然后，`HAVING` 子句对**分组后的结果**进行过滤，只保留那些 `COUNT(*)` 大于 1 的分组。
        
    3. **`SELECT ...`**: 最后，显示符合条件的部门及其聚合结果。
        
- 结果：
    
    | department | employee_count | avg_salary |
    
    |------------|----------------|------------|
    
    | Sales | 3 | 60000 |
    
    | IT | 2 | 75000 |
    

**总结 `WHERE` vs `HAVING`：**

- `WHERE` 过滤**行**，在**分组之前**执行。
    
- `HAVING` 过滤**组**，在**分组之后**执行，并且可以包含聚合函数。
    

`GROUP BY` 是 SQL 中进行数据汇总和分析的基石，掌握它对于进行数据报告和洞察至关重要。