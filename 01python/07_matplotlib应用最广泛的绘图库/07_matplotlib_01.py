#print('hello world!')
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

t=np.arange(0,2.5,0.1)



# plt.plot(x, y)

#不支持中文,处理
plt.rcParams['font.sans-serif']  = ['SimHei']  # 黑体
# plt.rcParams['font.family'] = 'SimHei'
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title('case-0-线图')
plt.show()

plt.axis([0,5,0,20])
plt.title('case-0-1-图-添加文本标、网格、图例',fontsize=20,fontweight='bold',loc='center')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
##text()函数的前两个参数为标签在图形中的位置的坐标. 可在图表中任何位置添加文本
plt.text(1.1,12,r'$y=x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
#添加网格
plt.grid(True) #grid()函数，传入参数True, 添加网格
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#添加图例legend(),loc='upper right', loc取值范围0-10，0-最佳位置，1-'upper right' 右上角；2-左上角。。。
plt.legend(['First series'],loc='upper right')
plt.show()
#text()函数的前两个参数为标签在图形中的位置的坐标. 可在图表中任何位置添加文本
#matplotlib整合了LaTex表达式,支持在图表中插入数学表达式.
# 将表达式内容置于两个$字符之间,可在文本中添加LaTex表达式,
# 解释器会将该符号之间的文本识别成LaTex表达式,把它们转为数学表达式、公式、数学符号或希腊字母等





#对于多行注释，可以使用三个连续的单引号（'''）或者三个连续的双引号（"""）来创建块注释
'''
# y1=map(math.sin,math.pi*t)  --> 将生成器中的数据收集到一个列表或 NumPy 数组中,即要转为一个列表或 NumPy 数组
# In [28]: type(y1)  #查看类型
# Out[28]: map

# In [32]: y1=list(map(math.sin,math.pi*t))  #如将生成器中的数据,转为一个列表
# In [33]: type(y1)  #查看类型
# Out[33]: list



# --》用这格式，传入y1做参数到matplotlib会报错误“RuntimeError: matplotlib does not support generators as input” 这类错误
#原因:错误通常是因为尝试将一个生成器（generator）直接用作绘图输入，而 Matplotlib 期望的是一个数组（array）或类似数组的结构。生成器在迭代时会逐个产生数据，这与 Matplotlib 需要的连续数据格式不兼容。
#将生成器中的数据收集到一个列表或 NumPy 数组中，然后再将这些数据传递给 Matplotlib。
#下面是一些解决步骤：
# 假设 gen 是你的生成器
gen = (x for x in range(10))  # 示例生成器
# 将生成器转换为列表
data_list = list(gen)

# 或者，如果你需要 NumPy 数组
data_array = np.array(list(gen))
'''
# y1=map(math.sin,math.pi*t)  --> 将生成器中的数据收集到一个列表或 NumPy 数组中
#将生成器中的数据收集到一个列表或 NumPy 数组中

'''
#import mathmath.sin(x) : 参数x：表示角度的数值或变量，以弧度为单位.
1) 弧度是平面角的度量单位，用符号“rad”表示。其核心定义是：‌长度等于半径的圆弧所对的圆心角为1弧度‌。这意味着，在一个半径为r的圆中，如果一段弧的长度l恰好等于r，那么这段弧所对的圆心角就是1弧度‌

2)弧度与角度的换算
弧度与角度（度）是两种不同的角度量单位，它们之间的换算关系基于一个关键等式：‌180° = π弧度,
  基于此，可以推导出以下换算公式：
     角度转弧度‌：角度数 × (π / 180)
     ‌弧度转角度‌：弧度数 × (180 / π)
     例如，90°转换为弧度是90 × (π / 180) = π/2弧度；而π/3弧度转换为角度是π/3 × (180 / π) = 60°‌
'''
t=np.arange(0,2.5,0.1)
y1=list(map(math.sin,math.pi*t))
y2=list(map(math.sin,math.pi*t+math.pi/2) )
y3=list(map(math.sin,math.pi*t-math.pi/2) )


#case-1: plt.plot - 点图   (import matplotlib.pyplot as plt) 
#下面的是点图显示
# plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys') #多个序列，写法1
#多个序列，写法2
plt.plot(t,y1,'b*')
plt.plot(t,y2,'g^')
plt.plot(t,y3,'ys')
plt.title('case-1-点图')
#添加图例legend(),loc='upper right', loc取值范围0-10，0-最佳位置，1-'upper right' 右上角；2-左上角。。。
#每个序列都要调用一次plot()函数，调用顺序跟传给legend()函数作为参数的文本标签顺序应保持一致
plt.legend(['First series','Second series','Third series'],loc=2)  #loc='upper right', loc取值范围0-10，1-'upper right'
plt.show()

#case-2: 线图
#下面的是线图显示
plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-')
plt.title('case-2-线图')
plt.show()

# #subplot() :函数的参数由三个整数组成  如subplot(1,1,1)  或 subplot(111)
#     第一个数字：决定图形沿垂直方向被分为几部分
#     第二个数字：决定图形沿水平方向被分为几部分
#     第三个数字：设定可以直接用命令控制的子图
#      i.e. ``fig.add_subplot(235)`` is the same as ``fig.add_subplot(2, 3, 5)``. Note that this can only be used if there are no more than 9 subplots.



#case-3:多个图形 plt.subplot -垂直方向被分为几部分，如 第一个数字2，指2部分 ： pyplot命令要同时管理多个图形，subplot()函数可以将图形区分为不同的绘图区域，还能激活特定子图，以便用命令控制它
plt.subplot(211)
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')
plt.title('case-3-多个图形 plt.subplot -垂直方向被分为几部分')
plt.show()


#matplotlib.use('TkAgg')
#plt.rcParams['font.sans-serif'] = ['SimHei']


# import matplotlib.font_manager as font_manager
# # 获取可用的字体列表并选择一个字体
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
# #print(font_list)  # 查看可用的字体列表
# 
# # 选择一个字体并设置它为默认的 sans-serif 字体
# font_path = 'C:\\Users\\zhongdh\\AppData\\Local\\Microsoft\\Windows\\Fonts\\DejaVuSans.ttf'  # 替换为你的字体路径
# prop = font_manager.FontProperties(fname=font_path)
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = [prop.get_name()]

# #指定字体文件的路径
# #matplotlib.font_manager._load_fontlist({'fontpaths': [r'C:\Windows\Fonts\DejaVuSans.ttf']})
# plt.rcParams['font.sans-serif'] = ['SimHei']  #SimHei  ; SimSun-ExtG


plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STFangsong']  # 设置支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

#case-3:多个图形 plt.subplot -水平方向被分为几部分，如 第二个数字2，指2部分 ： pyplot命令要同时管理多个图形，subplot()函数可以将图形区分为不同的绘图区域，还能激活特定子图，以便用命令控制它
t3=np.arange(0.,1.,0.05)
y31=list(map(math.sin,2*math.pi*t3))
y32=list(map(math.cos,2*math.pi*t3))
plt.subplot(121)
#plt.plot(t3,y31,'b-.')
plt.title('my plot-1')
#plt.xlabel('x轴',fontsize=20,fontweight='bold',fontname='SimHei') #,fontsize=20,fontweight='bold',fontname='Times New Roman'
plt.xlabel('x轴',fontsize=20,fontweight='bold')
plt.ylabel('y轴')
plt.plot(t3,y31,'b-.')
plt.subplot(122)
plt.plot(t3,y32,'r--')
plt.title('case-3:多个图形 plt.subplot -水平方向被分为几部分')
plt.show()






