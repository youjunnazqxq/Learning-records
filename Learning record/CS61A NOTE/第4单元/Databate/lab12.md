在 SQL 中，**分组（GROUP BY）** 和 **聚合（聚合函数）** 是处理分组统计问题的关键工具，广泛用于数据汇总、统计分析等场景。下面是它们的详细解释：

---

## 一、聚合函数（Aggregate Functions）

聚合函数用于对一组值进行计算，并返回一个单一的结果。常见的聚合函数有：

|函数名|作用|示例说明|
|---|---|---|
|`COUNT()`|统计数量|`COUNT(*)` 统计行数|
|`SUM()`|求和|`SUM(salary)` 统计工资总和|
|`AVG()`|求平均值|`AVG(score)` 平均分数|
|`MAX()`|求最大值|`MAX(age)` 最大年龄|
|`MIN()`|求最小值|`MIN(age)` 最小年龄|

---

## 二、分组（GROUP BY）语法与作用

### 语法：

```sql
SELECT 列名1, 聚合函数(列名2)
FROM 表名
GROUP BY 列名1;
```

### 作用：

`GROUP BY` 用于将查询结果按照某列的值进行分组，然后对每组使用聚合函数进行计算。**每一组都会返回一行结果**。

---

## 三、简单例子讲解

假设有一个学生成绩表 `scores`：

|name|subject|score|
|---|---|---|
|Alice|Math|85|
|Alice|English|90|
|Bob|Math|78|
|Bob|English|88|

### 1. 查询每个学生的总分：

```sql
SELECT name, SUM(score) AS total_score
FROM scores
GROUP BY name;
```

**结果：**

|name|total_score|
|---|---|
|Alice|175|
|Bob|166|

### 2. 查询每个科目的平均分：

```sql
SELECT subject, AVG(score) AS avg_score
FROM scores
GROUP BY subject;
```

**结果：**

|subject|avg_score|
|---|---|
|Math|81.5|
|English|89|

---

## 四、结合 `WHERE` 和 `HAVING`

- `WHERE`：在分组前过滤数据；
    
- `HAVING`：在分组后过滤分组结果（**不能用 WHERE 过滤聚合结果**）。
    

### 示例：只查询总分大于170的学生：

```sql
SELECT name, SUM(score) AS total_score
FROM scores
GROUP BY name
HAVING total_score > 170;
```

---

## 五、注意事项

1. `SELECT` 语句中，**除了聚合函数的列，其他列必须出现在 `GROUP BY` 中**；
    
2. `GROUP BY` 是在聚合函数之前执行的；
    
3. 如果不使用聚合函数但用 `GROUP BY`，就只会返回每组的一条记录。
    

---

如果你有具体的表结构或题目，我可以帮你写出针对性的 SQL 示例。