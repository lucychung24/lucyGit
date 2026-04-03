import pandas as pd
import numpy as np

#pandas数据转换：
#---- 【start】6.2-数据转换 ----#
# print("6.2.1-数据转换：删除重复数据")
# print("6.2.2-数据转换：映射")
#---- 【start】6.2.1-数据转换：删除重复数据 ----#

print("6.2.1-数据转换：显示重复数据（df.duplicated()）、 删除重复数据 （drop_duplicates()删除重复项的记录后的数据）")
df=pd.DataFrame({'coloe':['white','white','red','red','green','blue'],
                 'value':[10,20,30,30,50,60]})
#keep : {'first', 'last', False}, default 'first'
df = pd.DataFrame({
'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
'rating': [4, 4, 3.5, 15, 5]})

print('1)df.duplicated() 重复项返回True,举例如下：')
#df.duplicated() 重复项返回True
print(f"df :\n {df}")
print(f" df.duplicated() 重复项返回True: \n{df.duplicated()}")
print(f"subset`: 指定用于判断重复的列名列表，默认使用所有列:df.duplicated(subset=['brand'])重复项返回True :\n {df.duplicated(subset=['brand'])}")
print(f"df.duplicated(subset=['brand','style'])重复项返回True :\n {df.duplicated(subset=['brand','style'])}")
print(f"keep='first'（保留第一次出现的行，标记后续重复行为 True）:df.duplicated(subset=['brand','style'],keep='first')重复项返回True:\n {df.duplicated(subset=['brand','style'],keep='first')}")
print(f"keep='last'（保留最后一次出现的行，标记之前重复行为 True）,df.duplicated(subset=['brand','style'],keep='last')重复项返回True:\n {df.duplicated(subset=['brand','style'],keep='last')}")
print(f"keep=False（标记所有重复行为 True）,df.duplicated(subset=['brand','style'],keep=False)重复项返回True: \n {df.duplicated(subset=['brand','style'],keep=False)}")

#返回重复项的记录，使用df[df.duplicated()]
print('2)df[df.duplicated()]返回重复项的记录,举例如下：')
print(f"返回重复项的记录，使用df[df.duplicated()] ：df[df.duplicated(subset=['brand','style'],keep='first')] : \n {df[df.duplicated(subset=['brand','style'],keep='first')]}")

print('3)drop_duplicates()删除重复项的记录后的数据,举例如下：')
print(f"df :\n {df}")
print(f"subset`: 指定用于判断重复的列名列表，默认使用所有列:df.duplicated(subset=['brand'])重复项返回True :\n {df.duplicated(subset=['brand'],keep='first')}")
drop_dupl_data=df.drop_duplicates(subset=['brand'],keep='first')
print(f"drop_duplicates()删除重复项的记录后的数据，使用df.drop_duplicates() ：drop_dupl_data=df.drop_duplicates(subset=['brand'],keep='first')] : \n {df[df.duplicated(subset=['brand','style'],keep='first')]}")

#duplicated():它返回一个布尔值的 Series，指示每一行是否是重复项。
# 主要参数包括：
# - `subset`: 指定用于判断重复的列名列表，默认使用所有列。
# - `keep`: 指定如何标记重复行，可选值为
#          'first'（保留第一次出现的行，标记后续重复行为 True）、
#          'last'（保留最后一次出现的行，标记之前重复行为 True）、
#          False（标记所有重复行为 True）。
# def duplicated(self,
#                subset: Hashable | Sequence[Hashable] | None = None,
#                keep: Literal["first", "last", False] = "first")
#   -> Series
# subset : column label or sequence of labels, optional Only consider certain columns for identifying duplicates,
#     by default use all of the columns.
# keep : {'first', 'last', False}, default 'first' Determines which duplicates (if any) to mark.
#      - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
#      - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
#     - False : Mark all duplicates as ``True``


#---- 【end】6.1.1-数据转换：删除重复数据 ----#


#---- 【start】6.2.2-数据转换：映射） ----#

# print("6.2.2-数据转换：映射")
print("6.2.2-数据转换：映射：映射关系就是创建一个映射关系列表，把元素跟一个特定的标签或字符串绑定起来。\n"
      "下面这几个函数都一表示映射关系的dict对象作为参数。\n"
      "  replace():替换元素\n"
      "  map():新建一列\n"
      "  rename():替换索引\n")
print("举例-1）replace():替换元素\n")
df=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                 'color':['white','rosso','verde','black','yellow'],
                 'price':[5.56, 4.20, 1.30,0.56, 2.75 ]})
