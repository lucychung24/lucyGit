#为图表添加更多元素
import matplotlib.pyplot as plt
import numpy as np

#The font properties of the legend. If None (default), the current matplotlib.rcParams will be used.
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'STFangsong']  # 设置支持中文的字体
# 解决负号显示问题
#plt.rcParams['axes.unicode_minus'] = False

plt.axis([0,5,0,20])
plt.title('title-图1',fontsize=20,fontweight='bold',fontname='SimHei') #fontname='SimHei'
plt.xlabel('Counting',color='gray')  #轴标签
plt.ylabel('Square values',color='gray')
#在图表任意位置添加文本：text(x,y,s,fontdict=none,**kwargs)函数
#x,y前两个参数为标签在图形中位置坐标，但每个标签的y值较相应的数据点的y值有一点偏差
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
#可在文本中添加LaTex表达式，这表达式内容置于两$符号之间， 通常需要在LaTex表达式的字符串前添加r字符
plt.text(1.1,12,r'$y=x^2$',fontsize=20,fontweight='bold',bbox={'facecolor':'yellow','alpha':0.2})  #alpha:透明度，值0到1之间，值越小越透明
#添加网格:grid()函数，传入参数True
plt.grid(True)
'''
#case-1:一个plot函数绘制单个序列
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#添加图例:legend()函数, 图例位置由loc关键字控制，loc取值0到10，0：最佳位置，1：右上角，2：左上角，3：右下角，4：左下角，5：右侧。。。
plt.legend(['First series'],loc=2) #loc='upper left'
'''

#case-2:多个plot函数绘制多个序列
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.7,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2,4,12],'b*')
#添加图例:legend()函数, 图例位置由loc关键字控制，loc取值0到10，0：最佳位置，1：右上角，2：左上角，3：右下角，4：左下角，5：右侧。。。
plt.legend(['First series','Second series','Third series'],loc=2) #loc='upper left'
plt.show()


