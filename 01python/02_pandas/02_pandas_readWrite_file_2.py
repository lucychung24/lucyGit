#pandas数据读写：I/O API工具：1）读写从csv和txt文件： read_csv()、read_table()、to_csv()
import numpy as np
import pandas as pd
#print(pd.__docformat__)
#print(pd.__version__)

print("5-Pandas数据读写")
csvframe=pd.read_csv('pandas数据读写/myCSV_01.csv')
#print(csvframe)

readtab=pd.read_table('pandas数据读写/myCSV_02_nohead.csv',sep=','
                      ,header=None,names=['white','red','blue','green','animal']) #使用name选项指定表头，直接把存有各列名称的数组赋给它
#print(readtab)
txtframe=pd.read_table('pandas数据读写/ch05_04.txt',sep=' ')  # 分隔符是空格
print("5.1-Pandas处理文件类型数据源的函数-读写从csv和txt文件: read_csv()、read_table()、to_csv()。\n"
      f" 举例：read_csv()： csvframe=pd.read_csv('pandas数据读写/myCSV_01.csv') ：{csvframe} \n"
      f" 举例：read_table：读csv文件: readtab=pd.read_table('pandas数据读写/myCSV_02_nohead.csv',sep=',',header=None,names=['white','red','blue','green','animal']"
      f"：\n{readtab} \n  "
      f"   #header选项:对于没表头情况，使用header选项，将其值置为空（header=None）， pandas会为其添加默认表头；\n"
      f"   #name选项:使用name选项指定表头，直接把存有各列名称的数组赋给它 \n")

print(f" 举例：read_table：读txt文件,分隔符是空格: txtframe=pd.read_table('pandas数据读写/ch05_04.txt',sep=' ') ：{txtframe} \n")

txtframe2=pd.read_table('pandas数据读写/ch05_04_1.txt',sep='\\s+')
print(f"RegExp解析txt文件：read_table函数支持使用正则表达式作为分隔符，通过sep参数实现。\n"
      f"1)典型应用场景\n"
      f"  多字符分隔符‌：sep='\\r\\t'处理回车+制表符分隔的文件。\n"
      f"  空白符分隔‌：sep='\\s+'处理任意空白符分隔的文件。\n"
      f"  ‌复杂模式‌：sep='[,;]+'处理逗号或分号分隔的文件。如 df = pd.read_table('data.txt', sep='[,;]+')\n"
      f" 2)注意事项\n"
      f"  正则表达式需用双反斜杠（如\\s+）转义。\n"
      f"  sep为None时，Pandas会自动检测分隔符。\n"
      f"  delim_whitespace=True等效于sep='\\s+' \n"
      f"  举例sep：指定分隔符，支持正则表达式（如\\s+表示一个或多个空白符）\n  "
      f"  如：txtframe2=pd.read_table('pandas数据读写/ch05_04_1.txt',sep='\\s+') ：{txtframe2} \n ")

readcsv2=pd.read_csv('pandas数据读写/myCSV_03.csv')
#print(readcsv2)
readcsv3=pd.read_csv('pandas数据读写/myCSV_03.csv',index_col=['color','status']) # 添加index_col选项，扩展read_csv()函数的功能，把所有想转换为索引的列名称赋给index_col
print("5.1.1-read_csv():添加index_col选项，扩展read_csv()函数的功能，把所有想转换为索引的列名称赋给index_col\n")
print("举例：新建一个csv文件，其中有两列将用作等级索引。 "
      "如：csv文件myCSV_03.csv 原始数据:")
print(f"{readcsv2}\n")



print(f"index_col选项，操作其中有两列将用作等级索引 pd.read_csv('pandas数据读写/myCSV_03.csv',index_col=['color','status']) 操作后: \n{readcsv3}\n ")

#mul_head_df=pd.read_table('pandas数据读写/ch05_06.txt')
mul_head_df=pd.read_table('pandas数据读写/ch05_06.txt',sep=',',skiprows=[0,1,3,6])
print("5.1.2-skiprow选项，可以排除多余的行，把排除的行的行号放到数组中，赋给该选项。 如要排除前5行，写为skiprows=5; 只排除第五行，写为skiprows=[];只排除指定行，如第1,2,5行，写为skiprows=[0,1,4] 把所有想转换为索引的列名称赋给index_col\n")
print(f"举例：文件有多行注释的，如文件 ch05_06.txt的内容：\n {pd.read_table('pandas数据读写/ch05_06.txt')}\n"
      f"   skiprows只排除指定行mul_head_df=pd.read_table('pandas数据读写/ch05_06.txt',sep=',',skiprows=[0,1,3,6]): \n{mul_head_df} \n")
#print(mul_head_df)
'''
myCSV_04_date.csv文件内容如下:
Study ID,CG_Arrival_Date/Time,Arrival_Date,Arrival_Time
2,1/1/2011 0:03,1/1/2011,0:03:00
3,1/1/2011 0:53,1/1/2011,0:53:00
'''


