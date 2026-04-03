#NumPy是练习，学习常用操作 - 数组创建的有几种方法：
# array()函数，arange()函数，linspace()，zeros()，ones()
# numpy.andom模块的random() 如np.random.random((3,4))
'''
NumPy是Python中用于科学计算的基础包，主要提供以下核心功能：
主要用途‌
创建和操作‌多维数组‌（ndarray），这是NumPy的核心数据结构
执行高性能的‌数值计算‌，比Python原生列表运算速度快得多
作为其他数据处理库（如Pandas、SciPy）的基础依赖

NumPy
ndarray(N-dimensional array,N维数据组)对象

NumPy数组的另一个特点是大小固定，也就是说，创建数组时一旦指定好大小，就不会发生变化。这与python的列表有所不同，列表的大小是可以改变的。
'''

import numpy as np
#1-数组创建的有几种方法- 方法1：使用array()函数，参数为单层或嵌套列表
print(f"1-数组创建的有几种方法- 方法1：使用array()函数，参数为单层或嵌套列表")
#a=np.array([1,2,3])
a=np.array([[[1,1,1,1,5.1],[2,2,3,4,5],[3,3,3,3,8.5]],[[4,4,4,4,5.1],[5,5,5,4,5],[6,6,6,7,8.5]],[[7,7,7,4,5.1],[8,8,8,4,5],[9,9,9,7,8.5]],[[2,2,4,4,5.1],[5,5,5,4,5],[6,6,6,7,8.5]]])
#a=np.array([[1,2,3,4,5.1],[2,2,3,4,5],[3,3,6,7,8.5]])
print(f"数组变量a，a的元素,如 a：\n {a}")
type(a)
print(f"1.1）检查创建的对象是否是ndarray,把新声明的变量传给type()函数即可，如 type(a) 返回结果是: {type(a)}")
print(f"1.2）调用变量的dtype属性,查数据类型，如 a.dtype 返回结果是: {a.dtype}")
print(f"1.2）调用变量的ndim属性,轴数量，如 a.ndim 返回结果是: {a.ndim}")
print(f"1.2）调用变量的size属性,查数组长度，如 a.size 返回结果是: {a.size}")
print(f"1.2）调用变量的shape属性,查数组的型，如 a.shape 返回结果是: {a.shape}")
print(f"1.2）调用变量的itemsize属性,它定义了数组中每个元素的长度为几个字节，如 a.itemsize 返回结果是: {a.itemsize}")
print(f"1.2）调用变量的data属性,表示包含数组实际元素的缓冲区，如 a.data 返回结果是: {a.data}")

f=np.array([[1,2,3],[4,5,6]],dtype=complex)  #float
print(f"1.3）dtype选项，可以用dtype选项作为array()函数的参数，明确指定dtype的类型，"
      f"如 f=np.array([[1,2,3],[4,5,6]],dtype=complex) , f 返回结果是:\n {f}")


print(f"2-数组创建的有几种方法- 方法2：自带的数组创建方法")
b=np.zeros((2,3))
print(f"2.1）自带的数组创建方法zeros()函数,生成由shape参数指定维度信息，元素均为0的数组,如 b=np.zeros((2,3)), b返回结果是:\n {b}")
print(f"2.1）自带的数组创建方法ones()函数,生成由shape参数指定维度信息，元素均为1的数组,如 np.ones((2,3)), 返回结果是:\n {np.ones((2,3))}")
print(f"2.1）自带的数组创建方法arange()函数,根据传入参数，按照特定规则，生成包含一个数值序列的数组。\n "
      f"如生成一个包含0到9的数组，只需传入标识序列结束的数字作为参数即可，如 np.arange(10)或np.arange(0,10), 返回结果是:\n {np.arange(10)}"
      f"\n如不想以0作为起始值，可自己指定，这需要使用两个参数，第一个为起始值，第二个为结束值，如 np.arange(4,10), 返回结果是:\n {np.arange(4,10)}"
      f"\n还可生成等间隔的序列，如果为arange()函数指定了第三个参数，它表示序列中相邻两个值之间的差距，第三个参数可用是浮点型，如 np.arange(0,12,3), 返回结果是:\n {np.arange(0,12,3)} "
      f"\n第三个参数可用是浮点型，如 np.arange(0,6,0.6), 返回结果是:\n {np.arange(0,6,0.6)} ")
#使用arange()函数但要结合reshape()函数 生成二维数组
#c=np.arange(0,12).reshape(3,4)
print(f"2.3）上面创建的数组都是一维数组，如果要生成二维数组，仍然可使用arange()函数但要结合reshape()函数,如 c=np.arange(1,12).reshape(3,4), 返回结果是:\n {np.arange(0,12).reshape(3,4)}")

