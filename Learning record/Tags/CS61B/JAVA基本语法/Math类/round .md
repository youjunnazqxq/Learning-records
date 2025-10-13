`Math.round()` 方法在 Java 中用于执行**四舍五入**操作。
### `Math.round()` 的作用

`Math.round()` 是 `java.lang.Math` 类中的一个静态方法，它根据**标准四舍五入规则**将一个浮点数（`float` 或 `double`）转换为最接近的整数。

它有两个重载版本：

1. **`long round(double a)`**: 接受一个 `double` 类型的参数，返回一个 `long` 类型的值。
    
2. **`int round(float a)`**: 接受一个 `float` 类型的参数，返回一个 `int` 类型的值。
    

**四舍五入规则：**

- 如果小数部分 **大于或等于 0.5** (或 0.5f)，则向上取整。
    
- 如果小数部分 **小于 0.5** (或 0.5f)，则向下取整。
    

**示例：**

- `Math.round(3.4)` 会返回 `3`
    
- `Math.round(3.5)` 会返回 `4`
    
- `Math.round(3.6)` 会返回 `4`
    
- `Math.round(-3.4)` 会返回 `-3`
    
- `Math.round(-3.5)` 会返回 `-3` (注意：对于负数，-3.5 向上取整是 -3，向下取整是 -4)
    
- `Math.round(-3.6)` 会返回 `-4`
    

在您提供的代码片段 `int result = Math.round(quotient);` 中：

- `quotient` 变量很可能是一个 `float` 类型（因为返回类型是 `int`），或者它是一个 `double` 类型，但编译器会将其结果向下转型为 `int`。
    
- `Math.round()` 将 `quotient` 的值进行四舍五入，然后将结果（一个整数）赋给 `result` 变量。
    

---

### 与 `Math.floor()` 和 `Math.ceil()` 的区别

- **`Math.round()`**: 四舍五入到最接近的整数。
    
- **`Math.floor()`**: 向下取整，返回小于或等于参数的最大（最接近负无穷大）双精度值。
    
    - `Math.floor(3.9)` 返回 `3.0`
        
    - `Math.floor(-3.1)` 返回 `-4.0`
        
- **`Math.ceil()`**: 向上取整，返回大于或等于参数的最小（最接近正无穷大）双精度值。
    
    - `Math.ceil(3.1)` 返回 `4.0`
        
    - `Math.ceil(-3.9)` 返回 `-3.0`
        

`Math.round()` 是一个非常常用的方法，特别是在需要将浮点数结果显示为整数，并希望遵循常规四舍五入规则的场景中。