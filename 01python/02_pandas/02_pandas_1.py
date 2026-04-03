#pandas库 - Pandas 是 Python 中用于数据分析和数据操作的核心库;pandas的核心为两大数据结构, Series和DataFrame
'''
1、数据结构‌
Series‌：一维带索引的数组，支持多种数据类型（如整数、浮点数、字符串）。
DataFrame‌：二维表格结构，类似 Excel 表格，支持列名和行索引，每列可独立数据类型‌
'''

import pandas as pd
import numpy as np
#---- 【start】 ----#
#---- 【end】 ----#

#---- 【start】 ----#
#---- 【end】 ----#





#---- 【start】Pandas库Series ----#
'''
s=pd.Series([12,-4,7,9])
print("Pandas是Python 中用于数据分析和数据操作的核心库;pandas的核心为两大数据结构, Series和DataFrame。\n"
      "pandas数据结构，index对像声明后不能改变，跟其他元素不同。不同数据结构公用index对象时，改特性能够保证它的安全。"
      "在数据分析方面的大多数优秀特性都取决于完全整合到这些数据结构中的Index对象")
print("1-Series:Pandas库用Series对象用来表示一位数据结构；"
      "它的内部结构是由两个相互关联的数组组成，主数组存放数据，Index数组存放标签；主数组的每一个元素都有一个与之相关的标签。"
      f"\n  "
      f"")
print("1.1-声明series对象：调用Series()构造函数，把药存放在Series对象中的数据以数组形式传入。 "
      f"\n  如：s=pd.Series([12,-4,7,9]) , 生成series对象s的值：\n{s} \n"
      f"   (*从Series的输出看到，左侧Index是一列标签，右侧是标签对应的元素。 声明Seriess时，若不指定标签，pandas默认使用从0开始依次递增的数值作为标签。)\n")

s=pd.Series([12,-4,7,9],index=['a','b','c','d'])
print(f"  指定标签:调用构造函数时，指定index选项，把存放有标签的数组赋给它。 最好使用有意义的标签，用于区分和识别每个元素。\n "
      f"     如：s=pd.Series([12,-4,7,9],index=['a','b','c','d']), 生成series对象s的值：\n{s} \n")

print(f"1.2-选取内部元素：指定键 如 用s[2] 或 s.iloc[2] ,其返回结果/值： {s.iloc[2]}\n "
      f"       (*注意：按位置访问的这写法s[2]，这种方式已被弃用，能有值但会有警告。解决方案‌：明确使用 .iloc[] 按位置访问，或 .loc[] 按标签访问。如修改为 s.iloc[2] \n "
      f"1.2-选取内部元素：指位于索引位置的标签 如s['b'],其返回结果/值：{s['b']} \n"
      f"1.2-选取内部元素： 如 s[0:2]  其返回结果/值：\n {s[0:2]}\n"
      f"1.2-选取内部元素： 如 s[['b','c']] 其返回结果/值：\n {s[['b','c']]}\n")

print(f"1.3-为元素赋值： 如 s.iloc[1] = 0 操作后，s的值：\n {s} \n")

arr=np.array([1,2,3,4])
s3=pd.Series(arr)
s4=pd.Series(s)
print(f"1.3-用Numpy数组或其他Series对象定义新的Series对象： "
      f"如:用Numpy数组 arr=np.arange([1,2,3,4]), s3=pd.Series(arr)  操作后，s3的值：\n {s3} \n"
      f"如:其他Series对象 s4=pd.Series(s)  操作后，s4的值：\n {s4} \n"
      f"    (*注意：新Series对象中的元素，不是原Numpy数组或Series对象元素的副本，而是对它们的应用，即 改变原有对象元素的值（Numpy数组或Series对象的值），新Series对象的值也会变)")

print("1.4-Series筛选元素： \n")


'''

print("1.4-Series筛选元素： \n")
#---- 【end】Pandas库Series ----#

print("2-DataFrame对象： \n")
print("2-DataFrame对象： \n")
print("2-DataFrame对象： \n")

#---- 【start】Pandas库更换索引index()函数 ----#
'''
ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
ser.index
# print(ser.index) # print(ser)
print("2.3-index对像 \n")
print("pandas数据结构，index对像声明后不能改变，跟其他元素不同。不同数据结构公用index对象时，改特性能够保证它的安全。"
"在数据分析方面的大多数优秀特性都取决于完全整合到这些数据结构中的Index对象。\n")
print("2.3.1-index对像声明：指定构造函数的index选项，把存储多个标签的数组转化为index对象。\n"
      "  举例： ser=pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green']) \n"
      f"    *ser的值 (ser）：\n {ser}\n "
      f"    *ser的index对象值（ser.index）：\n {ser.index}\n ")

#ser.idxmax()
print("2.3.2-index对像的方法：\n"
      f"  1）idxmin()和idxmax()函数分别返回索引值最小和最大的元素： 如 ser.idxmin()值 :{ser.idxmin()} ; ser.idxmax() 值:{ser.idxmax()}  \n")
'''
#---- 【end】Pandas库更换索引index()函数 ----#

