## Flex 开启（伸缩盒模型，子元素）

  想要开启Flex布局只需要在其父元素身上开启：display：flex；这样父元素就会变成伸缩容器，而子元素变成了其中的伸缩项目，这时候子元素会按照主轴的方向在容器的内容区中一一展开一一展开；


## 主轴 测轴

主轴默认方向：从左到右
侧轴默认方向：从上到下
（注意 无指定原点）

### 调整主轴方向

```
flex:direction
	row:主轴默认方向
	row-reverse：相反方向
	column：侧轴默认方向
	column:相反方向
	侧轴跟着主轴一起旋转
```

### 换行方式

默认的时候，主轴上的元素展开是不会换行的，他会缩小伸缩项目的大小来实现添加

换行：
```
flex-wrap:
1
nowrap:默认 不换行
wrap：换行，当伸缩容器的内容区撑满的时候自动换行
wrap-reverse：从测轴方向的相反反向进行开始
```

### 主轴对其方式

```
justify-content:
flex-start:主轴起点开始对其  默认方式
flex-end：主轴终点开始对其
center：居中对其
space-between：均匀分布 两端对其
space-around ： 
space-evenly
```
![[Pasted image 20251007154528.png]]

### 侧轴对齐方式：

#### 当元素只暂居一行的时候：

```
align-item:
flex-start
flex-end
center
baseline：与伸缩项目的第一行文字的基线对齐
stretch：如果伸缩项目未设置高度，将占据整个容器的高度（默认）
```
![[Pasted image 20251007155113.png]]


#### 当有多行元素的时候

```
align-content:
flex-start
flex-end
center
space-between
space-around
space-evenly
stretch:占满整个侧轴--默认
```

![[Pasted image 20251007155312.png]]
![[Pasted image 20251007155332.png]]
![[Pasted image 20251007155342.png]]

### 利用justify-content来实现水平居中

1.父容器开始flex布局，随容用这来实现
```
.outer{
display:flex
justify-content:center;
align-items:center;

}
.inner{

}
```
2 父亲开始flex布局，随后子元素开始margin ：auto





### 问题：如何让一个父容器没有高度的元素居中呢

给父容器设置一个动态的高度，100vh-header高度，再居中就可以了，，用calc属性就行


## 排序

order：给伸缩项目的属性，值越小排在越前面
















