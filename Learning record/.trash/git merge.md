
第 1 步：切换到主分支 main

这是你的目标分支，也就是要接收新代码的分支。

Bash

```
git checkout main
```

第 2 步：更新主分支 main

这是最关键的一步！在合并前，必须确保你的 main 分支包含了远程仓库的最新代码，以避免冲突。

Bash

```
git pull origin main
```

第 3 步：执行合并

现在你的 main 分支是最新的了，可以把你的功能分支合并进来了。

Bash

```
git merge feature-login
```

第 4 步：解决冲突（如果发生）

如果 Git 提示有冲突（Conflict），你需要：

1. 手动打开冲突文件，编辑并决定保留哪些代码。
    
2. 保存文件后，用 `git add <文件名>` 标记为已解决。
    
3. 最后用 `git commit` 完成这次合并。
    

如果一切顺利没有冲突，Git 会自动完成合并，你可以跳过这一步。

第 5 步：推送合并结果

你的本地 main 分支现在已经包含了新功能，需要把它推送到远程仓库，让团队其他成员也能看到。

Bash

```
git push origin main
```

第 6 步：清理分支（可选，但推荐）

合并成功后，通常会删除已经完成使命的功能分支，保持仓库整洁。

Bash

```
# 删除本地分支
git branch -d feature-login

# 删除远程分支
git push origin --delete feature-login
```

**总结成一句话就是**：**先切换到主干，拉取最新代码，再合并你的分支，最后推送。**