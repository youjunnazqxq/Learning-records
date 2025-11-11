**基本的二进制对象是 `ArrayBuffer` —— 对固定长度的连续内存空间的引用**


```
let buffer = new ArrayBuffer(16);

```

它会分配一个 16 字节的连续内存空间，并用 0 进行预填充

`ArrayBuffer` 是一个内存区域。它里面存储了什么？无从判断。只是一个原始的字节序列。

**如要操作 `ArrayBuffer`，我们需要使用“视图”对象。**

视图对象本身并不存储任何东西。它是一副“眼镜”，透过它来解释存储在 `ArrayBuffer` 中的字节。


- **`Uint8Array`** —— 将 `ArrayBuffer` 中的每个字节视为 0 到 255 之间的单个数字（每个字节是 8 位，因此只能容纳那么多）。这称为 “8 位无符号整数”。
- **`Uint16Array`** —— 将每 2 个字节视为一个 0 到 65535 之间的整数。这称为 “16 位无符号整数”。
- **`Uint32Array`** —— 将每 4 个字节视为一个 0 到 4294967295 之间的整数。这称为 “32 位无符号整数”。
- **`Float64Array`** —— 将每 8 个字节视为一个 `5.0x10-324` 到 `1.8x10308` 之间的浮点数。


# TypedArray

所有这些视图（`Uint8Array`，`Uint32Array` 等）的通用术语是 [TypedArray](https://tc39.github.io/ecma262/#sec-typedarray-objects)。它们共享同一方法和属性集。

请注意，没有名为 `TypedArray` 的构造器，它只是表示 `ArrayBuffer` 上的视图之一的通用总称术语：`Int8Array`，`Uint8Array` 及其他，很快就会有完整列表。


1. 如果给定的是 `ArrayBuffer` 参数，则会在其上创建视图。我们已经用过该语法了。
    
    可选，我们可以给定起始位置 `byteOffset`（默认为 0）以及 `length`（默认至 buffer 的末尾），这样视图将仅涵盖 `buffer` 的一部分。
    
2. 如果给定的是 `Array`，或任何类数组对象，则会创建一个相同长度的类型化数组，并复制其内容。
    
    我们可以使用它来预填充数组的数据：


    如果给定的是另一个 `TypedArray`，也是如此：创建一个相同长度的类型化数组，并复制其内容。如果需要的话，数据在此过程中会被转换为新的类型

对于数字参数 `length` —— 创建类型化数组以包含这么多元素。它的字节长度将是 `length` 乘以单个 `TypedArray.BYTES_PER_ELEMENT` 中的字节数

#### 越界行为 

# TypedArray方法 

`TypedArray` 具有常规的 `Array` 方法，但有个明显的例外。

我们可以遍历（iterate），`map`，`slice`，`find` 和 `reduce` 等。

但有几件事我们做不了：
- 没有 `splice` —— 我们无法“删除”一个值，因为类型化数组是缓冲区（buffer）上的视图，并且缓冲区（buffer）是固定的、连续的内存区域。我们所能做的就是分配一个零值。
- 无 `concat` 方法


