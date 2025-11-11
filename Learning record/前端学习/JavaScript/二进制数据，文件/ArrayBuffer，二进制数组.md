
**`ArrayBuffer` 是 JavaScript 中处理二进制数据（如文件、图片、网络数据包）的基础，它代表一块原始内存，必须配合视图（Views）来使用。**

```
let buffer = new ArrayBuffer(16);

```

它会分配一个 16 字节的连续内存空间，并用 0 进行预填充

**如要操作 `ArrayBuffer`，我们需要使用“视图”对象。**

视图对象本身并不存储任何东西。它是一副“眼镜”，透过它来解释存储在 `ArrayBuffer` 中的字节。


- **`Uint8Array`** —— 将 `ArrayBuffer` 中的每个字节视为 0 到 255 之间的单个数字（每个字节是 8 位，因此只能容纳那么多）。这称为 “8 位无符号整数”。
- **`Uint16Array`** —— 将每 2 个字节视为一个 0 到 65535 之间的整数。这称为 “16 位无符号整数”。
- **`Uint32Array`** —— 将每 4 个字节视为一个 0 到 4294967295 之间的整数。这称为 “32 位无符号整数”。
- **`Float64Array`** —— 将每 8 个字节视为一个 `5.0x10-324` 到 `1.8x10308` 之间的浮点数。

![[Pasted image 20251111191149.png]]

# TypedArray

所有这些视图（`Uint8Array`，`Uint32Array` 等）的通用术语是 [TypedArray](https://tc39.github.io/ecma262/#sec-typedarray-objects)。它们共享同一方法和属性集。

### `TypedArray` (类型化数组) 的 5 种创建方式总结

根据你提供的图片，创建 `TypedArray`（例如 `Uint8Array`、`Uint16Array` 等）有以下五种方式：

1. **从 `ArrayBuffer` 创建**
    
    - **语法**：`new TypedArray(buffer, [byteOffset], [length])`
        
    - **说明**：这是在现有的 `ArrayBuffer` (`buffer`) 上创建一个“视图”。你可以选择性地提供 `byteOffset`（字节偏移量，即视图的起始位置）和 `length`（视图包含的元素个数）。
        
    - **关键点**：这是唯一**不会**自动创建新 `ArrayBuffer` 的方式。
        
2. **从 `Array` (普通数组) 创建**
    
    - **语法**：`new TypedArray([0, 1, 2, 3])`
        
    - **说明**：会创建一个新的、长度相同的类型化数组，并**复制**普通数组中的内容。
        
    - **关键点**：会自动创建一个新的 `ArrayBuffer`。
        
3. **从另一个 `TypedArray` 创建**
    
    - **语法**：`new TypedArray(anotherTypedArray)`
        
    - **说明**：会创建一个新的、长度相同的类型化数组，并**复制**其内容。
        
    - **关键点**：会自动创建一个新的 `ArrayBuffer`。
        
    - **注意**：如果两个 `TypedArray` 的类型不同（例如从 `Uint16Array` 复制到 `Uint8Array`），数据在复制过程中会被转换，可能会丢失精度或被截断（如图中 `1000` 变为 `232`）。
        
4. **从 `length` (长度) 创建**
    
    - **语法**：`new TypedArray(4)`
        
    - **说明**：创建一个包含指定**元素个数**（这里是 4）的类型化数组。数组内容会被初始化（通常为 0）。
        
    - **关键点**：会自动创建一个新的 `ArrayBuffer`，其字节大小为 `length * TypedArray.BYTES_PER_ELEMENT`（例如 `new Uint16Array(4)` 会创建 4 * 2 = 8 字节的 buffer）。
        
5. **无参数创建**
    
    - **语法**：`new TypedArray()`
        
    - **说明**：创建一个长度为 0 的类型化数组。
        
    - **关键点**：会自动创建一个长度为 0 的新 `ArrayBuffer`。

#### 越界行为 

# TypedArray方法 

`TypedArray` 具有常规的 `Array` 方法，但有个明显的例外。

我们可以遍历（iterate），`map`，`slice`，`find` 和 `reduce` 等。

但有几件事我们做不了：
- 没有 `splice` —— 我们无法“删除”一个值，因为类型化数组是缓冲区（buffer）上的视图，并且缓冲区（buffer）是固定的、连续的内存区域。我们所能做的就是分配一个零值。
- 无 `concat` 方法



# DataView

[DataView](https://developer.mozilla.org/zh/docs/Web/JavaScript/Reference/Global_Objects/DataView) 是在 `ArrayBuffer` 上的一种特殊的超灵活“未类型化”视图。它允许以任何格式访问任何偏移量（offset）的数据。

- 对于类型化的数组，构造器决定了其格式。整个数组应该是统一的。第 i 个数字是 `arr[i]`。
- 通过 `DataView`，我们可以使用 `.getUint8(i)` 或 `.getUint16(i)` 之类的方法访问数据。我们在调用方法时选择格式，而不是在构造的时候。

`new DataView（buffer,[byteoffset],[byteLength]）`
- **`buffer`** —— 底层的 `ArrayBuffer`。与类型化数组不同，`DataView` 不会自行创建缓冲区（buffer）。我们需要事先准备好。
- **`byteOffset`** —— 视图的起始字节位置（默认为 0）。
- **`byteLength`** —— 视图的字节长度（默认至 `buffer` 的末尾）。