newcolor={'rosso':'red','verde':'green'}  #表示映射关系的dict对象
print(f"df (有两个颜色不是英文词汇（'rosso','verde'）) :\n {df}\n")
print(f"表示映射关系的dict对象,newcolor :\n {newcolor}")
print("1.1)replace():替换元素,替换两个颜色不是英文词汇 :df.replace(newcolor) :\n",df.replace(newcolor))

ser=pd.Series([1,3,np.nan,5,np.nan,9])
ser.replace(np.nan,0)
print(f"ser : {ser}")
print("1.2)replace():替换元素,把Nan替换为其他值 :ser.replace(np.nan,0) :\n:",ser.replace(np.nan,0))

print("\n6.2.2-数据转换：映射-1）map():新建一列,如用映射添加元素\n 举例")

df2=pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                 'color':['white','rosso','verde','black','yellow']})
price={'ball':5,'mug':4,'bottle':1.3,'scissors':3.41,'pen':1,'pencil':0.5,'ashtray':2.7} #用字典price

print(f"df2 :\n {df2}\n")
print(f"price (表示映射关系的dict对象):\n {price}\n")

df2['price']=df2['item'].map(price) #新建一列,如用映射添加元素,用字典price作为参数，为df2对象中产品添加price列
print("2.1)map():新建一列,如用映射添加元素,用字典price作为参数，为df2对象中产品添加price列 :df2['price']=df2['item'].map(price) :\n",df2)

print("6.2.2-数据转换：映射-3）rename():替换索引:如使用映射关系转换轴标签\n")

reindex={0:'first',1:'second',2:'third',3:'fourth',4:'fifth'} #
recolumn={'item':'object','price':'value'}
print(f"df2 :\n {df2}\n")
print(f"reindex（要替换索引标签的映射关系的dict定义） :\n {reindex}\n")
print(f"recolumn（要替换列标签的映射关系的dict定义） :\n {recolumn}\n")
print(f"rename():替换索引/列标签:如使用映射关系转换对象df2的轴标签（如索引和列标签）：df.rename(index=reindex,columns=recolumn):\n {df.rename(index=reindex,columns=recolumn)}\n")

#---- 【end】6.2.2-数据转换：映射 ----#

#---- 【start】6.2.3-数据转换：离散化和面元划分：cut() 、qcut()----#

print("6.2.3-数据转换：离散化和面元划分：cut()、qcut()")
print("6.2.3-1)离散化和面元划分：cut()")
# 创建示例数据
# result = pd.Series(np.random.rand(15) * 100) #生成20个0-100范围内的随机数作为示例数据
result = pd.Series(np.random.random_integers(0,100,17) )
# 定义分箱区间
bins = [0, 25, 50, 75, 100] #定义一数组，存储用于面元划分的个数值
# 使用pandas.cut()进行分箱
# cat = pd.cut(result, bins, right=True, labels=['0-25', '25-50', '50-75', '75-100'], include_lowest=True)
# cat = pd.cut(result, bins, labels=['0-25', '25-50', '50-75', '75-100']) #设置right=True表示包含右侧边界, right的默认值是True
cat = pd.cut(result, bins)
print("原始数据result:\n", result)
print("\n1)分箱结果 cat = pd.cut(result, bins):\n", cat)
print("\n2)分箱结果,每个面元出现的次数 pd.Series(cat).value_counts() :\n", pd.Series(cat).value_counts()  ) # pd.Series(cat).value_counts() 替换旧的pd.value_counts(cat)
#pandas.value_counts is deprecated and will be removed in a future version。use  pd.Series(obj).value_counts() instead.

#lable选项，指定面元的名称
bin_name={'unlikely','less likely','likely','highly likely'}
cat = pd.cut(result, bins,labels=bin_name)
print("bin_name :\n", bin_name)
print("\n3)分箱结果,lable选项，指定面元的名称 cat = pd.cut(result, bins,labels=bin_name):\n", cat)

print("\n4)分箱结果:若不指定面元的各边界限，而传入一个整数作为参数，cut()函数会按照指定的数字，"
      "把数组元素的取值范围划分为相应的几部分，每个区间的上下限取决于样本数据"
      "如： cat = pd.cut(result, 5):\n", pd.cut(result, 5))

print("6.2.3-2)离散化和面元划分：qcut()函数能保证每个面元的个体数相同，但每个面元的区间大小不等")
quintiles=pd.qcut(result,5)
print("原始数据result:\n", result)
print("\n1)qcut()分箱结果 quintiles=pd.qcut(result,5):\n", quintiles)
print("\n2)qcut()分箱结果,每个面元出现的次数尽量相同等分 pd.Series(cat).value_counts() :\n", pd.Series(quintiles).value_counts()  )


