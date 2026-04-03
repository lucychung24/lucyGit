#对接数据库
import numpy as np
import pandas as pd
print("5.10-对接数据库:\n"
      "pandas.io.sql模块提供独立于数据库叫作sqlalchmy的统一接口，简化连接模式。\n"
      "create_engine 是 SQLAlchemy 模块下的函数，用于创建数据库连接引擎，支持多种数据库（如 Oracle、MySQL、PostgreSQL）。\n"
      "create_engine 属于 SQLAlchemy 模块，而非 Pandas。Pandas 通过 SQLAlchemy 连接数据库\n")
print("5.10.1-Python内置的SQLite数据库sqlite3.SQLite3工具实现了简单、轻量级的DBMS SQL")
print("举例1：读写-SQLite数据库sqlite3的表数据 ：\n"
      "1)创建SQLite数据库引擎:engine=create_engine('sqlite:///foo.db') \n"
      "2)把dataframe转换为数据库表:frame.to_sql('colors',engine,if_exists='replace',index=False)\n"
      "3)读取数据库,使用read_sql()函数，参数为表名和engine实例:tab_data=pd.read_sql('colors',engine)\n")
#‌导入SQLAlchemy‌：在代码开头添加导入语句：
from sqlalchemy import create_engine

frame =pd.DataFrame(np.arange(20).reshape(4,5),columns=['white','red','blue','black','green'])
print(frame)

#Python内置的SQLite数据库sqlite3.SQLite3工具实现了简单、轻量级的DBMS SQL.
#‌导入SQLAlchemy‌：在代码开头添加导入语句：
from sqlalchemy import create_engine
# 创建SQLite数据库引擎
engine=create_engine('sqlite:///foo.db')

# pandas.to_sql 是 Pandas 中用于将 DataFrame 数据写入 SQL 数据库的核心函数，支持多种数据库（如 MySQL、PostgreSQL、SQLite、Oracle 等）。
# to_sql 是 Pandas 与 SQL 数据库交互的桥梁，通过 SQLAlchemy 引擎实现高效数据传输。结合 chunksize 和 dtype 参数可显著提升大数据量写入性能。
#把dataframe转换为数据库表
frame.to_sql('colors',engine,if_exists='replace',index=False)

#读取数据库,使用read_sql()函数，参数为表名和engine实例
tab_data=pd.read_sql('colors',engine)
print(f"tab_data: \n{tab_data}\n")

print("举例2:数据库sqlite3 ：连接数据库，创建表，插入数据engine=create_engine('sqlite:///foo.db') ")
import sqlite3
#You can use ":memory:" to open a database connection to a database that resides in RAM instead of on disk.
con=sqlite3.connect(":memory:")

'''
#举例：删除表和建表
print("1-删除表")
#1-删除表
drop_tab_sql="""drop table test ;"""
con.execute(drop_tab_sql)
'''

print("2-创建表test")
#2-创建表
create_tab_query="""
create table test (a varchar(20),b varchar(20),c real,d integer);
"""
con=sqlite3.connect(":memory:")
con.execute(create_tab_query)
con.commit()


#create table test (a varchar(20),b varchar(20),c real,d integer))
#3-使用SQL INSERT语句插入数据到数据库表中
print("3-使用SQL INSERT语句插入数据到数据库表test中")
data=[['white','up',1,2],['blue','down',2,8],['green','up',4,4],['red','down',5,5]]
print (f"data:\n {data}")
stmt="insert into test values (?,?,?,?)"
con.executemany(stmt,data) #执行插入sql
con.commit()

# execute() 用于执行单条 SQL 语句，支持参数化查询，防止 SQL 注入。
# sql‌：SQL 语句（字符串或预编译对象）
# params‌：参数字典或元组（可选）
# many‌：是否执行多条语句（默认 False）
#
# xecutemany() 用于批量执行相同 SQL 语句，显著提高插入性能。其核心参数包括：
# sql‌：SQL 语句（字符串或预编译对象）
# data‌：参数列表（元组或字典）
# batcherrors‌：是否捕获批量错误（可选）


#4-查询刚插入数据库表的数据
print("4-查询刚插入数据库表的数据:")
cursor=con.execute("select * from test")
rows=cursor.fetchall()

print(f"cursor=con.execute(\"select * from test\") ,cursor : {cursor}")
print(f"rows=cursor.fetchall() ,rows : {rows}\n")

#可以用pd.read_sql_query() 查表数据
#pd.read_sql_query() :Read SQL query into a DataFrame
sel_data=pd.read_sql_query("select * from test",con) #Read SQL query into a DataFrame
print(f"可以用pd.read_sql_query() 查表数据："
      f"如sel_data=pd.read_sql_query(\"select * from test(\",con)"
      f" sel_data的数据:\n{sel_data}\n")

print("5-把元组列表rows数据传给DataFrame的构造函数，如需要列名称，可以用游标的description属性获取")
cursor.description
col_name=[]
for col_desc in cursor.description:
    col_name.append(col_desc[0])
    print(col_desc)
print (f"col_name : {col_name}")
# tran_df_data=pd.DataFrame(rows,columns=zip(*cursor.description)[0])  #报错TypeError: 'zip' object is not subscriptable
tran_df_data=pd.DataFrame(rows,columns=col_name)
print(f"列名称，可以用游标的description属性获取:执行cursor.description :\n {cursor.description} \n")
print(f"元组列表rows数据传给DataFrame的构造函数,执行tran_df_data=pd.DataFrame(rows,columns=col_name)，) "
       f"\n tran_df_data:\n {tran_df_data}\n")
