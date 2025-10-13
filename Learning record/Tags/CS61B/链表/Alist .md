## 实现代码：
```public class AList {
    private int[] items;
    private int size;

    public AList() {
        items = new int[8];
        size = 0;
    }

    private void resize(int capacity) {
        int[] a = new int[capacity];
        System.arraycopy(items, 0, a, 0, size);
        items = a;
    }

    public int get(int i) {
        return items[i];
    }

    // ... 其他方法 ...
}
```
## 其他类型

```
public class AList<Glorp> {
    private Glorp[] items;
    private int size;

    public AList() {
        // Java 中不能直接 new T[]，所以通常用 new Object[] 然后强制类型转换
        items = (Glorp[]) new Object[8];
        size = 0;
    }

    private void resize(int cap) {
        Glorp[] a = (Glorp[]) new Object[cap];
        System.arraycopy(items, 0, a, 0, size);
        items = a;
    }

    public Glorp get(int i) {
        return items[i];
    }

    // ... 其他方法 ...
}
#### 1. 从链表 (Linked List) 到数组列表 (Array List)

- **链表的局限性**: 对于双向链表 (Doubly Linked Lists)，尽管 `addFirst`, `addLast`, `removeFirst`, `removeLast` 等操作很快 ，但
    
    `get(int i)` 操作在列表很长时会非常慢 。
    
- **原因**: `get(i)` 需要从头部的哨兵节点 (sentinel node) 开始，一步步扫描到目标位置，所以对于远离头尾的索引 `i` 来说效率很低 。
    
- **解决方案**: 采用数组来代替链式结构 。数组支持“随机访问” (Random Access)，从任何位置检索数据的速度都非常快，且这个速度与数组的大小无关 。
    

#### 2. 朴素数组列表 (Naive AList) 的实现

- **核心思想**: 使用一个数组的子集来存储列表的元素 。
    
- **基本结构**:
    
    - 一个私有数组用于存储元素，例如
        
        `private int[] items;` 。
        
    - 一个私有变量用于记录当前元素的数量，例如
        
        `private int size;` 。
        
- **AList 的不变量 (Invariants)**：这些是必须始终为真的规则。
    
    - `size` 的值永远是 `AList` 中元素的数量 。
        
    - 下一个要插入元素的位置永远是
        
        `size` 。
        
    - 列表中的最后一个元素永远在
        
        `size - 1` 的位置 。
        
- **`removeLast` 操作**:
    
    - 该操作会获取
        
        `items[size - 1]` 的值作为返回值，然后将 `size` 减 1 。
        
    - 对于原生类型（如
        
        `int`）的列表，将删除的元素位置设为 0 并非必须，因为这不影响不变量的正确性 。
        

#### 3. 数组的动态扩容 (Resizing)

- **问题**: 当 `AList` 内部的数组满了 (`size == items.length`)，就无法再通过 `addLast` 添加新元素 。
    
- **解决方案：扩容**
    
    1. 创建一个容量更大的新数组 。
        
    2. 使用
        
        `System.arraycopy(...)` 将旧数组的所有元素复制到新数组中 。
        
    3. 将
        
        `AList` 的 `items` 引用指向这个新数组 。
        
- **扩容策略的性能影响**:
    
    - **增量扩容 (Additive Resizing)**: 每次扩容时只增加一个固定的量（例如，`resize(size + 1)`) 。这种方式性能极差 。例如，将一个满的 100 容量数组扩容到 1000，需要大约 500,000 次的元素复制操作 (
        
        `101 + 102 + ... + 1000`) 。
        
    - **几何/倍率扩容 (Geometric Resizing)**: 每次扩容时将容量乘以一个系数（例如，`resize(size * RFACTOR)`) 。这种方式性能非常好 ，Python 的
        
        `list` 就是这样实现的 。
        
- **缩容 (Shrinking)**: 当大量元素被删除后，数组的“使用率” (`R = size / items.length`) 会变得很低，造成空间浪费 。一个典型的解决方案是当使用率低于某个阈值（如 0.25）时，将数组容量减半 。
    

#### 4. 泛型数组列表 (Generic AList)

- **目的**: 创建一个可以存储任意对象类型（而不仅仅是 `int`）的 `AList` 。
    
- **实现**: 使用泛型，例如 `public class AList<Glorp>` 。内部数组也变成
    
    `private Glorp[] items;` 。
    
- **泛型数组的创建**:
    
    - 在 Java 中，你不能直接创建泛型数组，
        
        `new Glorp[capacity]` 会导致“泛型数组创建 (generic array creation)”错误 。
        
    - 正确的做法是创建一个
        
        `Object` 数组，然后强制类型转换为泛型数组：`items = (Glorp[]) new Object[8];` 。这会产生一个编译器警告，但应该忽略它 。
        

#### 5. 内存管理：闲散 (Loitering) 问题

- **定义**: “闲散 (Loitering)” 指的是代码中仍然持有不再需要的对象的引用 。
    
- **问题**: 在泛型 `AList` 中，如果 `removeLast` 操作只减少 `size` 而不清空数组中对应位置的引用，那么这个引用依然存在 。只要引用存在，Java 的垃圾回收器就无法销毁该对象，从而导致内存浪费（内存泄漏） 。如果对象本身很大（例如，一张图片），这个问题会非常严重 。
    
- **解决方案**: 在删除对象时，必须将数组对应位置的引用设为 `null` 。这会断开引用，让垃圾回收器可以回收内存 。这种操作对于原生类型的
    
    `AList` 是不必要的 。
    

#### 6. 抽象与封装 (Obscurantism)

- **概念**: 这是计算机科学中“抽象层”的一个概念，指的是一个类的使用者不应该也不需要知道它的内部实现细节 。
    
- **实现**: Java 通过 `private` 等关键字来强制实现这种封装 。
    
- **编程实践**: 优秀的程序员在编写一个类时，也会对自己隐藏细节。例如，在编写 `addFirst` 方法时，应该完全信任 `resize` 方法能够正常工作，而不需要去思考 `resize` 的具体实现 。将编程任务分解成小的函数模块，并对这些小模块进行充分的测试，是实现这一点的关键 。```