#---- 【end】6.2.3-数据转换：离散化和面元划分：cut() ----#

#---- 【start】6.2.4-数据转换：异常值检测和过滤 ----#

print("6.2.4-数据转换：异常值检测和过滤")
print("举例1：将元素比标准差大3倍的元素视作异常值，筛选出这异常值。每一列的值跟每一列的3倍标准差比较，其中一列值>3倍标准差,返回该列所在行的数据")

randframe=pd.DataFrame(np.random.randn(1000,3)) #创建3列dataframe对象，每列1000个随机数
randframe.describe()  #describe()查看每一列的描述性统计量
randframe.std() #std() 标准差
#如：将元素比标准差大3倍的元素视作异常值，筛选出这异常值。
#   每一列跟每一列的3倍标准差比较，其中一列>3倍标准差,返回该列所在行的数据
#any() 方法的 axis 参数应通过关键字参数传递.any(axis=1) 明确指定按行（列索引）检查，返回布尔 Series（每行是否满足条件）。
# np.abs(randframe) > (3 * randframe.std()) 生成布尔 DataFrame（元素是否超过 3 倍标准差）。
# .any(axis=1) 检查每行是否有任意元素满足条件（即绝对值超过 3 倍标准差）
excep_data=randframe[(np.abs(randframe) > (3*randframe.std())).any(axis=1)]

print(f"randframe=pd.DataFrame(np.random.randn(1000,3)) #创建3列dataframe对象，每列1000个随机数:\n{excep_data}")
print(f"randframe.describe()  #describe()查看每一列的描述性统计量:\n{randframe.describe()}")
print(f"randframe.std() #std() 标准差:\n{randframe.std()}")
print(f"元素比标准差大3倍的元素视作异常值，筛选出这异常值。"
      f"每一列的值跟每一列的3倍标准差比较，其中一列值>3倍标准差,返回该列所在行的数据。\n"
      f"# np.abs(randframe) > (3 * randframe.std()) 生成布尔 DataFrame（元素是否超过 3 倍标准差）。\n"
      f"# .any(axis=1) 检查每行是否有任意元素满足条件（即绝对值超过 3 倍标准差）\n"
      f"如：excep_data=randframe[(np.abs(randframe) > (3*randframe.std())).any(axis=1)]:\n{excep_data}")

#---- 【end】6.2.4-数据转换：异常值检测和过滤----#

#---- 【end】6.2.5-数据转换：排序及抽取部分数据----#

print("6.2.5-数据转换：排序及抽取部分数据:dataFrame.take()")
nframe=pd.DataFrame(np.arange(25).reshape(5,5))
# permutation()：返回打乱顺序的数组或整数范围
neworder=np.random.permutation(5) #permutation(5) 创建一个包含0-4，顺序随机的这5个整数的数组。
# np.random.randint(5,15,5) # randint()：返回指定范围内的随机整数或整数数组（如 [3, 7, 1]）

print(f"原始的nframe=\n{nframe}\n")
print(f"neworder一个包含0-4，顺序随机的这5个整数的数组:neworder=np.random.permutation(5) :\n{neworder}\n")
#对dataFrame对象的所有行应用take()函数，把新的次序传给它
new_nframe=nframe.take(neworder,axis=0) #axis : {0 or 'index', 1 or 'columns', None}, default 0
print(f"1)应用take()函数，调整nframe的新次序,nframe各行/列的根据neworder的顺序调整。\n"
      f"如：根据neworder根据neworder的顺序调整nframe各行\n "
      f"new_nframe=nframe.take(neworder,axis=0) ：\n{new_nframe}\n")

neworder2=[3,4,2] #只对nframe的一部分数据排序: 指定排序的部分数据
new_nframe2=nframe.take(neworder2,axis=0)
print(f"2)只对nframe的一部分数据排序。")
print(f"A)neworder2指定排序的部分数据：neworder2=[3,4,2]，neworder2：\n{neworder2}\n")
print(f"B)只对nframe的一部分数据排序：new_nframe2=nframe.take(neworder2,axis=0)：\n{new_nframe2}\n")


#随机取样：dataframe的数据
neworder3=np.random.randint(0,len(nframe),3) #生成随机顺序的数
new_nframe3=nframe.take(neworder3,axis=0)
print(f"3)随机取样：dataframe的数据: 如随机取样：dataframe的数据很大，可能需要随机取样，最快的方法使用np.random.randint()生成随机顺序的数。")
print(f"A)neworder3生成随机顺序的部分数据：neworder3=np.random.randint(0,len(nframe),3) #生成随机顺序的数：\n{neworder3}\n")
print(f"B)对nframe随机取样一部分数据：new_nframe3=nframe.take(neworder3,axis=0)：\n{new_nframe3}\n")