#---- 【start】Pandas库更换索引reindex()函数 ----#
'''
serd=pd.Series(np.arange(6),index=['white','white','blue','green','green','yellow'])
serd.is_unique  #Series.is_unique ：‌定义‌：检查 Series 中的值是否唯一（无重复）。‌返回值‌：布尔值（True 表示唯一，False 表示有重复）
serd.index.is_unique #Index.is_unique： 定义‌：检查 Index（索引）中的值是否唯一。‌返回值‌：布尔值（True 表示唯一，False 表示有重复）
print(f"  2）含有重复标签的index：index对像有is_unique属性，调用它查看是否存在重复的索引项。"
      f"     举例：创建有重复标签/索引项的：serd=pd.Series(np.arange(6),index=['white','white','blue','green','green','yellow'])\n"
      f"        *有重复重复标签/索引项的，serd的值：\n {serd} \n"
      f"        *index对象的is_unique属性：调用 serd.index.is_unique 操作后返回值：\n  {serd.index.is_unique}")


print("2.3-index对像 \n")
print("2.4-reindex()函数更换索引：index对象不能改变，但可以执行更换索引操作（reindex()函数）解决这问题。Pandas的reindex()函数更换索引，根据新标签序列，重新调整原Series/DataFrame的元素，生成一个新的对象。更换index对象时，可以调整索引列中个标签的顺序、删除或增加新标签。 "
      "")
# 创建示例DataFrame
data = {
    'A': pd.date_range(start='2016-01-01', periods=20, freq='D'),
    'x': np.linspace(0, 19, 20),
    'y': np.random.rand(20),
    'C': np.random.choice(['Low', 'Medium', 'High'], 20).tolist(),
    'D': np.random.normal(100, 10, size=20).tolist()
}
df = pd.DataFrame(data)

print("原始的 df :\n",df)

# 重建索引示例
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print("\n 重建索引结果 (如：df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])):\n", df_reindexed)

#修改df 第1行，“A"列的日期值为'2016-09-01', 替换原来的'2016-09-01'
#df["A"][0]='2016-09-01'   # df["col"][row_indexer] = value ; Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.
df.loc[0,'A']='2016-09-01'
print(f"\n修改df 第1行，'A'列的日期值为'2016-09-01', 替换原来的'2016-09-01'。 如 执行df.loc[0,'A']='2016-09-01' 操作后，"
      " df的df.loc[0,'A'] 值，如预期有修改:\n {df.loc[0,'A']}")

print(f"重建索引结果2-df_reindexed 中的值如预期没变，因为reindex()函数是生成一个新的对象，是副本），df_reindexed的值:\n {df_reindexed}")

# 使用fill_value填充缺失值
df_filled = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'], fill_value=0)
print("\n填充缺失值结果 (如df_filled = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'], fill_value=0)):\n", df_filled)

# 重建索引并修改列顺序
df_reordered = df.reindex(columns=['D', 'C', 'A'])
print("\n修改列顺序结果 (如df_reordered = df.reindex(columns=['D', 'C', 'A']):\n", df_reordered)


import pandas as pd

# Series 示例
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s_reindexed = s.reindex(['c', 'b', 'a', 'd'], method='ffill', fill_value=0)  # 结果：c 3.0, b 2.0, a 1.0, d 0.0
print(f"更换索引: Series 示例: "
      f"  s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])"
      f"  s_reindexed = s.reindex(['c', 'b', 'a', 'd'], method='ffill', fill_value=0)  # 结果：c 3.0, b 2.0, a 1.0, d 0.0"
      f"  更换索引后:s_reindexed 值:\n {s_reindexed}\n")

# DataFrame 示例
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['x', 'y'])
df_reindexed = df.reindex(index=['y', 'x', 'z'], columns=['B', 'A'], fill_value=-1)  # 结果：y  4 2, x 3 1,  z -1 -1
print(f"更换索引: DataFrame 示例: "
      "  df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['x', 'y'])"
      "  df_reindexed = df.reindex(index=['y', 'x', 'z'], columns=['B', 'A'], fill_value=-1)  # 结果：y  4 2, x 3 1,  z -1 -1"
      f"  更换索引后:df_reindexed 值:\n {df_reindexed}\n")
'''
#---- 【end】Pandas库更换索引reindex()函数 ----#


