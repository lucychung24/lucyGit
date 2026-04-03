#处理中文显示问题
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STFangsong']  # 设置支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

#处理中文显示问题
plt.rcParams['font.sans-serif'] =  ['SimHei']  # 黑体

#myname = raw_input("what is your name? ")
print ( "hi "+" myname "+", i'm glad to say: Hello world!")
'''
#case 1
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,3,6])
plt.title('pliot - demo 1')
plt.show()
'''

'''
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
import matplotlib
matplotlib.matplotlib_fname()  # 这将返回配置文件的路径
print('************************'+matplotlib.matplotlib_fname() )

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STFangsong']  # 设置支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

#处理中文显示问题
plt.rcParams['font.sans-serif'] =  ['SimHei']  # 黑体

import matplotlib.pyplot as plt
import numpy as np
import datetime


plt.figure()
plt.title('示例标题')
plt.show()