# permutation()：返回打乱顺序的数组或整数范围（如 [1, 2, 0, 3, 4]）。
# randint()：返回指定范围内的随机整数或整数数组（如 [3, 7, 1]）。
# # permutation() 示例
# print(np.random.permutation(5))  # 输出: [1 2 0 3 4] (打乱顺序)
# print(np.random.permutation([1, 2, 3]))  # 输出: [2 1 3] (打乱数组)
#
# # randint() 示例
# print(np.random.randint(1, 10))  # 输出: 3 (单个随机整数)
# print(np.random.randint(1, 10, size=(3, 4)))  # 输出: 3x4 随机整数矩阵

# print(f"表示映射关系的dict对象,newcolor :\n {newcolor}")

#---- 【end】6.2.5-数据转换：排序-----#


#---- 【start】6.2.6-字符串处理-内置的字符串处理方法、正则表达式） ----#

print("6.2.6-1）字符串处理-内置的字符串处理方法")

text='16 Bolton Avenue , Bolton'
tokens = [s.strip() for s in text.split(',') ] #strip()删除多余的空白字符（包括换行符）
address,city =[s.strip() for s in text.split(',') ]  #元素数量较少且固定不变，可用这赋值方法
print(f"text='16 Bolton Avenue , Bolton', text: {text}")
print(f"举例1.1) split()函数，分隔,如text.split(','):\n {text.split(',') }\n")
print(f"举例1.2) strip()函数，删除多余的空白字符（包括换行符）,\n"
      f"如address,city =[s.strip() for s in text.split(',') ] 分别赋值address,city ,\n"
      f"   执行后address是：{address}  \n "
      f"        city是 : {city}\n")

# address+ ','+ city
print(f"举例1.3) 文本拼接方法：1）用+运算符： 如：address+ ','+ city 执行后:\n {address+ ','+ city }")

strings=['A+','A','A-','B','BB','BBB','C+']
';'.join(strings) #join(),在作为连接符的字符上调用join函数，这是更实用的方法
print(f"\n举例1.3) 文本拼接方法：2）join(),在作为连接符的字符上调用join函数，这是更实用的方法。\n"
      f"  如用';'作为连接符，在这字符上调用join函数,拼接strings的内容:\n "
      f"   strings的内容 ：\n{strings }\n"
      f"   ';'作为连接符，在这字符上调用join函数,拼接strings的内容，如';'.join(strings) 执行后 ：\n{';'.join(strings) }\n")
print(f"举例1.4) 查找子串：1）python的in关键字，检查子串的最好方法：如 ‘Bolton’ in text 执行后:\n {'Bolton' in text }\n")
print(f"举例1.4) 查找子串：2）index()函数实现字符串查找，返回子串在字符串中的索引。若没找到会报错。\n "
      f"举例1.4) 查找子串：3）find()函数实现字符串查找，返回子串在字符串中的索引。若没找到会返回-1。\n"
      f"  如 text.index('Bolton') 执行后返回：{text.index('Bolton') }\n"
      f"  如 text.find('Bolton') 执行后返回：{text.find('Bolton') }\n"
      f"  如 若没找到text.index('New York') 执行后,会报错‘ValueError: substring not found’\n" #：{text.index('New York')}
      f"  如 若没找到text.find('New York') 执行后返回：{text.find('New York')}\n"
      )

print(f"举例1.5) 字符串或字符串组合在文本中出现的次数count()函数：\n"
      f"  如 text.count('e')，执行后返回:  {text.count('e')} \n"
      f"  如 text.count('Avenue')，执行后返回: {text.count('Avenue')}\n")

print(f"举例1.6) 替换或删除字符串中的子串或单个字符：replace()函数：\n"
      f"  text: {text}\n"
      f"  如 text.replace('Avenue','Street')，执行后返回:  {text.replace('Avenue','Street')} \n"
      f"  如 text.replace('6','')，执行后返回: {text.replace('6','')}\n")


print("6.2.6-2）字符串处理-正则表达式：（导入python内置的re模块才能使用正则表达式）")
#python内置的re模块，用于操作regex对象。导入re模块才能使用正则表达式
import re
text="This is   an\t odd  \n  text!"
# re.split(r'\s+',text)  #正则表达式'\s+'表示一个或多个空白字符串

print(f"原始的text :\n  {text}\n")
print("举例1）re模块的split()函数：正则表达式'\\s+'表示一个或多个空白字符串\n"
      "  如：用正则表达式'\\s+' 分隔数据text，re.split(r'\\s+',text) "
      "\n   执行后返回:"
      f"    {re.split(r'\s+',text)}\n")

