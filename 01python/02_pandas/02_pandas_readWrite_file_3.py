#pandas数据读写：I/O API工具：2）读写HTML文件： read_csv()、read_table()、to_csv()
#如今很多网站为避免模块缺失和错误信息，已采用html5格式，因此建议安装html5lib模块。若使用anaconda,安装命令为 canda install html5lib
import numpy as np
import pandas as pd

#---- 【start】 ----#
#---- 【end】 ----#

#---- 【start】5.2-读写HTML文件 ----#

print("---【start】5.2-读写HTML文件----\n")
print("5.2-读写HTML文件:read_html(),to_html() \n"
      "如今很多网站为避免模块缺失和错误信息，已采用html5格式，因此建议安装html5lib模块。若使用anaconda,安装命令为 canda install html5lib \n")

frame=pd.DataFrame(np.arange(16).reshape(4,4),columns=['ball','pen','pencil','paper'],index=['yellow','red','blue','green'])
print("5.2.1-写HTML文件:to_html()函数，可以直接把DataFrame转换为html表格。（DataFrame的内部结构被自动转换为钱入在表格中的<TH>、<TR>、<TR>标签，保留所有内部层级结构） \n"
      "1）to_html()函数的调用"
      f"  举例：如dataFrame对象frame的内容：\n {frame} \n"
      f"  调用dataframe实例上调用to_html()函数，如 frame.to_html() 执行后,正确生成创建html表格所需的html标签：\n {frame.to_html()} \n")

print("2）生成一个字符串并把它写入到html页面上:\n"
      "  步骤1：创建一个包含HTML页面代码的字符串\n"
      "  步骤2：把包含HTML页面代码的字符串，写入到html文件中，如文件myFrame.html文件\n")
