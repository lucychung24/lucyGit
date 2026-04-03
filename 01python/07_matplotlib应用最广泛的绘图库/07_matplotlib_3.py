#处理多个Figure和Axes对像 ： #多个图形 plt.subplot + 设置支持中文
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STFangsong']  # 设置支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

#case-3:多个图形 plt.subplot -水平方向被分为几部分，如 第二个数字2，指2部分 ： pyplot命令要同时管理多个图形，subplot()函数可以将图形区分为不同的绘图区域，还能激活特定子图，以便用命令控制它
t3=np.arange(0.,1.,0.05)
y31=list(map(math.sin,2*math.pi*t3))
y32=list(map(math.cos,2*math.pi*t3))
plt.subplot(121)
#plt.plot(t3,y31,'b-.')
plt.title('my plot-图1',fontsize=20,fontweight='bold')
#plt.xlabel('x轴',fontsize=20,fontweight='bold',fontname='SimHei') #,fontsize=20,fontweight='bold',fontname='Times New Roman'
plt.xlabel('x轴',fontsize=20,fontweight='bold',fontname='SimHei')
plt.ylabel('y轴',fontsize=20,fontweight='bold',fontname='SimHei')
plt.plot(t3,y31,'b-.')
plt.subplot(122)
plt.plot(t3,y32,'r--',linewidth=4.0)
plt.show()


'''
#case-4:多个图形- subplot(211): 这生成的是概念图表，不并真存在的图表
#，因此这会存在新建的会覆盖之前存在的。若不要这覆盖之前，用 add_subplot() method or the axes() function 
#If you do not want this behavior, use the add_subplot() method or the axes() function instead.
# subplot(211)： produces a subaxes in a figure which represents the top plot
# (i.e. the first) in a 2 row by 1 column notional grid (no grid actually exists
# , but conceptually this is how the returned subplot has been positioned).
# Creating a subplot will delete any pre-existing subplot that overlaps with it beyond sharing a boundary

# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
plt.show()
'''

'''
import matplotlib.font_manager as font_manager
# 获取可用的字体列表并选择一个字体
font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
#print(font_list)  # 查看可用的字体列表

# 获取可用的字体列表并选择一个字体
font_list = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
print(font_list)  # 查看可用的字体列表

# 选择一个字体并设置它为默认的 sans-serif 字体
font_path = 'C:\\Users\\zhongdh\\AppData\\Local\\Microsoft\\Windows\\Fonts\\DejaVuSans.ttf'  # 替换为你的字体路径
prop = font_manager.FontProperties(fname=font_path)
prop.get_name()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [prop.get_name()]
'''
