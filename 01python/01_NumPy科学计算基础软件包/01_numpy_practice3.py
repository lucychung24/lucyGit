#NumPy是练习，学习常用操作 - 常用概念:向量化和广播机制

import numpy as np

print(f"2.3-3常用概念:向量化。 向量化和广播这两个概念是NumPy内部实现的基础。有了向量化，编写代码时无需使用显式循环。这些循环实际上不能省略，只不过是在内部实现，被代码中的其他结构代替。"
      f"Numpy向量化在数组运算、条件筛选、统计计算和矩阵运算中的应用，通过广播机制自动扩展操作，避免显式循环，显著提升性能和代码简洁性。")
print("向量化使得很多运算看去更像数学表达式，例如，NumPy中两个数组或矩阵相乘可表示为 a * b , 其他语言这运算要用多重for结构去计算相乘（for (i=0;i<rows;i++) {c[i]=a[i]*b[i];}）")

a = np.array([[1, 2, 3], [4, 5, 6]])  # 形状 (2, 3)
b = np.array([1, 0, -1])              # 形状 (3,)
result = a + b  # 广播后结果形状 (2, 3)
print(f"\n2.3-4常用概念:广播机制。NumPy广播机制是NumPy中处理不同形状数组间算术运算的核心特性，其核心功能是自动扩展较小数组的维度，使其与较大数组匹配，从而实现逐元素操作")
print(f"\n  举例： a = np.array([[1, 2, 3], [4, 5, 6]])  # 形状 (2, 3);b = np.array([1, 0, -1])  # 形状 (3,)"
      f"\n     result = a + b  # 广播后结果形状 (2, 3)"
      f"\n     a的值：\n {a}"
      f"\n     b的值：\n {b}"
      f"\n     result = a + b  # 广播后结果形状 (2, 3), result的值：\n {result}")

#
# 创建结构化数组
print(f"\n2.4-结构化数组:结构化数组，它包含的是结构或记录而不是独立的元素， 可用dtype选项指明组成结构体的元素及它们的数据类型和顺序")
dtype = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
data = [('Alice', 30, 60.5), ('Bob', 25, 70.2), ('Charlie', 35, 68.0)]
structured_array = np.array(data, dtype=dtype)
structured_array
print("原始数组：", structured_array)

# 字段访问
names = structured_array['name']
ages = structured_array['age']
weights = structured_array['weight']

# 字段修改
structured_array['age'] += 1  # 年龄加1
structured_array[0]['weight'] = 61.0  # 修改第一个元素的体重

# 按字段排序
sorted_by_age = np.sort(structured_array, order='age')

# 字段统计
average_age = np.mean(structured_array['age'])
max_weight = np.max(structured_array['weight'])

# 输出结果
print(f"原始数组，年龄加1,structured_array['age'] += 1 ,修改第一个元素的体重structured_array[0]['weight'] = 61.0  后 ：\n {structured_array}")
print("按年龄排序：", sorted_by_age)
print("平均年龄：", average_age)
print("最大体重：", max_weight)

'''
3.6.1.  广播机制
NumPy广播机制是NumPy中处理不同形状数组间算术运算的核心特性，其核心功能是自动扩展较小数组的维度，使其与较大数组匹配，从而实现逐元素操作‌

广播机制的核心规则：
1、维度对齐‌：从末尾维度开始比较，若维度长度相等或其中一个为1，则可广播‌
2、虚拟扩展‌：较小数组在内存中不实际复制数据，通过内存访问策略（striding）实现虚拟扩展‌
3、兼容性条件‌：
   若两个数组形状完全相同，直接逐元素运算。
   若数组维数不同，较小数组在前面补1维（如(4, 1)与(3,)可广播）。数组的各维度相容，也就是两个数组的每一维度等长，或其中一个数组为一维，那么广播机制就适用。‌
   若某维度长度不为1且不匹配，抛出广播错误‌

广播机制的优势：
简化代码‌：无需手动扩展数组或循环，一行代码实现复杂运算‌
高效计算‌：避免内存复制，通过内存访问优化提升计算速度‌
应用场景‌：广泛应用于数组加减、标量运算等，尤其在数据科学和机器学习中‌

'''