#---- 【start】Pandas库算术和对齐 ----#
#Series对象
s1=pd.Series([3,2,5,1],['white','yellow','blue','green'])
s2=pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])
rst=s1+s2
# print(f"s1:\n {s1}")  print(f"s2:\n {s2}") rst=s1+s2   print(f"rst=s1+s2: \n{rst}")
print("3.1-Pandas库算术和对齐:pandas能够将两个数据结构的索引对齐。\n"
      f"1)举例Series对象：算术和对齐 \n"
      f"  s1=pd.Series([3,2,5,1],['white','yellow','blue','green']) \n "
      f"  s2=pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown']) \n"
      f"  s1的元素:\n {s1} \n"
      f"  s2的元素:\n {s1} \n"
      f"  算术和对齐,rst=s1+s2 执行后，rst的值：\n {rst}\n"
      f"     *有些标签，两个对象都有，有些只属于其中一个对象。两个都有，就把它们的元素相加；只属于其中一个的，标签也会显示在结果中，不过元素为NaN \n"
      )

#DataFrame对象
frame1=pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])
frame2=pd.DataFrame(np.arange(12).reshape((4,3)),index=['blue','green','white','yellow'],columns=['nug','pen','ball'])
df_rst=frame1+frame2
print("2)举例DataFrame对象：算术和对齐 \n\n"
      f"  frame1=pd.DataFrame(np.arange(16).reshape((4,4)),index=['red','blue','yellow','white'],columns=['ball','pen','pencil','paper'])\n"
      f"  frame2=pd.DataFrame(np.arange(12).reshape((4,3)),index=['blue','green','white','yellow'],columns=['nug','pen','ball'])\n"
      f"  frame1的元素:\n {frame1} \n"
      f"  frame2的元素:\n {frame2} \n"
      f"  算术和对齐,df_rst=frame1+frame2 执行后，df_rst的值：:\n {df_rst} \n"
      f"  *DataFrame对象之间运算，对齐规则相同，不过行和列都要执行对齐操作。有些标签，两个对象都有，有些只属于其中一个对象。两个都有，就把它们的元素相加；只属于其中一个的，标签也会显示在结果中，不过元素为NaN\n")
#---- 【end】Pandas库算术和对齐 ----#


#---- 【start】 ----#
#---- 【end】 ----#




#print(f"df_reindexed:\n {df_reindexed}")


#print(f"  如：s=pd.Series([12,-4,7,9]) , 生成series对象s的值：\n{s} \n")

#print(pd.__version__)


'''
4.1.	pandas和numpy有什么区别
Pandas 和 NumPy 是 Python 数据科学的核心库，它们在数据结构、功能用途和应用场景上有显著区别：

1. ‌数据结构与类型支持‌
NumPy
核心数据结构‌：ndarray（多维数组）。
类型要求‌：所有元素必须为同种数据类型（如 int32、float64），不支持异构数据。
索引方式‌：仅支持整数索引（如 arr[0]），不支持标签索引。
Pandas
核心数据结构‌：Series（一维带标签数组）和 DataFrame（二维表格）。
类型灵活性‌：DataFrame 每列可独立数据类型（如整数、浮点数、字符串），支持异构数据。
索引方式‌：支持整数索引（如 df[0]）和标签索引（如 df['列名']）。

2. ‌功能与用途‌
NumPy
核心功能‌：数值计算、矩阵运算、统计分析。
应用场景‌：科学计算、工程计算、机器学习（如特征矩阵运算）。

Pandas
核心功能‌：数据处理、清洗、聚合、时间序列分析。
应用场景‌：数据分析、数据预处理、金融分析（如按月聚合数据）。

3. ‌性能与内存使用‌
NumPy
内存高效‌：固定类型数组在内存中紧凑存储。
计算速度‌：矢量化操作（如 arr + 1）比循环快数十倍。

Pandas
内存开销‌：每列数据类型独立存储，内存使用可能更高。
计算效率‌：适合复杂操作（如分组统计），但单列计算时可能不如 NumPy 快。

4. ‌典型操作示例‌
操作
NumPy
Pandas
创建数组
np.array([1, 2, 3])	pd.Series([1, 2, 3])
数据类型
ndarray（单一类型）	DataFrame（多列异构类型）
索引方式
arr[0]	df['列名']
数学运算
arr + 1	df['列名'] + 1
数据读取
无内置读取功能	pd.read_csv('data.csv')
数据聚合
np.mean(arr)	df.groupby('列名').sum()

5. ‌使用场景建议‌
数值计算‌：优先使用 NumPy（如矩阵运算、科学计算）。
数据分析‌：优先使用 Pandas（如 CSV 读取、数据清洗、时间序列处理）。
协同使用‌：Pandas 的 DataFrame 内部使用 NumPy 数组，二者可无缝集成。

总结‌：
NumPy 专注于高效数值计算，Pandas 专注于灵活数据处理与分析。选择时需根据具体任务需求（如数据类型、计算复杂度）决定。

'''