readcsv4=pd.read_csv('pandas数据读写/myCSV_04_date.csv')
df = pd.read_csv('pandas数据读写/myCSV_04_date.csv', parse_dates=[1, 2]) # parse_dates参数处理日期列，自动将字符串格式的日期转换为 datetime64[ns] 类型
print(f"5.1.3-parse_dates选项:read_csv 函数通过parse_dates参数处理日期列，自动将字符串格式的日期转换为 datetime64[ns] 类型"
      f"举例：1）没用parse_dates参数处理日期列：read_csv读取csv文件：readcsv4=pd.read_csv('pandas数据读写/myCSV_04_date.csv')，其内容及字段类型")
print(f"    readcsv4 内容:\n{readcsv4}")
print(f"    readcsv4 字段类型：\n {readcsv4.dtypes} \n")
print(f"举例：2）用parse_dates参数处理日期列：read_csv读取csv文件：df = pd.read_csv('pandas数据读写/myCSV_04_date.csv', parse_dates=[1, 2])，其内容及字段类型")
print(f"    df内容:\n {df}")
print(f"    df字段类型:\n{df.dtypes}\n"
      f"        *parse_dates参数处理日期列，自动将字符串格式的日期转换为 datetime64[ns] 类型")

filterRow_csvframe=pd.read_csv('pandas数据读写/myCSV_01.csv',skiprows=2,nrows=2)
print(f"5.1.4-从txt文件读取部分数据-nrows和skiprows选项：假如只想读取文件部分数据，可明确指定要解析的行号，这时用到nrows和skiprows选项。\n"
      f"  可以指定起始行n(n=skiprows)和从起始行往后读多少行(nrows=i) \n"
      f"  举例:pd.read_csv('pandas数据读写/myCSV_01.csv',skiprows=2,nrows=2) : \n{filterRow_csvframe}\n")

'''
ch05_01.csv文件内容：
    white  red  blue  green animal
0      1    5     2      3    cat
1      2    7     8      5    dog
2      3    3     6      7  horse
3      2    2     8      3   duck
4      4    4     2      1  mouse
'''
print("5.1.5-从txt文件读取部分数据-chunksize选项")
print("chunksize选项：chunksize 是 Pandas 中用于分块读取大文件的关键参数，通过将文件分割成多个小块逐块处理，有效避免内存溢出问题。"
      " \n 核心功能:"
      "\n   1)分块读取‌：指定每次读取的行数（如 chunksize=1000000 表示每次读取100万行）"
      "\n   2)返回类型‌：返回一个 TextFileReader 对象，该对象是一个生成器，支持迭代操作"
      "\n   3)适用场景‌：处理超大数据集（如亿级数据）时，避免一次性加载整个文件到内存")
print("  举例：从文件ch05_01.csv文件读数据，每个两行取一个累加起来最后把结果插入到Series对象中。 如 pieces=pd.read_csv('pandas数据读写/ch05_01.csv',chunksize=3) ，选项chunksize=3指定每次读取的行数 ")
out=pd.Series()
i=0
pieces=pd.read_csv('pandas数据读写/ch05_01.csv',chunksize=3)
for piece in pieces:
    out._set_value(i,piece['white'].sum())
    print(f"循环 i : {i}  ; "
          f"\n  piece['white']: \n {piece['white']} ;"
          f"\n  piece['white'].sum():\n {piece['white'].sum()} \n")
    i=i+1
    print(f"i=i+1 : {i}")
print(f"累加起来最后把结果插入out :\n {out}")
print(f"pieces: {pieces}")

frame2=pd.DataFrame(np.arange(16).reshape(4,4),columns=['ball','pen','pencil','paper'])
frame2.to_csv('pandas数据读写/write_ch05_07_1.csv')  # 索引和列名称连同数据一起写入
frame2.to_csv('pandas数据读写/write_ch05_07_2.csv',index=False,header=False)  #使用index=False,header=False 选项，取消默认写入索引和列名称
#print(frame2)
print("\n 5.2-往csv文件写数据")
print("5.2.1-to_csv(): 把DataFrame中的数据写入csv文件。写入过程中，要用到to_csv()函数，其参数为即将生成的文件名。"
      "\n  举例：把DataFrame对象 frame2， 写入文件"
      f"\n  对象frame2的元素：\n {frame2}"
      f"\n  写入文件1: frame2.to_csv('pandas数据读写/write_ch05_07_1.csv') , 索引和列名称连同数据一起写入\n"
      f"\n  写入文件2: frame2.to_csv('pandas数据读写/write_ch05_07_2.csv',index=False,header=False) #使用index=False,header=False 选项，取消默认写入索引和列名称:\n  "
      f"    *注意：数据结构中的NaN写入文件后，显示为空字段")



#print(f"{pd.read_csv('pandas数据读写/myCSV_03.csv',index_col=['color','status'])}")