con.close()

print( " ****************************************************************************")



#import sys
# print("python版本信息："+sys.version)  #python版本信息

print("5.10.2-Python连接oracle数据库")
#对接oracle数据库：
# 1）安装oracle的客户端（•	oracle-instantclient-basic-<version>-<platform>.zip 和•	oracle-instantclient-sdk-<version>-<platform>.zip）
#  并配置oracle环境变量path
# 2) 安装cx_Oracle ：安装命令如 conda install cx_Oracle

print("连接oracle数据库：需要1）安装oracle的客户端，并配置环境变量path；2）安装cx_Oracle ：安装命令如 conda install cx_Oracle \n")
print("一）create_engine, pandas.read_sql 是 Pandas 中用于从 SQL 数据库读取数据的核心函数，支持直接将 SQL 查询或数据库表转换为 DataFram")
print("create_engine 是 SQLAlchemy 的核心函数，用于创建数据库引擎，支持多种数据库（如 Oracle、MySQL、PostgreSQL）")
import cx_Oracle
# 创建数据库连接引擎
ora_engine=create_engine('oracle://scott:scott@192.168.60.130:1521/orcl')
orl_data=pd.read_sql('select * from  DEPT d ',ora_engine)
print(f"tab_data: \n{orl_data}\n")

#参数化查询
sql="SELECT * FROM emp e WHERE e.SAL >:min_sal"
params = {'min_sal': 2500}
orl_data_df2 = pd.read_sql(sql, ora_engine, params=params)
print(f"orl_data_df2 (SELECT * FROM emp e WHERE e.SAL >:min_sal): \n{orl_data_df2}\n")

# 分块读取大数据集‌
i=1
print("分块读取大数据集‌-start")
print("1)chunksize=5 -【for chunk in pd.read_sql('SELECT * FROM emp', ora_engine, chunksize=5)】")
chunk_size=10 #每块数据量 如10
for chunk in pd.read_sql('SELECT * FROM emp', ora_engine, chunksize=chunk_size):
    # process(chunk)
    print(f"process loop-{i}:  chunk:\n {chunk}")

    # 示例：计算每块数据的平均值
    avg_value = chunk['sal'].mean()
    print(f"计算每块数据的sal平均值Average: {avg_value}\n")

    i=i+1
print("分块读取大数据集‌-end")

print("解析日期列‌-start")
data3=pd.read_sql('SELECT * FROM emp e WHERE e.sal  >2500',ora_engine,parse_dates=['hiredate'])
print(f"data3 : {data3}")
print("解析日期列‌-end")
print("----------**********************_______________")

'''
print("2)chunk_size = 5  # 每块数据量 -【for chunk in pd.read_sql(query, ora_engine, chunksize=chunk_size)】")

import pandas as pd
from sqlalchemy import create_engine

# 创建数据库连接引擎
# ora_engine=create_engine('oracle://scott:scott@192.168.60.130:1521/orcl')

# 执行分块读取
chunk_size = 5  # 每块数据量
query = "SELECT * FROM emp"

for chunk in pd.read_sql(query, ora_engine, chunksize=chunk_size):
    # 处理每块数据
    print(f"Processing {len(chunk)} rows")
    # 示例：计算每块数据的平均值
    avg_value = chunk['sal'].mean()
    print(f"Average: {avg_value}")
'''
# print("分块读取大数据集‌-end")


# print("连接oracle数据库：需要1）安装oracle的客户端，并配置环境变量path；2）安装cx_Oracle ：安装命令如 conda install cx_Oracle \n")
# print("cx_Oracle 的版本："+cx_Oracle.__version__)
print("二）cx_Oracle.makedsn() ,cx_Oracle.connect(): cx_Oracle.makedsn 用于创建 Oracle 数据库的连接字符串（DSN），支持多种连接方式")
print("举例：连接oracle数据库（'192.168.60.130''orcl' user='scott）查表 select * from  DEPT的数据 \n")
import cx_Oracle

# 数据库连接字符串格式：'username/password@hostname:port/service_name'
#cx_Oracle.makedsn 用于创建 Oracle 数据库的连接字符串（DSN），支持多种连接方式
dsn = cx_Oracle.makedsn('192.168.60.130', '1521', service_name='orcl')
connection = cx_Oracle.connect(user='scott', password='scott', dsn=dsn)

# 创建一个cursor对象
cursor = connection.cursor()

# 执行查询
cursor.execute("SELECT * FROM DEPT")

# 获取查询结果
for result in cursor:
    print(result)

# 关闭cursor和connection
cursor.close()
connection.close()

'''
5.9.4.	连接其他数据库

对接数据库:
pandas.io.sql模块提供独立于数据库叫作sqlalchmy的统一接口，简化连接模式。
create_engine 是 SQLAlchemy 模块下的函数，用于创建数据库连接引擎，支持多种数据库（如 Oracle、MySQL、PostgreSQL）。
create_engine 属于 SQLAlchemy 模块，而非 Pandas。Pandas 通过 SQLAlchemy 连接数据库.

#postgresql,如下
create_engine('postgresql://sott:tiger@localhost:5432/mydatabase')
#mysql,如下
create_engine('mysql+pymysql://sott:tiger@localhost/mydatabase')
#mssql,如下
create_engine('mssql+pymysql://sott:')
#oracle,如下
create_engine('oraclql://sott:tiger@localhost/sidname')
'''
