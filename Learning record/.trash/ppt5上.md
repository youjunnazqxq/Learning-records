这份课件主要讲解了人工智能与博弈中的核心算法：**期望极小化搜索 (Expectimax Search)**。以下为你提取的重点知识和核心英文术语：

### 期望极小化搜索 (Expectimax Search) *

该算法主要用于存在**不确定结果 (Uncertain outcomes)**的博弈或搜索环境中 。

- 导致结果未知的原因包括：**显式随机性 (Explicit randomness)**（例如掷骰子）、**不可预测的对手 (Unpredictable opponents)**（例如幽灵的随机移动）以及**动作失败 (Actions can fail)**（例如机器人车轮打滑） 。
    
- 与Minimax算法计算最坏情况不同，Expectimax的节点值反映的是**平均情况结果 (Average-case outcomes)**或期望值 。
    
- 树结构中的**最大化节点 (Max nodes)**处理逻辑与Minimax搜索中完全一致 。
    
- 树结构中新增了**机会节点 (Chance nodes)**，它们类似于极小化节点，但计算的是其子节点的**期望效用 (Expected utilities)**，即平均期望值 。
    

### 概率基础理论 (Probabilities) *

**随机变量 (Random variable)**代表一个结果未知的事件 。

- **概率分布 (Probability distribution)**是为各种可能的结果分配权重的机制 。
    
- 概率遵循严格的数学定律：所有的概率都必须是**非负的 (Non-negative)**，且所有可能结果的概率总和必须等于1 。
    
- 期望值的计算逻辑为：将每个后继状态的概率与其值相乘，并对所有的后继状态进行累加求和 。
    

### 剪枝的局限性 (Pruning Limitations)

- 在Expectimax搜索中**无法进行剪枝 (Cannot skip/prune)** 。
    
- 无法跳过特定节点的原因是，即使是极端的数值也会主导平均值的计算结果，因此必须完整评估所有分支 。
    

### 多智能体效用 (Multi-Agent Utilities) *

这种评估方法是将传统的Minimax推广到了有两个以上玩家的博弈场景中 。

- 树的叶子节点和非叶子节点的值都使用**效用元组 (Utility tuples)**来表示 。
    
- 在决策过程中，每个玩家只负责最大化元组中**属于自己的效用分量 (Maximizes its own component)** 。
    
- 这种多维度的效用评估会在动态博弈中自然产生**合作与竞争 (Cooperation and competition)**的行为模式 。
    

### 效用函数与世界模型 (Utilities and World Models)

- **效用 (Utilities)**是将世界状态映射为实数的函数，用于描述智能体的**偏好 (Preferences)**或目标 。
    
- **最大期望效用原则 (Principle of maximum expected utility)**表明，一个理性的智能体应该根据其已知信息选择能使其期望效用最大化的行动 。
    
- Minimax代表一种**危险的悲观主义 (Dangerous Pessimism)**，它总是假设最坏情况，这种方法对数值的**单调变换不敏感 (Insensitive to monotonic transformations)**，即相对大小比具体数值更重要 。
    
- Expectimax代表需要避免的**危险的乐观主义 (Dangerous Optimism)**，因为在实际具有对抗性的世界中假设随机性可能导致不利结果，并且它的计算依赖于具体的数值**幅度 (Magnitudes)**，数值的具体大小对最终决策有决定性影响 。
    

---

你需要我为你详细推导一下课件中第12题或第14题里特定博弈树的期望效用计算步骤吗？