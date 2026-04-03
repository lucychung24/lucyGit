#数据聚合：1）groupby工具
import pandas as pd
import numpy as np

#pandas数据数据聚合：
#---- 【start】6.3-数据聚合 ----#
#---- 【start】6.3.1-数据聚合-groupby工具 ----#

frame=pd.DataFrame(
{
'color':['white','red','green','red','green'],
'object':['pen','pencil','pencil','ashtray','pen'],
'price1':[5.56,4.2,1.3,0.56,2.75],
'price2':[4.75,4.12,1.6,0.75,3.15]
}
)

print("6.3.1-数据聚合-GroupBy工具:\n"
      "对于数据分类，pandas提供了非常灵活和高效的GroupBy工具。\n"
      "GroupBy指的是它内部机制SPLIE-APPLY-COMBINE(分组-用函数处理-合并结果)过程。它的操作模式由这3个阶段组成。\n"
      "")
# print('举例1）：')
frame=pd.DataFrame(
{
'color':['white','red','green','red','green'],
'object':['pen','pencil','pencil','ashtray','pen'],
'price1':[5.56,4.2,1.3,0.56,2.75],
'price2':[4.75,4.12,1.6,0.75,3.15]
}
)
group = frame.groupby('color')
group.groups
group.mean('price1')


group = frame['price1'].groupby(frame['color'])
group.groups
group.mean()
#可以把所有分组依据和计算方法指定好，写为
frame['price1'].groupby(frame['color']).mean()


print('举例1）GroupBy ：分组依据和计算  ')
print(f"frame 的数据：{frame}")
print(f"A)groupby分组操作,如group = frame['price1'].groupby(frame['color'])，这只分组，没进行任何计算，\n"
      f"    执行后：\n{ frame['price1'].groupby(frame['color'])} \n")
print(f"B)调用GroupBy对象的groups属性，查看分组情况：\n"
      f"   如 group.groups,执行后：\n{group.groups} \n")
print(f"C)对组进行计算，如求平均group.mean(),\n"
      f"   执行后： frame 的数据：\n"
      f"{group.mean()}\n"
      f"D) 也可以把所有分组依据和计算方法指定好，如把A)分组和C)计算，写为：frame['price1'].groupby(frame['color']).mean(),"
      f"  执行后：{frame['price1'].groupby(frame['color']).mean()}\n"
)


#等级分组
ggroup2=frame['price1'].groupby([ frame['color'],frame['object'] ] )
ggroup2.groups
ggroup2.sum()

#查看返回结果的数据结构，type()
# >>> type(ggroup2)
# <class 'pandas.core.groupby.generic.SeriesGroupBy'>


print(f"E）等级分组：使用多列进行分组，如ggroup2=frame['price1'].groupby([ frame['color'],frame['object'] ] )\n"
      f"  执行后，查看其分组情况 ggroup2.groups\n：{ggroup2.groups} \n")

#组迭代
print("举例2）GroupBy对象支持迭代操作，\n"
      "如：组迭代,生成一系列由各组名称及其数据部分组成的元组 \n"
      "for name,group in frame.groupby('color'):\n "
      "    print(name) \n"
      "    print(group)\n"
      " 执行后:")
# for name,group in frame['price1'].groupby(frame['color']):
for name,group in frame.groupby('color'):
    print(name)
    print(group)
    # print(group.sum())

# 上面：组迭代 ，执行结果
# green
#    color  object  price1  price2
# 2  green  pencil    1.30    1.60
# 4  green     pen    2.75    3.15
# red
#   color   object  price1  price2
# 1   red   pencil    4.20    4.12
# 3   red  ashtray    0.56    0.75
# white
#    color object  price1  price2
# 0  white    pen    5.56    4.75

#---- 【end】6.3.1-数据聚合-groupby工具 ----#

#---- 【start】6.3.2-数据聚合-链式转换： ----#

print("6.3.2-数据聚合-链式转换：\n"
      "上面groupby的分组操作，最终结果是Series或DataFrame数据结构，这保留了索引系统和列名称。\n"
      "因此，在groupby过程的任何一个阶段都可选择一列数据。pandas库对在分组操作上的巨大灵活性。")
print("举例2）链式转换：在groupby过程的任何一个阶段都可选择一列数据，pandas库对在分组操作上的巨大灵活性。\n"
      "如下面操作，在groupby过程的任何一个阶段都可选择一列数据")