regex=re.compile(r'\s+') # compile()函数先预编译正则表达式
regex.split(text) #在调用它split()函数，达到跟‘例1）’一样的分隔
print("*re模块的工作原理：如调用re.split()函数时，首先编译正则表达式；然后在作为参数传入的文本上调用split()函数。\n"
      "   re.compile()函数编译正则表达式，得到一个可以重用的正则表达式对象，从而节省CPU周期,提高效率。")
print("举例2）用re.compile()函数先预编译正则表达式，在调用它split()函数，达到跟‘例1）’一样的分隔。\n"
      "   如A)re.compile()函数先预编译正则表达式,如regex=re.compile(r'\\s+') \n "
      f"    B)在调用它split()函数，达到跟‘例1）’一样的分隔,\n"
      f"         如regex.split(text) 执行后: {regex.split(text)}\n")

text ='This is my address: 16 Bolton Avenue, Boston; Apple street, San Francisco'
#找出字符串text中所有以大写字母A开头的单词
re.findall(r'A\w+',text)
#找出字符串text中所有以字母A开头的单词,字母A不区分大小写
re.findall(r'[A,a]\w+',text)
print("举例3）findall()函数,匹配文本中所有符合正则表达式的子串。返回一个列表，元素为所有符合正则表达式的子串。\n"
      "  如：找出字符串所有以大写字母A开头的单词。\n"
      f"     A)text: {text}\n"
      f"     B)找出字符串text中所有以大写字母A开头的单词: \n"
      "       re.findall(r'A\\w+',text)\n"
      f"      执行后返回：{re.findall(r'A\w+',text)}\n "
      f"     C)找出字符串text中所有以字母A开头的单词,字母A不区分大小写,: \n"
      "       re.findall(r'[A,a]\\w+',text)\n"
      f"      执行后返回：{re.findall(r'[A,a]\w+',text)}\n ")

#search()函数,返回第一处符合模式的子串，其返回结果是一个特殊类型的对象，该对象是子串在字符中的开始和结束位置。
re.search(r'[A,a]\w+',text)
search = re.search(r'[A,a]\w+',text)
search.start() #子串在字符中的开始和结束位置
search.end() #子串在字符中的开始和结束位置
print("举例4）search()函数,返回第一处符合模式的子串，其返回结果是一个特殊类型的对象，该对象是子串在字符中的开始和结束位置。\n"
      f"  如：re.search(r'[A,a]\\w+',text) \n"
      f"     执行返回:  {re.search(r'[A,a]\w+',text)}\n\n"
      f"  如：search = re.search(r'[A,a]\\w+',text) \n"
      f"     执行后，获取子串在字符中的开始和结束位置: "
      f"     search.start() #子串在字符中的开始位置：{search.start()}\n"
      f"     search.end() #结束位置 :{search.end()}\n"
      )

re.match(r'[A,a]\w+',text)  #没能找到任何匹配的子串，它不会返回任何对象
match_retrun=re.match(r'[t,T]\w+',text)  #其返回结果是一个特殊类型的对象，该对象是子串在字符中的开始和结束位置
print("举例5）match()函数,从字符串开头开始匹配，如果第一个字符就不匹配，它就不会在搜索字符串内部。\n"
      "      如果没能找到任何匹配的子串，它不会返回任何对象。\n"
      "      如果有返回内容，其返回结果是一个特殊类型的对象，该对象是子串在字符中的开始和结束位置。跟search()函数返回相同\n\n"
      f"     A)text: {text}\n"
      "      如：re.match(r'[A,a]\\w+',text) \n"
      f"         执行结果：没能找到任何匹配的子串，它不会返回任何对象 {re.match(r'[A,a]\\w+',text)}"
      "      如：match_retrun=rre.match(r'[t,T]\\w+',text) \n"      
      f"         执行结果：如果有返回内容，其返回结果是子串在字符中的开始和结束位置 \n"
      f"         执行后，获取子串在字符中的开始和结束位置:\n "
      f"         match_retrun.start() #子串在字符中的开始位置：{match_retrun.start()}\n"
      f"         match_retrun.end() #结束位置 :{match_retrun.end()}\n"
      )

#---- 【end】6.2.6-字符串处理-内置的字符串处理方法、正则表达式----#





#---- 【start】6.2.2-数据转换：映射） ----#
# print("6.2.2-数据转换：映射")
# print("6.2.1-数据转换：删除重复数据")
#---- 【end】6.2.2-数据转换：映射 ----#