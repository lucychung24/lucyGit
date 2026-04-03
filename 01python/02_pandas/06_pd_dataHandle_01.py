#pandas数据处理：包括1）加载；2）组装：合并（merging）、拼接(concatenation)、组合(combine)；3）变形(轴向旋转)、4）删除
import pandas as pd
import numpy as np

#---- 【start】6.1-数据准备-组装：合并（merging） ----#
print("6.1-数据准备-组装：合并（merging）、拼接(concatenation)、组合(combine)")
#---- 【start】6.1.1-数据准备-组装：合并（merging） ----#

print("6.1.1-数据准备-组装：合并（merging）-多表关联（基于列）,pd.merge() on选项指定基于哪列合并，若不指定用相同列字段:\n"
      "1）pd.merge() on选项指定基于哪列合并，若不指定用相同列字段。"
      "没有相同的列字段。left_on选项指定第一个dataFrame基于哪列合并;right_on第二个dataFrame的.\n"
      "2）merge()默认执行内连接操作。how选项指定连接类型，如：inner内连接;left左连接; right右链接;outer外连接\n"
      "3）可用根据索引合并，用索引作为键，把left_index和right_index选项的值置为True,将其激活，就可将其作为合并dataFrame的基准。\n"
    )
print("举例1.1：合并frame11、frame12，有相同的列字段id。on选项指定基于哪列合并，若不指定用相同列字段")
frame11=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                    'price':[12.33, 11.44, 33.21, 13.23, 33.62]})
frame12=pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                    'color':['white','red','red','black']})
merge_frame=pd.merge(frame11,frame12) #merge()合并操作
print(f"frame11:\n{frame11}")
print(f"frame12:\n{frame12}")
print(f"合并frame11、frame12：merge_frame=pd.merge(frame11,frame12), merge_frame:\n{merge_frame}\n")

print("举例1.2：合并frame1、frame2，有相同的列字段id。on选项指定基于哪列合并，若不指定用相同列字段")
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                     'color':['white','red','red','black','green'],
                     'brand':['OMG','ABC','ABC','POD','POD']})
frame2=pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                    'brand':['OMG','POD','ABC','POD']})
merge_frame1=pd.merge(frame1,frame2) #merge()合并操作,没on选项指定基于哪列合并，用相同的列字段id和brand进行合并
merge_frame2=pd.merge(frame1,frame2,on='id') #合并frame1、frame2（用列字段id）
merge_frame3=pd.merge(frame1,frame2,on='brand') #合并frame1、frame2（用列字段brand）
print(f"frame1:\n{frame1}")
print(f"frame2:\n{frame2}")
print(f"1）合并frame1、frame2（用相同的列字段id和brand进行合并）：merge_frame1=pd.merge(frame1,frame2), merge_frame1:\n{merge_frame1}\n"
      f"   * frame1和frame2合并没on选项指定基于哪列合并，用相同的列字段id和brand进行合并"
      f"，这两字段没有相同值，因此没取到数据得到一个空DataFrame对象")
print(f"2）合并frame1、frame2（用列字段id）：merge_frame2=pd.merge(frame1,frame2,on='id'), merge_frame2:\n{merge_frame2}\n")
print(f"3）合并frame1、frame2（用列字段brand进行合并）：merge_frame3=pd.merge(frame1,frame2,on='brand'), merge_frame3:\n{merge_frame3}\n")

print("举例1.3：合并frame1、frame3，没有相同的列字段。left_on选项指定第一个dataFrame基于哪列合并;right_on第二个dataFrame的")
frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                     'color':['white','red','red','black','green'],
                     'brand':['OMG','ABC','ABC','POD','POD']})
frame3=pd.DataFrame({'sid':['pencil','pencil','ball','pen'],
                    'brand':['OMG','POD','ABC','POD']})

merge_frame3=pd.merge(frame1,frame3,left_on='id',right_on='sid') #left_on选项指定第一个dataFrame基于哪列合并;right_on第二个dataFrame

print(f"frame1:\n{frame1}")
print(f"frame3:\n{frame3}")
print(f"合并frame1、frame2：merge_frame3=pd.merge(frame1,frame3,left_on='id',right_on='sid'):\n{merge_frame3}\n")