print(f"A)frame['price1'].groupby(frame['color']).mean(),执行后:\n{frame['price1'].groupby(frame['color']).mean()} \n")
print(f"B)frame.groupby(frame['color'])['price1'].mean(),执行后:\n{frame.groupby(frame['color'])['price1'].mean()} \n")
print(f"C) (frame.groupby(frame['color']).mean('price1'))['price1'],执行后:\n{(frame.groupby(frame['color']).mean('price1'))['price1']}\n")

print("举例3）执行聚集操作后，某些列原名称可能存在表意不明确的现象，可在列名前加上前缀,用add_prefix()。\n"
      f"  如：求平均值：\n"
      f"A) frame.groupby('color').mean(['price1''price2']) ：\n{frame.groupby('color').mean(['price1','price2'])}\n"
      f"B) 执行聚集操作后列名前加上前缀,用add_prefix()：\n"
      f"     frame.groupby('color').mean(['price1','price2']).add_prefix('mean'):\n{frame.groupby('color').mean(['price1','price2']).add_prefix('mean')}\n")
#求平均值： 
frame.groupby('color').mean(['price1','price2'])
#可在列名前加上前缀,用add_prefix()：执行聚集操作后，某些列原名称可能存在表意不明确的现象，可在列名前加上前缀,用add_prefix()
frame.groupby('color').mean(['price1','price2']).add_prefix('mean')

# frame.groupby(frame['color']).mean([frame['price1'], frame['price2']]) #可执行
# frame.groupby('color').mean(['price1''price2']) #可执行

#A
frame['price1'].groupby(frame['color']).mean()
# B
frame.groupby(frame['color'])['price1'].mean()
# C
(frame.groupby(frame['color']).mean('price1'))['price1']


# frame.groupby('color')['price1'].mean()
# frame['price1'].groupby(frame['color']).mean()

result1=frame['price1'].groupby(frame['color']).mean()
#查看返回结果的数据结构，type()
type(result1)

# result2=frame.groupby(frame['color']).mean()
result2=frame.groupby('color').mean('price1')
#查看返回结果的数据结构，type()
type(result2)

# >>> result1=frame['price1'].groupby(frame['color']).mean()
# >>> result1
# color
# green    2.025
# red      2.380
# white    5.560
# Name: price1, dtype: float64
# >>> type(result1)
# <class 'pandas.core.series.Series'>

# >>> result2=frame.groupby('color').mean('price1')
# >>> result2
#        price1  price2
# color
# green   2.025   2.375
# red     2.380   2.435
# white   5.560   4.750
# >>> type(result2)
# <class 'pandas.core.frame.DataFrame'>

#---- 【start】6.3.2-数据聚合-链式转换： ----#




#---- 【start】6.3.3-数据聚合-分组函数： ----#

print('6.3.3-数据聚合-分组函数:\n'
      '很多函数不是专门为GroupBy对象实现的，它们却适用于Series数据结构。'
      '从GroupBy对象得到Series对象，即指定列名称，然后用函数执行计算就可以。')
print('6.3.3-数据聚合-分组函数:1）适用于Series数据结构的计算函数，可以调用；2）自定义聚合函数，作为参数传给agg()函数 \n')
print("举例3）用quantile()函数计算分位数")
group=frame.groupby('color')
#type()查看GroupBy操作返回的对象类型
type(group)
type(group['price1'])
# >>> group['price1']
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x00000215BCEE4A40>
# >>> type(group['price1'])
# <class 'pandas.core.groupby.generic.SeriesGroupBy'>
#用quantile()函数计算分位数
group['price1'].quantile(0.6)

print(f"如: group=frame.groupby('color'): {group}")
print(f" A)type()查看GroupBy操作返回的对象类型:\n"
      f"   如 type(group)对象类型: {type(group)}\n"
      f"    type(group['price1'])对象类型: {type(group['price1'])}\n")
print(f" B)用quantile()函数计算分位数:group['price1'].quantile(0.6): {group['price1'].quantile(0.6)}")

#‌计算分位数‌就是在一组数据中，找到某个特定位置的值，这个值能帮你把数据分成几部分。比如中位数（50%分位数）就是正中间的数，把数据分成两半
#分位数‌：比如四分位数（25%、50%、75%）把数据分成四段，帮你快速了解数据的分布情况
# ‌数据分析‌：用quantile()函数可以快速计算分位数，比如df.quantile(0.25)就是25%分位数。
# ‌异常值检测‌：如果数据中某个值远高于或低于分位数，可能是个异常点。