print(f"2.4）自带的数组创建方法linspace(),跟arange()函数很相似，前两个参数指定起始值和结束值，第三个参数：指定想把开头和结尾两个数字所指定的范围分成几部分"
      f"\n 如 np.linspace(0,10,5), 返回结果是:\n {np.linspace(0,10,5)}"
      f"\n 如 np.linspace(0,13,5), 返回结果是:\n {np.linspace(0,13,5)}")
#np.linspace()
e=np.random.random((3,4))
#print(e)
print(f"2.5）自带的数组创建方法numpy.andom模块的random(),使用随机数填充数组，只需把数组的大小作为参数传递给它，如 np.random.random((3,4)), 返回结果是:\n {e}")












'''
字符串前面的 f 是‌格式化字符串字面量‌（f-string）的标识符, 让在字符串中直接嵌入变量或表达式.
在引号前加 f 或 F,用 {} 在字符串中插入变量Python会在运行时自动计算并替换为实际值.
'''

'''


#case-1: 获取和处理网页数据 - 方法1）使用 Requests库
#使用Python和requests库，用户可向OpenWeatherMap API发送请求，获取特定城市的天气数据。通过状态码判断请求是否成功
import requests
api_key='a97e33dfce7cb8921e178c7339c631c7'
city='London,uk'
#url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key
url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
print(f"url ： {url}")
response=requests.get(url) #发送GET请求并获取响应
print(f"1）get url 返回的结果response 内容，如下: \n  {response.text}\n")
if response.status_code==200:
    # 在此处处理响应数据
    weather_data=response.json()
    print(f"2）读取URL返回的json数据（weather_data=response.json()） -1 weather_data：\n {weather_data}")
    print(f"3）读取URL返回的json数据 -如 weather：\n  {weather_data['weather'][0]['description']}")
    print(f"4）读取URL返回的json数据 -如 main：\n  {weather_data['main']}")
    print(f"5）读取URL返回的json数据 -如 main里面的temp：\n  {weather_data['main']['temp']}")
    #print(weather_data)
else:
    print(f"请求失败，状态码为{response.status_code}")




#case-2: 获取和处理网页数据 - 方法2）使用 urllib库
from urllib import request
api_key='a97e33dfce7cb8921e178c7339c631c7'
city='London,uk'
#url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key
url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
print(f"url ： {url}")
response=request.urlopen(url) #发送GET请求并获取响应
content = response.read().decode('utf-8')  # 需要手动解码
print(f"1）get url 返回的结果response/content 内容，如下: \n  {content}")
content=json.loads(content)
print(f"2）读取URL返回的json数据 -如 main：\n  {content['main']}")
print(f"3）读取URL返回的json数据 -如 main里面的temp：\n  {content['main']['temp']}")
#print(content['main'])


'''
'''
NumPy是Python中用于科学计算的基础包，主要提供以下核心功能：

主要用途‌

创建和操作‌多维数组‌（ndarray），这是NumPy的核心数据结构
执行高性能的‌数值计算‌，比Python原生列表运算速度快得多
作为其他数据处理库（如Pandas、SciPy）的基础依赖

关键功能‌

高效的数组运算‌ - 支持向量化操作，避免使用循环
广播机制‌ - 让不同形状的数组能够进行数学运算
线性代数计算‌ - 矩阵乘法、求逆、特征值分解等
数学函数库‌ - 包含三角函数、统计函数、傅里叶变换等

应用场景‌

数据分析与处理
机器学习模型开发
图像处理和计算机视觉
科学计算和工程建模

学习建议‌：如果你刚开始接触数据分析，建议先掌握NumPy数组的基本创建和操作，这是后续学习Pandas等库的重要基础。
'''
'''
NumPy提供了大量实用的函数，主要可以分为以下几类：

📊 数组创建函数‌

np.array()：从列表/元组创建数组
np.arange()：生成等差序列
np.linspace()：生成等间隔数
np.zeros() / np.ones()：创建全0或全1数组
np.eye()：创建单位矩阵

🧮 数学运算函数‌

四则运算：np.add(), np.subtract(), np.multiply(), `np.divide()
三角函数：np.sin(), np.cos(), np.tan()
对数函数：np.log(), np.log10()
取整函数：np.floor(), np.ceil()

📈 统计函数‌

np.sum()：数组元素总和
np.mean()：平均值
np.median()：中位数
np.std()：标准差
np.var()：方差

🔍 查找和排序函数‌

np.argmax() / np.argmin()：最大/最小值索引
np.sort()：数组排序
np.unique()：返回唯一值

💡 实用建议‌：如果你刚开始学习，建议先从np.array()、np.arange()、np.sum()、np.mean()这几个最基础的函数开始练习。
'''