#步骤1：创建一个包含html页面代码的字符串
s=['<HTML>']
s.append('<HEAD><TITLE>myFrame.html</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html() ) #frame.to_html() 把DataFrame转换为html表格的数据
s.append('</BODY></HTML>')
html=''.join(s)
print(f"练习步骤1：创建一个包含HTML页面代码的字符串,变量html字符串的数据:\n {html}")

#步骤2：把包含html页面代码的字符串，写入到html文件中，如文件myFrame.html文件
html_file = open("pandas数据读写/myFrame.html",'w')
html_file.write(html)
html_file.close()
print(f"练习步骤2：把包含HTML页面代码的字符串，写入到html文件中，如文件myFrame.html文件:\n ")


# --open("pandas数据读写/myFrame.html",'w')---
#Character Meaning
#'r':open for reading (default)
#'w':open for writing, truncating the file first
#'x':create a new file and open it for writing
#'a':open for writing, appending to the end of the file if it exists
#'b':binary mode
#'t':text mode (default)
#'+':open a disk file for updating (reading and writing)


import lxml
print("\n\n5.2.1-读HTML文件:read_html()函数,解析HTML页面，寻找HTML表格。如果找到没将其转换为可以直接用于数据分析的DataFrame对象。返回DataFrame列表。\n"
      "    read_html()自动解析网页中的所有表格。通过table_index参数指定抓取第N个表格（索引从0开始）。read_html()函数最常用的模式是以网址作为参数，直接解析并抽取网页中的表格。\n")
read_hml_frame = pd.read_html("pandas数据读写/myFrame.html")
print("举例1：read_html()解析上面例子创建的HTML文件:read_html()\n"
      f"  如：read_hml_frame = pd.read_html(\"pandas数据读写/myFrame.html\"), read_hml_frame的内容：\n {read_hml_frame}")
print("\n\n5.2.1-read_html()函数")

#处理read_htlm()读网址url，报错urllib.error.HTTPError: HTTP Error 403: Forbidden
#from import lxml etree

#例2：read_html()函数最常用的模式是以网址作为参数
# 网址：网址打开显示的内容，如下：（HTML表格为一排行榜，包含用户名和得分两项）
# old url: http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/
# new url 报错，没找到表格: https://www.meccanismocomplesso.org/classifica-punteggio/
# url : https://blog.csdn.net/a1657054242/article/details/139934633
read_html_tab=pd.read_html("https://blog.csdn.net/a1657054242/article/details/139934633")
print("举例2：read_html()函数最常用的模式是以网址作为参数， 如下网址打开显示的内容，如下：（HTML表格为一排行榜，包含用户名和得分两项）\n"
      f"  如：ranking=pd.read_html('https://blog.csdn.net/a1657054242/article/details/139934633') "
      f"  操作后，返回ranking的内容 ranking[0]: \n {read_html_tab[0]}\n")

# FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
#   df_list = pd.read_html(str(soup.prettify()))
# 问题原因: 当前，read_html() 的 io 参数可以接受 URL、文件路径或类文件对象。但直接传递原始 HTML 字符串（字面量 HTML）已被弃用，因为这与函数统一接收类文件对象或 URL 的设计目标不一致
#解决方案:要解决此问题，您需要使用 io.StringIO 将 HTML 字符串包装成类文件对象。以下是具体方法

print("\nread_html() 的 io 参数可以接受 URL、文件路径或类文件对象。但直接传递原始 HTML 字符串（字面量 HTML）已被弃用,使用这会有警告。"
      "\n因为这与函数统一接收类文件对象或 URL 的设计目标不一致。"
      "\n要解决此问题，您需要使用 io.StringIO 将 HTML 字符串包装成类文件对象")
print("----使用 io.StringIO 将 HTML 字符串包装成类文件对象-----\n"
      "    如：html_stream = StringIO(table_html)  # table_html是HTML 字符串;\n"
      "       html_stream = StringIO(v_html.text)\n"
      "       df_list = pd.read_html(html_stream, flavor=\"html5lib\")  # flavor 可选 \"lxml\" 或 None")
import requests
from io import StringIO
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
#response = requests.get('https://blog.csdn.net/a1657054242/article/details/139934633', headers=headers)
#v_html ='https://blog.csdn.net/a1657054242/article/details/139934633'
v_html =requests.get('https://blog.csdn.net/a1657054242/article/details/139934633', headers=headers)
#print(f"v_html.text : {v_html.text}")
# 正确做法：使用 StringIO 包装 HTML 字符串
html_stream = StringIO(v_html.text)  #使用 io.StringIO 将 HTML 字符串包装成类文件对象
df_list = pd.read_html(html_stream, flavor="html5lib")  # flavor 可选 "lxml" 或 None
print(f"获取了多少个表格len(df_list): {len(df_list)}")
print("通过table_index参数指定抓取第N个表格（索引从0开始）如：获取第一个表格 df_list[0] 或第一个表格 df_list :")
df = df_list[0]  # 获取第一个表格 df_list 或 df_list[0]
print(df)


# HTML文件有多个表格：
v_html_2 =pd.read_html('pandas数据读写/a.html')
print("--v_html_2 --HTML文件有多个表格 len( v_html_2): " ,len(v_html_2))
print(f"--v_html_2 --HTML文件有多个表格,如有2个，查可第2个表格 v_html_2[1]： {v_html_2[1]}")

print("---【end】5.2-读写HTML文件----\n")

#---- 【end】5.2-读写HTML文件 ----#

# FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
#   df_list = pd.read_html(str(soup.prettify()))
# 问题原因: 当前，read_html() 的 io 参数可以接受 URL、文件路径或类文件对象。但直接传递原始 HTML 字符串（字面量 HTML）已被弃用，因为这与函数统一接收类文件对象或 URL 的设计目标不一致
#解决方案:要解决此问题，您需要使用 io.StringIO 将 HTML 字符串包装成类文件对象。以下是具体方法
## import pandas as pd
## from io import StringIO
## 
## # 示例：假设 table_html 是您的原始 HTML 字符串
## table_html = """
## <table>
##   <tr><th>项目</th><th>2023年</th><th>2022年</th></tr>
##   <tr><td>营业收入</td><td>5000万</td><td>4500万</td></tr>
##   <tr><td>净利润</td><td>800万</td><td>700万</td></tr>
## </table>
## """
## 
## # 正确做法：使用 StringIO 包装 HTML 字符串
## html_stream = StringIO(table_html)
## df_list = pd.read_html(html_stream, flavor="html5lib")  # flavor 可选 "lxml" 或 None
## df = df_list  # 获取第一个表格
## print(df)




#---- 【start】5.3-从XML文件读数据 ----#

print("---【start】5.3-从XML文件读数据----\n")
print("5.3-从XML文件读数据\n"
      "    pandas的所有I/O API函数中，没有专门处理XML格式的。Python有很多读写XML格式数据的库（除了pandas库）。\n"
      "    其中一个库叫作lxml,他在处理大文件方面行能优异，因而从众多类库之中脱颖而出。"
      "下面介绍用lxml处理XML文件，以及如何把它和pandas整合，最终从XML文件中获取到所需数据并将其转换为DataFrame。"
      "1）把XML文件中的数据结构转换为DataFrame对象，要用到lxml库的二级模块objectify ，是导入这方法（from lxml import objectify）\n")

print("5.3.1-步骤1）从XML文件读数据:lxml库的二级模块objectify,用parse()函数解析XML文件,返回树结构 \n")
#导入lxml库的二级模块objectif
from lxml import objectify  # 把XML文件中的数据结构转换为DataFrame对象，要用到lxml库的二级模块objectify
#用parse()函数解析XML文件
xml=objectify.parse("pandas数据读写/employees.xml")  # 返回的xml是一个树结构（lxml.etree._ElementTree object）。需要先定义根结构，才能获取到树结构的各个节点，
root = xml.getroot() # xml.getroot()，定义根结构
root.employee.name #获取单个节点：选择节点，依次指定标签，各标签之间用点号分隔（,）

#获取某个元素的所有子节点
root.getchildren() # getchildren()函数，获取某个元素的所有子节点
#再用tag属性，获取子节点tag属性的名称
[child.tag for child in root.employee.getchildren()] #再用tag属性，获取子节点tag属性的名称

#用text属性，获取到位于标签之间的内容
[child.text for child in root.employee.getchildren()] #用text属性，获取到位于标签之间的内容


#root.getchildren()[0].employee
print(f"  \n如xml=objectify.parse(\"pandas数据读写/employees.xml\")，执行后xml：{xml}")
print(f"   定义根结构【root = xml.getroot()】，执行后root：{root}\n"
      f"   A)获取单个节点：选择节点，依次指定标签，各标签之间用点号分隔（,），如root.employee.name: {root.employee.name} \n\n"
      f"   B)getchildren()函数，获取某个元素的所有子节点，再用tag属性，获取子节点tag属性的名称.\n"
      f"      如[child.tag for child in root.getchildren()] ：\n{root.getchildren()} \n"
      f"      如[child.tag for child in root.employee.getchildren()] ：\n{[child.tag for child in root.employee.getchildren()]} \n\n"
      f"   C)用text属性，获取到位于标签之间的内容 \n"
      f"      如：[child.text for child in root.employee.getchildren()] ：\n{[child.text for child in root.employee.getchildren()]}"
      )

print(f"5.3.1-步骤2）从XML文件读数据:把树结构转换为DataFrame对象 \n")


#定义函数：把树结构转换为DataFrame对象

print("-- 方法1:lxml库的二级模块二级模块objectify,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象 ***********")
print("提取数据 - star-----")
#定义函数：把树结构转换为DataFrame对象
# 提取数据
data = []
for employee in root.employee:
      row = {
            'id': int(employee.get('id')),
            'name': str(employee.name),
            'department': str(employee.department),
            'position': str(employee.position),
            'salary': float(employee.salary),
            'hiredate': str(employee.hiredate)
      }
      data.append(row)

# 创建DataFrame
df = pd.DataFrame(data)
print(f"方法1:把树结构转换为DataFrame对象,df的数据：\n{df}")
print(f"\n  其中df的数据类型 df.dtypes :\n{df.dtypes} \n")


#lxml库的二级模块etree 模块,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象
print("-- 方法2:lxml库的二级模块etree 模块,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象 ***********")
from lxml import etree
import pandas as pd

tree = etree.parse('pandas数据读写/employees.xml')
root = tree.getroot()
print(f"-- 1)tree = etree.parse('pandas数据读写/employees.xml'),root = tree.getroot(), 执行后root : {root}")
data = []
for item in root.findall('employee'):  # 假设XML中有多个<employee>节点
    row = {field.tag: field.text for field in item}
    data.append(row)

df = pd.DataFrame(data)
print(f"--方法2: 树结构转换为DataFrame对象, df的元素:\n {df}\n")

print("---【end】5.3-从XML文件读数据----\n")

'''
>>> root.getchildren()[0]
<Element employee at 0x1758f1151c0>

>>> root.getchildren()[0].getchildren()
['张三', '技术部', '软件工程师', 12000, '2023-05-15']

>>> len(root.getchildren()[0].getchildren())
5


a=[]
a.append({'c1':1,'c2':2,'c3':3})
a.append({'c1':4,'c2':5,'c3':6})
#a=[1,2,3,4,5,6,7,8,9,10]
print('a:\n',a)
df=pd.DataFrame(a)
print('df:\n',df)
print(df.dtypes)


a:
 [{'c1': 1, 'c2': 2, 'c3': 3}, {'c1': 4, 'c2': 5, 'c3': 6}]
 
df:
    c1  c2  c3
0   1   2   3
1   4   5   6

c1    int64
c2    int64
c3    int64
dtype: object
[{'c1': 1, 'c2': 2, 'c3': 3}, {'c1': 4, 'c2': 5, 'c3': 6}]

'''
#---- 【end】5.3-从XML文件读数据 ----#

#---- 【start】5.4-读写Excel文件 ----#

print("5.4-读写Excel文件")
print("5.4.1-写Excel文件：pd.read_excel()")
v_read_excel=pd.read_excel("pandas数据读写/data.xlsx")  # 默认读第一个sheet; 可用sheet_name=''指定sheet
#读第二个sheet，可用sheet_name=''指定sheet名；可用工作表的序号（索引）如第二个sheet的序号（索引）是2
v_read_excel_2=pd.read_excel("pandas数据读写/data.xlsx",sheet_name="Sheet2")  # 读第二个sheet,可用sheet_name=''指定sheet名；
v_read_excel_3=pd.read_excel("pandas数据读写/data.xlsx",1) # 读第二个sheet,可用工作表的序号（索引）如第二个sheet的序号（索引）是2
#print(v_read_excel_3)
print(f"  如：pd.read_excel(\"pandas数据读写/data.xlsx,sheet_name=\"Sheet2\")) 执行后: \n{v_read_excel}\n")

print("5.4.2-写Excel文件：pd.to_excel()")
#将dataFrame对象转换为excel
frame=pd.DataFrame(np.random.random((4,4)),index=['r1','r2','r3','r4'],columns=['Jan2000','Feb2000','Mar2000','Apr2000'])
print(f"1）dataFrame对象,frame的内容：\n{frame}\n")
frame.to_excel("pandas数据读写/output_data.xlsx")
print(f"2）将dataFrame对象转换为excel，如 frame.to_excel(\"pandas数据读写/output_data.xlsx\")：\n")
print("---【end】5.4-读写Excel文件据----\n")

#---- 【end】5.4-读写Excel文件 ----#


#---- 【start】5.5-读写JSON数据 ----#

print("5.5-读写JSON数据 ")
print("5.5.1-写JSON数据：to_json()，把dataframe转换为JSON文件 \n")
frame2=pd.DataFrame(np.random.random((4,4)),index=['r1','r2','r3','r4'],columns=['Jan2000','Feb2000','Mar2000','Apr2000'])
#print(frame2)
frame2.to_json("pandas数据读写/output_data.json") #把dataframe转换为JSON文件

print(f"  如：frame2的数据：\n{frame2} \n "
      f"  把dataframe转换为JSON文件，如：frame2.to_json(\"pandas数据读写/output_data.json\") \n ")

import json
print("5.5.2-读JSON数据：1)read_json()")
read_data=pd.read_json("pandas数据读写/output_data.json")
print(f"如： pd.read_json(\"pandas数据读写/output_data.json\") :{read_data} \n")

print("5.5.2-2)读JSON数据：json_normalize():"
      "json文件的数据不是表格形式，需要将字典结构的文件转换为列表形式，这个过程叫规范化(normalization)。"
      "pandas库的json_normalize()函数能够将字典或列表转换为表格。")
#1)加载json文件
file=open("pandas数据读写/01.json","r")
text=file.read()
text2=json.loads(text)
print(f"text=file.read() ,text : {text}")
print(f"text2=json.loads(text), text2 :\n {text2}\n")
# text3=pd.json_normalize(text2)
df1 = pd.json_normalize(text2) #pandas库的json_normalize()函数能够将字典或列表转换为表格
print(f"df1 = pd.json_normalize(text2), df1的内容 : \n{df1}\n")
data2 = [df1["main.temp"], df1["main.humidity"], df1["main.pressure"], df1["weather.description"],df1["wind.speed"], df1["wind.deg"], df1["dt"], df1["name"]]  #apply(datetime.datetime.strftime('%Y-%m-%d %H%M%S'))]   #strftime('%Y%m%d%H%M%S')   (datetime.datetime.fromtimestamp
data2_heading = ['temp', 'humidity', 'pressure', 'description', 'speed', 'deg', 'dt', 'name']
df_tran_data = pd.DataFrame(data2, index=data2_heading)

print(f"data2 = [df1[\"main.temp\"],df1[\"main.humidity\"], ...], 执行后data2的内容 :  \n{data2}")
print(f"data2_heading = ['temp', 'humidity', 'pressure', 'description', 'speed', 'deg', 'dt', 'name'], 执行后data2_heading的内容 : \n{data2_heading} \n ")
print(f"df_tran_data = pd.DataFrame(data2, index=data2_heading), 执行后df_tran_data的内容:df_tran_data : \n{df_tran_data} \n ")
import json
#from pandas.io.json import json_normalize
#pd.json_normalize()
print("5.5.2-读JSON数据：read_json()")

print("---【end】5.5-读写JSON数据 ----\n")

#---- 【end】5.5-读写JSON数据 ----#


#---- 【start】5.6-HDF5格式： ----#

print("5.6-HDF5格式")
print("HDF5（Hierarchical Data Format version 5）是一种用于存储和组织大规模科学数据的二进制文件格式，"
      "由美国国家超级计算中心开发，现由非营利组织HDF Group维护。")
print("python提供两种操纵HDF5格式数据的方法：PyTables和p5py。h5py为HDP5的高级API提供接口；"
      "PyTables分装了很多HDF5细节，提供更加灵活的数据容器、索引表、搜索功能和其他计算相关介质。"
      "python还有一个叫作HDFStore,类似dict的类,它用PyTables存储pandas对象。使用HDF5格式前，必须导入HDFStore类。")
from pandas.io.pytables import HDFStore
frame=pd.DataFrame(np.arange(16).reshape(4,4),columns=['up','down','left','right'],index=['white','black','red','blue'] )
print(f"frame: \n{frame}\n")
store=HDFStore('pandas数据读写/write_hdf5_06.h5')

store['obj1']=frame  #可以把多种数据结构存储到一个HDF5文件，如store变量表示这个文件
print(f"store['obj1=frame, store的内容：\n{store}\n")
print(f"store['obj1=frame, store['obj1']的内容：\n{store['obj1']}\n")

frame2=pd.DataFrame(np.arange(16).reshape(4,4),columns=['pen','pencil','ball','book'],index=['white','black','red','blue'] )
store['obj2']=frame2
print(f"store['obj1']=frame; store['obj2']=frame2, store的内容：\n{store}\n")
print(f"store['obj1']的内容：\n{store['obj1']}\n")
print(f"store['obj2']的内容：\n{store['obj2']}\n")

store.close()
print("5.6.1-HDF5格式")

#读刚生成的HDF5文件
store2=HDFStore('pandas数据读写/write_hdf5_06.h5','r')
print(f"读刚生成的HDF5文件store2=HDFStore('pandas数据读写/write_hdf5_06.h5','r') ，store2的信息:\n {store2} ")
print(f"store2['obj2']:\n {store2['obj2']}\n ")
store2.close()  #关闭打开的文件

#---- 【end】5.6-HDF5格式 ----#

#---- 【start】5.7-pickle-python对象序列化 ----#
print("5.7-pickle-python对象序列化")
print("一）用cPickle实现python对象序列化")
#cPickle是Python 2.x中的C语言实现模块，但在Python 3.x中已被合并到pickle模块中。Python 3.x默认使用_pickle（即pickle的C实现），但推荐直接使用pickle模块以保持兼容性
# import cPickle as pickle
import pickle
data ={'coloe':['red','blue','green'],'value':[5,6,7]}
pickled_data=pickle.dumps(data)
print(f" data :\n{data}")
print(f"pickled_data=pickle.dumps(data), pickled_data :\n{pickled_data}\n")

#loads()重建被序列化的对象（反序列化）
re_pickled_data=pickle.loads(pickled_data)
print(f"re_pickled_data=pickle.loads(pickled_data) re_pickled_data :\n{re_pickled_data} \n")

print("二）用pandas实现python对象序列化")
print("用pandas库实现对象序列化和反序列化很方便，有现成的工具，所有的操作都是隐式进行的，无需导入Pickle模块")
frame=pd.DataFrame(np.arange(16).reshape(4,4),columns=['up','down','left','right'],index=['white','black','red','blue'] )
frame.to_pickle("pandas数据读写/write_frame.pkl")
read_frame=pd.read_pickle("pandas数据读写/write_frame.pkl")
print(f"用pandas库实现对象序列化和反序列化很方便(frame.to_pickle();read_frame=pd.read_pickle() : {read_frame}")

#---- 【end】5.7-pickle-python对象序列化----#



#---- 【start】5.4-读写JSON数据 ----#
#---- 【end】5.4-读写JSON数据 ----#