#自定义聚合函数，将其他作为参数传给agg()函数
def range(series):
    return series.max() - series.min()

group['price1'].agg(range) #自定义聚合函数range，将其他作为参数传给agg()函数
# group[['price1','price2']].agg(range)  #自定义聚合函数range，将其他作为参数传给agg()函数

print("举例4）自定义聚合函数，将其他作为参数传给agg()函数。\n"
      "如:"
      "1) 自定义聚合函数range: \n"
      "def range(series): \n"
      "    return series.max() - series.min() \n"
      "2) 将自定义聚合函数range，作为参数传给agg()函数:"
      f"    group['price1'].agg(range)"
      f"    执行后 :\n{group['price1'].agg(range) }\n"
      f"      (*上面结果：返回各颜色分组中price1的最大值- price2的最小值 的差)，因group是按颜色分组，group['price1']取price1的;自定义聚合函数range是'最大值- 最小值' ")


#---- 【end】6.3.3-数据聚合-分组函数： ----#

#---- 【start】6.3.4-高级数据聚合-transform()和apply()函数 ----#
print("6.3.4-高级数据聚合-transform()和apply()函数,它们可用来执行多种甚至复杂的组操作 ")
frame1=pd.DataFrame(
{'color':['white','red','green','red','green'],
# 'object':['pen','pencil','pencil','ashtray','pen'],
'price1':[5.56,4.2,1.3,0.56,2.75],
'price2':[4.75,4.12,1.6,0.75,3.15]
}
)

#聚合操作（如求和）
sum1=frame1.groupby('color').sum().add_prefix('tot_')
#聚合操作（如求和）内容放到同一个DataFrame对象
pd.merge(frame1,sum1,left_on='color',right_on='color')
# pd.merge(frame1,sum,left_on='color',right_index=True) #right_index=True,  使用右侧索引（可选）
# pd.merge(frame1,sum,on='color')

#数据聚合transform()
sum2=frame1.groupby('color').transform('sum').add_prefix('tot_') #新的写法
# sum2=frame1.groupby('color').transform(np.sum).add_prefix('tot_')  #旧的写法。 这有警告 ，对于np.sum
# np.sum 这有警告，DataFrameGroupBy.sum，
# currently using DataFrameGroupBy.sum. In a future version of pandas, the provided callable will be used directly.
# To keep current behavior pass the string "sum" instead.

sum2=frame1.groupby('color').transform('sum').add_prefix('tot_')

print("1、高级数据聚合transform()-更适用聚合操作，但对参数有特定要求：作为参数的函数必须生成一个标量（聚合），因为只有这样才能进行广播。")
print("举例1）把下面的内容放到同一个DataFrame对象中：原DataFrame(含有数据的)和聚合操作（如求和）得到的计算结果")

print(f"DataFrame对象frame1 :\n {frame1}\n")
print(f"1.1）聚合操作（如求和）sum1=frame1.groupby('color').sum().add_prefix('tot_') :\n {sum1}\n")
print(f"1.2））聚合操作（如求和）内容放到同一个DataFrame对象: \n "
      f"   pd.merge(frame1,sum,left_on='color',right_on='color') ：\n"
      f"   执行后：\n{pd.merge(frame1,sum1,left_on='color',right_on='color')}\n")
print(f"2）高级数据聚合transform()，聚合操作（如求和）。\n "
      f"   用transform()：实现‘1.1）聚合操作（如求和）’可以写为如下的\n "
      f"     frame1.groupby('color').transform('sum').add_prefix('tot_')"
      f"     执行后：\n{sum2}")

print("2、高级数据聚合apply()-适用于执行更为一般的GroupBy操作。\n"
      "这个方法完全实现了SPLIT-APPLY-COMBINE机制。\n"
      "它把对象分为几部分后，再用函数处理每一部分，各步骤之间用链式方法连接在一起。")

frame3=pd.DataFrame(
{
'color':['white','black','white','white','black'],
'status':['up','up','down','down','down'],
'value1':[12.33,14.55,22.34,27.84,23.4],
'value2':[11.23,31.8,29.99,31.18,18.25]
}
)

