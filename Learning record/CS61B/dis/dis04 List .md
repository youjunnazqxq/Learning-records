```
public static void fillGrid(int[] LL, int[] UR, int[][] S) {
    int N = S.length;
    int kL, kR;
    kL = kR = 0;

    for (int i = 0; i < N; i += 1) {
        // 遍历 S 的每一列
        for (int j = 0; j < N; j += 1) {
            // 使用 i 和 j 的关系判断区域
            if (i > j) {
                // 如果是左下三角...
                S[i][j] = LL[kL]; // ...用 LL 的元素填充
                kL += 1;          // ...并更新 LL 的索引
            } else if (i < j) {
                // 如果是右上三角...
                S[i][j] = UR[kR]; // ...用 UR 的元素填充
                kR += 1;          // ...并更新 UR 的索引
            }
            // 如果 i == j (主对角线)，则不执行任何操作。
        }
    }
}
```