print("举例2.1：合并frame1、frame2, 根据on='id'合并：how选项指定连接类型，如：inner内连接;left左连接; right右链接;outer外连接")
print(f"frame1:\n{frame1}")
print(f"frame2:\n{frame2}")
iner_join_df=pd.merge(frame1,frame2,on='id',how='inner')
left_join_df=pd.merge(frame1,frame2,on='id',how='left')
right_join_df=pd.merge(frame1,frame2,on='id',how='right')
outer_join_df=pd.merge(frame1,frame2,on='id',how='outer')
print(f"how选项指定连接类型，如：how=inner内连接，iner_join_df=pd.merge(frame1,frame2,on='id',how='inner'):\n {iner_join_df}\n")
print(f"how选项指定连接类型，如：how=left左连接:\n {left_join_df}\n")
print(f"how选项指定连接类型，如：how=right右链接:\n {right_join_df}\n")

print("举例3.1：合并frame1、frame2,根据索引合并：1）【用merge()函数】用索引作为键，把left_index和right_index选项的值置为True,将其激活，就可将其作为合并dataFrame的基准")
#1)据索引合并，用merge()函数
index_join_df=pd.merge(frame1,frame2,left_index=True,right_index=True) #根据索引合并，用索引作为键，把left_index和right_index选项的值置为True
print(f"frame1:\n{frame1}")
print(f"frame2:\n{frame2}")
print("1)据索引合并，用merge()函数：合并frame1、frame2,根据索引合并，用索引作为键:index_join_df=pd.merge(frame1,frame2,left_index=True,right_index=True) "
      f"\n index_join_df :{index_join_df}")

print("举例3.1：合并frame1、frame2,根据索引合并：2）【用DataFrame对象的join()函数】用索引作为键")
#frame1的列名称跟frame2的列名称有重合： 处理方法1）同名：重命名frame2的列名称
frame2.columns=['brand2','id2'] #重命名frame2的列名称，因frame1的列名称跟frame2的列名称有重合
df_join=frame1.join(frame2) #用索引作为键

print("2)据索引合并，用DataFrame对象的join()函数：如frame2.columns=['brand2','id2']#重命名frame2的列名称，df_join=frame1.join(frame2) #用索引作为键： "
      f"\n {df_join}\n"
      f"\n  *frame1.join(frame2)，合并后得到的dataframe对象包含只存在于frame1中的索引2，但整合自frame2，索引号为4的各元素均为NaN"
      f"\n  *DataFrame对象的join()函数这更适合根据索引进行合并。\n"
      f"    注意：用join()函数合并，DataFrame对象的列名称不能有重合,否则会报错。若有重合，需重命名列名称\n")

#用列名，设置为索引，作为关联字段：如print("2)据索引合并，用DataFrame对象的join()函数：
join_df2=frame1.set_index('id').join(frame2.set_index('id2'))
print("2)据索引合并，用DataFrame对象的join()函数：用列名，设置为索引，作为关联字段, join_df2=frame1.set_index('id').join(frame2.set_index('id2')),"
      f"\n  join_df2 的值：\n{join_df2} \n")


#frame1的列名称跟frame2的列名称有重合： 处理方法2）设置关联字段为索引index
#If we want to join using the key columns, we need to set key to be
# the index in both `df` and `other`. The joined DataFrame will have
# key as its index
# join_df2=frame1.set_index('id').join(frame2.set_index('id2'))


#下面的用索引做关联字段，lsuffix左边frame1的字段加上后缀； rsuffix右边frame2的字段加上后缀
#frame1.join(frame2, lsuffix='_caller', rsuffix='_other')
# >>> frame1.join(frame2, lsuffix='_caller', rsuffix='_other')
#   id_caller  color brand_caller id_other brand_other
# 0      ball  white          OMG   pencil         OMG
# 1    pencil    red          ABC   pencil         POD
# 2       pen    red          ABC     ball         ABC
# 3       mug  black          POD      pen         POD
# 4   ashtray  green          POD      NaN         NaN



#---- 【end】6.1.1-数据准备-组装：合并（merging）----#


#---- 【start】6.1.2-数据准备-组装：拼接(concatenation)-堆叠数据（行/列） ----#

print("6.1.2-数据准备-组装：拼接(concatenation)-堆叠数据（行/列）")
print("拼接(concatenation):\n"
      "1）Numpy的concatenate()函数用于数组的拼接\n"
      "2）pandas的contact()函数实现按轴拼接的功能")