#apply() :apply(lambda x:x.max()) 根据分组，在组内求最大值
#Lambda 函数是 Python 中的一种‌匿名函数‌，使用 lambda 关键字定义，‌无需显式命名‌，语法简洁高效
# rst3=frame3.groupby(['color','status'], group_keys=False).apply(lambda x:x.max()) #根据分组，在组内求最大值
rst3=frame3.groupby(['color','status'])[['value1','value2']].apply(lambda x:x.max()) #根据分组，在组内求最大值


print(f"举例2）高级数据聚合apply()")
print(f" frame3 :{frame3} \n")
print(f"2.1）apply()函数使用：如：根据分组，在组内求最大值\n"
      f"    rst3=frame3.groupby(['color','status'])[['value1','value2']].apply(lambda x:x.max()) :\n"
      f"    执行后：\n{rst3} \n"
      f"     （*分组中white down，这组有两记录的，上面结果如预期在组内求最大值）")


# pandas中groupby.apply()、groupby.transform()和groupby.agg()是用于分组数据处理的三大核心函数，它们在功能、返回结果和适用场景上存在显著差异。
#
# 使用建议:
# agg(): 适用于快速生成分组统计值（如均值、总和），性能最优。
# transform(): 适用于在原数据上添加分组统计值（如均值填充缺失值），保持数据结构一致性。
# apply()：适用于复杂计算或自定义逻辑（如分组排序），灵活性最高但性能最差。
#
# 注意:
# agg()和transform()通常与内置函数结合使用，性能最优；
# apply()支持任意函数，但返回结果类型不固定，需根据需求选择；
# transform()返回结果与原数据同形，适合在原数据上添加统计值。

# >>> import pandas as pd
# >>> data = {    'A': [1, 1, 2, 2],    'B': [10, 20, 30, 40],    'C': [100, 200, 300, 400]}
# >>> df = pd.DataFrame(data)
# >>> df
#    A   B    C
# 0  1  10  100
# 1  1  20  200
# 2  2  30  300
# 3  2  40  400
# >>> # 1. agg()：分组求和
# >>> agg_result = df.groupby('A').agg({'B': 'sum', 'C': 'mean'})
# >>> agg_result
#     B      C
# A
# 1  30  150.0
# 2  70  350.0
# 返回结果个人理解lucy个人理解:
# 1列：按A列的值生成的分组
# 2列：A分组内B列值的和。（根据A的分组，在各分组内对B列的值求和）
# 3列：A分组内C列值的平均值（根据A的分组，在各分组内对C列的值求平均值 


# >>> # 2. transform()：分组均值填充
# >>> transform_result = df.groupby('A')['B'].transform('mean')
# >>> transform_result
# 0    15.0
# 1    15.0
# 2    35.0
# 3    35.0
# Name: B, dtype: float64
# 返回结果个人理解lucy个人理解:
# 1列：索引
# 2列：分组均值：根据A列的值分组，在分组内求B列的平均值。同一分组值相同, 如索引0和1的A列值都是1，是同一个分组，这两行显示的同一个均值
# 返回结果，与原数据同形的DataFrame，因此1列的索引，

# >>> # 3. apply()：分组排序
# >>> apply_result = df.groupby('A').apply(lambda x: x.sort_values('B'))
# >>>  apply_result
#   File "<stdin>", line 1
#     apply_result
# IndentationError: unexpected indent
# >>> apply_result
#      A   B    C
# A
# 1 0  1  10  100
#   1  1  20  200
# 2 2  2  30  300
#   3  2  40  400
#（lucy:组内按“4列：B列”的值，升序，排序显示数据）

# #排序：ascending=False，按B降序
# >>> df.groupby('A').apply(lambda x: x.sort_values('B',ascending=False))  #ascending=False
#      A   B    C
# A
# 1 1  1  20  200
#   0  1  10  100
# 2 3  2  40  400
#   2  2  30  300
# （lucy:组内按“4列：B列”的值，降序，排序显示数据）
# 返回结果个人理解lucy个人理解:
# 1列：A分组
# 2列：索引
# 3列：A列
# 4列：B列
# 5列：C列
# *数据显示，按A列的值分组，组内数据按B列的值进行排序显示，即组内按“4列：B列”的值的排序显示数据，如


#---- 【end】6.3.4-高级数据聚合-transform()和apply()函数 ----#

#数据聚合：1）groupby工具