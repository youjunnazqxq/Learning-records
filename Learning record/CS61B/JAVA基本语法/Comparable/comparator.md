

当然，我们来为 `Comparator` 也做一个清晰的总结。

### `Comparator` 接口总结

**1. 核心作用**

- `Comparator` 用于定义一个类的 **“外部比较规则”** 或 **“自定义排序”**。它像一个独立的“裁判”，不属于被比较的类本身。
    
- 当你希望用多种不同方式排序（比如一会按姓名，一会按成绩），或者要排序的类没有实现 `Comparable` 接口时，就应该使用 `Comparator`。
    

**2. 语法规则**

- **创建新类**: 你需要创建一个 **新的、独立的** 类，让它 `implements Comparator<YourClassName>`。
    
- **实现方法**: 你必须实现 `public int compare(YourClassName o1, YourClassName o2)` 这个方法。注意，它接收两个待比较的对象作为参数。
    
- **`compare` 方法的返回值**:
    
    - `o1` 对象排在 `o2` 对象 **之前**，返回 **负整数**。
        
    - `o1` 对象与 `o2` 对象 **相等**，返回 **零**。
        
    - `o1` 对象排在 `o2` 对象 **之后**，返回 **正整数**。
        

---

### 3. 实用例子

我们继续用 `Student` 类为例。它的自然顺序是按学号排，现在我们需要一个按姓名排序的外部比较器。

**比较器类 `SortByNameComparator.java`**

Java

```
import java.util.Comparator;

// 这是一个独立的类，存在的唯一目的就是为了比较两个 Student 对象的姓名
public class SortByNameComparator implements Comparator<Student> {

    @Override
    public int compare(Student s1, Student s2) {
        // 直接利用 String 类自带的 compareTo 方法来比较 s1 和 s2 的姓名
        return s1.getName().compareTo(s2.getName());
    }
}
```

**使用示例 `Main.java`**

Java

```
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Student> studentList = new ArrayList<>();
        studentList.add(new Student(105, "Wang Wu"));
        studentList.add(new Student(101, "Zhang San"));
        studentList.add(new Student(103, "Li Si"));

        System.out.println("原始列表: " + studentList);

        // 调用 Collections.sort() 的重载版本
        // 第二个参数传入我们自定义的比较器实例
        Collections.sort(studentList, new SortByNameComparator());

        System.out.println("按姓名排序后: " + studentList);
    }
}
```

**输出结果:**

```
原始列表: [Student{id=105, name='Wang Wu'}, Student{id=101, name='Zhang San'}, Student{id=103, name='Li Si'}]
按姓名排序后: [Student{id=103, name='Li Si'}, Student{id=105, name='Wang Wu'}, Student{id=101, name='Zhang San'}]
```

这个例子展示了 `Comparator` 的灵活性：我们可以创建任意多个这样的“裁判”类（比如按成绩排序、按年龄排序等），然后在需要时把对应的“裁判”传给 `sort` 方法，实现不同的排序需求。