print("举例1）Numpy的concatenate()函数用于数组的拼接")
#举例1）Numpy的concatenate()函数用于数组的拼接
array1=([0,1,2],[3,4,5],[6,7,8])
array2=np.arange(9).reshape((3,3))+6
rst11=np.concatenate([array1,array2]) #axis不填，其默认值axis=0，按行拼接，行数变多；堆叠数据（行/列）
rst12=np.concatenate([array1,array2],axis=1)  #axis=1,按列拼接，列数变多；堆叠数据（行/列）
print("array1:\n",array1)
print("array2:\n",array2)
print("1）Numpy的concatenate()函数用于数组的拼接:rst11=np.concatenate([array1,array2]),rst11:\n",rst11)
print("2）Numpy的concatenate()函数用于数组的拼接，axis=1:rst12=np.concatenate([array1,array2],axis=1) ,rst12:\n",rst12)

print("\n举例2）pandas的contact()函数实现按轴拼接的功能")
#举例2）pandas的contact()函数实现按轴拼接的功能- Series对象
ser1=pd.Series(np.random.randn(4),index=["1","2","3","4"])
ser2=pd.Series(np.random.randn(4),index=["5","6","7","8"])
rst21=pd.concat([ser1,ser2]) #axis不填，其默认值axis=0，按行拼接，行数变多；
rst22=pd.concat([ser1,ser2] ,axis=1)  #axis=1,返回结果是DataFrame ；按列拼接，列数变多；
rst23=pd.concat([ser1,ser2] ,keys=['p1','p2']) #keys选项:用于在拼接轴上创建等级索引，区分识别拼接的部分
rst24=pd.concat([ser1,ser2] ,axis=1,join='inner',keys=['p1','p2'])
print("ser1:\n",ser1)
print("array2:\n",array2)
print("2.1）pandas的contact()函数实现按轴拼接的功能-Series:rst21=pd.concat([ser1,ser2]),rst21:\n",rst21)
print(f"2.2）pandas的contact()函数实现按轴拼接的功能-Series，rst22=pd.concat([ser1,ser2] ,axis=1) "
      f"(*axis=1,返回结果是DataFrame ；按列拼接，列数变多),rst22:\n{rst22}\n"
      f"    *axis=1,返回结果是DataFrame ；按列拼接，列数变多")
print(f"2.3）keys选项:用于在拼接轴上创建等级索引，区分识别拼接的部分：rst23=pd.concat([ser1,ser2] ,keys=['p1','p2']) :\n {rst23}\n")
print(f"2.4）join选项:rst24=pd.concat([ser1,ser2] ,axis=1,join='inner',keys=['p1','p2']):\n {rst24}\n")


#举例2）pandas的contact()函数实现按轴拼接的功能- DataFrame
df1=pd.DataFrame(np.random.randn(9).reshape(3,3),columns=['A','B','C'],index=['1','2','3'])
df2=pd.DataFrame(np.random.randn(9).reshape(3,3),columns=['A','B','C'],index=['4','5','6'])
df_rst1=pd.concat([df1,df2],keys=['p1','p2'])
df_rst2=pd.concat([df1,df2],axis=1,keys=['p1','p2'])
print("DataFrame:df1:\n {df1}")
print("DataFrame:df2:\n {df2}")
print(f"2.5）pandas的contact()函数实现按轴拼接的功能-DataFrame:df_rst1=pd.concat([df1,df2],keys=['p1','p2']):\n {df_rst1}")
print(f"2.6）pandas的contact()函数实现按轴拼接的功能-DataFrame:df_rst2=pd.concat([df1,df2],axis=1,keys=['p1','p2']):\n {df_rst2} ")

#---- 【end】6.1.2-数据准备-组装：拼接(concatenation)----#

#---- 【start】6.1.1-数据准备-组装：组合(combine) -填充缺失值----#

print("6.1.3-数据准备-组装：组合(combine)-填充缺失值:两个数据集的索引完全或部分重合,只用重叠的其中一个的值，无法通过合并或拼接方法组合数据，用组合。\n"
      f"combine_first()函数可以用来组合Series对象,同时对齐数据")
ser3=pd.Series(np.random.randn(5),index=[1,2,3,4,5])
ser4=pd.Series(np.random.randn(4),index=[4,5,6,7])
ser_rst1=ser3.combine_first(ser4)
ser_rst2=ser4.combine_first(ser3)
ser_rst3=ser3[:3].combine_first(ser4[:3])  #指定部分合并
print(f"Series对象:ser3:\n {ser3}")
print(f"Series对象:ser4:\n {ser4}")
print(f"2.5）combine_first()函数用来组合,同时对齐数据:ser_rst1=ser3.combine_first(ser4):\n{ser_rst1}\n"
      f"    *若两个数据集的索引完全或部分重合,只用重叠的其中一个的值\n"
      f"    如ser3和ser4都有索引4,ser3.combine_first(ser4) 重合的取ser3，因为ser3.combine_first "
      f"     ser3.combine_first(ser4) ")
