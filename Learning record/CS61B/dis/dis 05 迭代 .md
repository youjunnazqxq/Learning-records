### 本次练习的核心知识点总结

1. **接口：`Iterable` 与 `Iterator` 的契约关系**
    
    - **学到了什么**：我们明白了 `Iterable` 和 `Iterator` 是一对协同工作的接口。一个类实现 `Iterable` 就像是做出了一个承诺：“我是可以被遍历的，来我这里拿遍历工具吧”。而它通过 `iterator()` 方法提供的那个 `Iterator` 对象，就是真正负责一步步遍历（`hasNext()`, `next()`）的那个“工具”。
        
    - **对应练习**：[热身问题1, 2, 3 ] 和 [OHQueue问题 ]。
        
2. **自定义迭代逻辑：让遍历更“智能”**
    
    - **学到了什么**：迭代器不只是简单地从头到尾走一遍。我们可以通过在 `hasNext()` 和 `next()` 中加入自己的逻辑，实现复杂的遍历行为，比如**过滤**不符合条件的元素（`OHIterator` ）或者
        
        **跳过**某些元素（`TYIterator` ）。
        
    - **对应练习**：[OHIterator的筛选功能 ] 和 [TYIterator的跳过功能 ]。
        
3. **继承与复用：站在巨人的肩膀上**
    
    - **学到了什么**：通过 `extends` 关键字，一个子类可以继承父类的所有功能，并且只重写（override）自己需要改变的部分。这让我们避免了重复编写大量代码。
        
    - **对应练习**：[第三题中 `TYIterator` 继承 `OHIterator` ]。
        
4. **多态：方法的重写 (Override) 与重载 (Overload)**
    
    - **学到了什么**：这是Java面向对象编程的基石。
        
        - **重写 (Override)**：子类重新实现了父类的方法。调用哪个版本，取决于对象的**实际类型**（运行时确定）。
            
        - **重载 (Overload)**：一个类里有多个同名但参数不同的方法。调用哪个版本，取决于参数的**声明类型**（编译时确定）。
            
    - **对应练习**：[第四题附加题 ]，里面几乎每行代码都在考察这两个概念的区别。
        
5. **类设计：分离关注点与内部类**
    
    - **学到了什么**：我们探讨了两种设计模式。将 `OHRequest` 和 `OHQueue` 分成独立文件，可以使每个类的职责更单一，更清晰。而将 `OHRequest` 作为 `OHQueue` 的私有内部类，则能更好地封装实现细节。这两种选择都是有效的，取决于具体的场景和设计目标。
        

### 最终代码实例

下面是我们一起构建的 `OHQueue` 和 `OHIterator` 的完整可用代码，这是一个将上述知识点融会贯通的绝佳范例。

Java

```
import java.util.Iterator;
import java.util.NoSuchElementException;

// 为了方便在一个文件里展示，我们将OHIterator作为OHQueue的静态内部类
// 这体现了我们讨论过的第二种设计思路
public class OHQueue implements Iterable<OHQueue.OHRequest> {

    // --- OHRequest 数据节点定义 ---
    public static class OHRequest {
        public String description;
        public String name;
        public OHRequest next;

        public OHRequest(String description, String name, OHRequest next) {
            this.description = description;
            this.name = name;
            this.next = next;
        }
    }

    // --- OHIterator 迭代器实现 ---
    private static class OHIterator implements Iterator<OHRequest> {
        OHRequest curr;

        public OHIterator(OHRequest queue) {
            this.curr = queue;
            // 在构造时就找到第一个“好”的请求
            while (curr != null && !isGood(curr.description)) {
                curr = curr.next;
            }
        }

        private boolean isGood(String description) {
            return description != null && description.length() > 5;
        }

        @Override
        public boolean hasNext() {
            return curr != null;
        }

        @Override
        public OHRequest next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            OHRequest requestToReturn = curr;
            // 移动到下一个节点
            curr = curr.next;
            // 循环找到下一个“好”的节点
            while (curr != null && !isGood(curr.description)) {
                curr = curr.next;
            }
            return requestToReturn;
        }
    }

    // --- OHQueue 本身 ---
    private OHRequest firstRequest;

    public OHQueue(OHRequest queue) {
        this.firstRequest = queue;
    }

    @Override
    public Iterator<OHRequest> iterator() {
        return new OHIterator(this.firstRequest);
    }


    // --- Main方法测试 ---
    public static void main(String[] args) {
        OHRequest s5 = new OHRequest("I deleted all of my files", "Allyson", null);
        OHRequest s4 = new OHRequest("conceptual: what is Java", "Omar", s5);
        OHRequest s3 = new OHRequest("git: I never did lab 1", "Connor", s4);
        OHRequest s2 = new OHRequest("help", "Hug", s3); // 描述太短，会被跳过
        OHRequest s1 = new OHRequest("no I haven't tried stepping through", "Itai", s2);

        OHQueue officeHoursQueue = new OHQueue(s1);

        System.out.println("队列中符合条件的同学有：");
        for (OHRequest request : officeHoursQueue) {
            System.out.println(request.name);
        }
    }
}
```

来源