
## 1. `if` 语句

`if` 语句用于根据条件执行代码块，如果条件为真（`true`），则执行其中的语句。

```java
if (条件) {
    // 如果条件为真，执行的代码
}
```

- **示例**：

```java
int x = 10;
if (x > 0) {
    System.out.println("x 是正数");
}
```

## 2. `if-else` 语句

`if-else` 语句在条件为假（`false`）时提供替代的代码块。

```java
if (条件) {
    // 如果条件为真，执行的代码
} else {
    // 如果条件为假，执行的代码
}
```

- **示例**：

```java
int x = -5;
if (x > 0) {
    System.out.println("x 是正数");
} else {
    System.out.println("x 不是正数");
}
```

## 3. `if-else if-else` 语句

用于多个条件判断，依次检查每个条件，直到找到一个为真的条件。

```java
if (条件1) {
    // 条件1为真时执行
} else if (条件2) {
    // 条件2为真时执行
} else {
    // 所有条件都为假时执行
}
```

- **示例**：

```java
int score = 85;
if (score >= 90) {
    System.out.println("等级：A");
} else if (score >= 80) {
    System.out.println("等级：B");
} else {
    System.out.println("等级：C");
}
```

## 4. 嵌套 `if` 语句

可以在 `if` 语句中嵌套另一个 `if` 语句，用于更复杂的条件判断。

```java
if (条件1) {
    if (条件2) {
        // 条件1和条件2都为真时执行
    }
}
```

- **示例**：

```java
int x = 10;
int y = 5;
if (x > 0) {
    if (y > 0) {
        System.out.println("x 和 y 都是正数");
    }
}
```

## 5. 条件表达式

条件必须是返回 `boolean` 类型的表达式（`true` 或 `false`），如比较运算符（`>`, `<`, `==`, `!=`, `>=`, `<=`）或逻辑运算符（`&&`, `||`, `!`）。

- **示例**：

```java
int a = 5;
int b = 3;
if (a > b && a != 0) {
    System.out.println("a 大于 b 且不为零");
}
```

## 6. 注意事项

- 条件括号 `()` 是必需的，代码块 `{}` 在单条语句时可省略，但建议始终使用以提高可读性。
- 每条语句必须以分号 `;` 结束。
- 嵌套层次不宜过深，以保持代码清晰。