print(f"2.6）combine_first()函数用来组合,同时对齐数据:ser_rst2=ser4.combine_first(ser3):\n{ser_rst2}\n")
print(f"2.6）combine_first()函数用来组合,同时对齐数据,指定部分合并:ser_rst3=ser3[:3].combine_first(ser4[:3]):\n{ser_rst3}\n")

df1 = pd.DataFrame({'key': ['A', None, 'C'], 'val1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'val2': [4, 5, 6]})
df3 = pd.DataFrame({'A': [3, 3, None,4], 'B': [3, None, 3,8]})
result_merge = pd.merge(df1, df2, on='key', how='outer') #how='inner' 键值对齐
rst_concat=pd.concat([df1, df2],keys=['d1','d2']) #堆叠数据（行/列）;	轴对齐
rst_concat1=pd.concat([df1, df2,df3],keys=['d1','d2','d3'],axis=1) #堆叠数据（行/列）;轴对齐
rst_combine = df1.combine_first(df2) #填充缺失值（优先保留非空）;索引对齐

#python 的combine_first() 和contranct()，merge()

print(f"df1:\n{df1}")
print(f"df2:\n{df2}")
print(f"df3:\n{df3}")
print(f"result_merge()多表关联（基于列）;键值对齐:"
      f"result_merge = pd.merge(df1, df2, on='key', how='outer'):\n{result_merge}")
print(f"rst_concat堆叠数据（行/列）;轴对齐:"
      f"rst_concat=pd.concat([df1, df2],keys=['d1','d2'])\n"
      f"{rst_concat}\n")
print(f"rst_concat1 (axis=1)堆叠数据（行/列）;轴对齐:"
      f"rst_concat1=pd.concat([df1, df2,df3],keys=['d1','d2','d3'],axis=1)\n"
      f"{rst_concat1}\n")
print(f"rst_combine()填充缺失值（优先保留非空）;索引对齐:"
      f"rst_combine = df1.combine_first(df2)\n"
      f"{rst_combine}\n")

#---- 【end】6.1.1-数据准备-组装：组合(combine) -填充缺失值----#

#---- 【start】6.1.1-数据准备-组装：轴向旋转----#

print("6.1.1-数据准备-组装：轴向旋转:\n"
      "1)按等级索引旋转,调整dataFrame对象中的数据（dataFrame支持等级索引）。轴旋转有两个基本操作:\n"
      "    入栈(stacking)：旋转数据结构，把将列索引转换为行索引,列转换为行\n"
      "    出栈(unstacking)：把行转换为列\n")
print("2)从“长”格式向“宽”格式旋转:"
      "    pivot():基于列值重塑数据 ,适用于将列值转换为行/列索引。不支持数据聚合（多值会生成 MultiIndex 列）\n")

print(f"举例：1)按等级索引旋转:stack()入栈 ; unstack()出栈\n")
#举例：1)按等级索引旋转,调整dataFrame对象中的数据（dataFrame支持等级索引）。轴旋转有两个基本操作:\n"
# frame2=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],'color':['white','red','red','black','green'], 'brand':['OMG','ABC','ABC','POD','POD']})
frame1=pd.DataFrame(np.arange(9).reshape(3,3),columns=['ball','pen','pencil'],index=['whith','black','red'])
stack_frame=frame1.stack().copy()
unstack_frame=stack_frame.unstack() #unstack()出栈,把行转换为列:
unstack_frame2=stack_frame.unstack(1) #传入表示层级的编号后名称，对相应层级进行操作
# frame1.loc['red','ball']=9
print(f"frame1:\n{frame1}\n") #传入表示层级的编号后名称，对相应层级进行操作
print(f"stack()入栈:旋转数据结构，把列转换为行,得到一个Series对象:\n{frame1.stack()}\n")
print(f"stack_frame:\n{stack_frame}\n")
print(f"unstack()出栈,把行转换为列:unstack_frame=stack_frame.unstack():\n{unstack_frame}\n")
print(f"unstack()出栈,把行转换为列,传入表示层级的编号（编号从0开始）或名称，对相应层级进行操作:stack_frame.unstack(1):\n{stack_frame.unstack(0)}\n")

#举例：2)从“长”格式向“宽”格式旋转\n
print(f"举例：2)从“长”格式向“宽”格式旋转:pivot():基于列值重塑数据 ,适用于将列值转换为行/列索引。不支持数据聚合（多值会生成 MultiIndex 列）\n")
long_df=pd.DataFrame({'color':['white','white','white',
                               'red','red','red',
                               'black','black','black'],
                      'item':['ball','pen','mug',
                              'ball','pen','mug',
                              'ball','pen','mug'],
                      'value':np.random.randn(9)})

widefram=long_df.pivot(index='item', columns='color')
# widefram=long_df.pivot(index='color', columns='item')
print(f"“长”格式(各列都有数据，每一列后面的数据常跟前面的有所重复，通常列表形式):widefram ： \n{long_df}\n")
print(f"pivot() 从“长”格式向“宽”格式旋转：widefram=long_df.pivot(index='item', columns='color')\n{widefram}\n ")

#stack()、unstack() 和 pivot() 在 Pandas 中的详细对比与用法说明
print(f"汇总：stack()、unstack() 和 pivot() 在 Pandas 中的对比与用法，举例如下：")
df1 = pd.DataFrame({'key': ['A', None, 'C'], 'val1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'val2': [4, 5, 6]})
df3 = pd.DataFrame({'A': [3, 3, None,4], 'B': [3, None, 3,8]})
result_merge = pd.merge(df1, df2, on='key', how='outer') #how='inner' 键值对齐
rst_concat=pd.concat([df1, df2],keys=['d1','d2']) #堆叠数据（行/列）;	轴对齐
rst_concat1=pd.concat([df1, df2,df3],keys=['d1','d2','d3'],axis=1) #堆叠数据（行/列）;轴对齐
rst_combine = df1.combine_first(df2) #填充缺失值（优先保留非空）;索引对齐


print(f"df1:\n{df1}")
print(f"df2:\n{df2}")
print(f"df3:\n{df3}")
print(f"result_merge()多表关联（基于列）;键值对齐:"
      f"result_merge = pd.merge(df1, df2, on='key', how='outer'):\n{result_merge}")
print(f"rst_concat堆叠数据（行/列）;轴对齐:"
      f"rst_concat=pd.concat([df1, df2],keys=['d1','d2'])\n"
      f"{rst_concat}\n")
print(f"rst_concat1 (axis=1)堆叠数据（行/列）;轴对齐:"
      f"rst_concat1=pd.concat([df1, df2,df3],keys=['d1','d2','d3'],axis=1)\n"
      f"{rst_concat1}\n")
print(f"rst_combine()填充缺失值（优先保留非空）;索引对齐:"
      f"rst_combine = df1.combine_first(df2)\n"
      f"{rst_combine}\n")


#---- 【end】6.1.1-数据准备-组装：轴向旋转----#

#---- 【start】6.1.1-数据准备-组装:删除数据----#
print("6.1.1-数据准备-组装:删除数据:删除多余的行和列：del ")
frame1=pd.DataFrame(np.arange(9).reshape(3,3),columns=['ball','pen','pencil'],index=['white','black','red'])
print(f"frame1:\n {frame1}")
del frame1['ball'] #删除列del
print(f"1）删除列del:如 del frame1['ball']:\n ",frame1)
drop_frame1=frame1.drop('white')  #删除行drop
print(f"2）删除行drop:如 drop_frame1=frame1.drop('white'):\n ",drop_frame1)
# print(f"frame1:\n {frame1}")


#---- 【end】6.2-数据准备-组装:删除数据----#



#---- 【start】6.2-数据处理 ----#
#---- 【end】6.2-数据处理 ----#


# print(f"2.6）pandas的contact()函数实现按轴拼接的功能-DataFrame:df_rst2=pd.concat([df1,df2],axis=1,keys=['p1','p2']):\n {df_rst2} ")


#---- 【end】6.1.1-数据准备-组装：组合(combine)----#

# 1）pd.merge() on选项指定基于哪列合并，若不指定用相同列字段。没有相同的列字段。left_on选项指定第一个dataFrame基于哪列合并;right_on第二个dataFrame的.
# 2）merge()默认执行内连接操作。how选项指定连接类型，如：inner内连接;left左连接; right右链接;outer外连接
# 3）可用根据索引合并，用索引作为键，把left_index和right_index选项的值置为True,将其激活，就可将其作为合并dataFrame的基准。
#---- 【end】6.1-数据准备-组装：合并（merging）  ----#

#---- 【start】6.2-数据处理 ----#
#---- 【end】6.2-数据处理 ----#


frame1=pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                     'color':['white','red','red','black','green'],
                     'brand':['OMG','ABC','ABC','POD','POD']})
frame3=pd.DataFrame({'sid':['pencil','pencil','ball','pen'],
                    'brand':['OMG','POD','ABC','POD']})
