#【8.4K- Iirs数据集 和 降维，主成分分解-PCA:主成分分析法（Principal Component Analysis） 】
#降维，主成分分解-PCA  （3D图）
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import datasets
from sklearn.decomposition import PCA # 主成分分析法（Principal Component Analysis）
from mpl_toolkits.mplot3d import Axes3D #绘制3散点图，要用到matplotlit的mpl_toolkits.mplot3d 模块

iris = datasets.load_iris()  #iris数据集（鸢尾花卉数据集）
iris.data #iris.data，是一个包含150个元素的数组（150 x 4)，每个元素包含4个数值：分别为萼片和花瓣的的数据（长和宽）,eg.[5.1, 3.5, 1.4, 0.2]
iris.target #iris.target:是一个包含150个数据值，其中共有3种取值（0，1，2），分别代表3种不同花卉的鸢尾类别,
iris.target_names #访问iris.target_names属性了解每个值代表的花卉类别 , array(['setosa', 'versicolor', 'virginica'], dtype='<U10')


#case-1:萼片的长和宽
x = iris.data[:,0]  #萼片的长和宽, 取第1列
y=iris.data[:,1]    #萼片的宽, 取第2列
species=iris.target
x_min,x_max = x.min()-.5,x.max()+.5
y_min,y_max = y.min()-.5,y.max()+.5

#scatter
plt.figure()
plt.title("iris dataset - classfication by Sepal Sixes",fontweight='bold')
plt.scatter(x,y,c=species)
plt.xlabel('Sepal length',fontweight='bold')
plt.ylabel('Sepal width',fontweight='bold')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks()
plt.yticks()
plt.show()

#case-2:花瓣的长和宽
x = iris.data[:,2]  #花瓣的长和宽, 取第3列
y=iris.data[:,3]    #花瓣的宽, 取第4列
species=iris.target
x_min,x_max = x.min()-.5,x.max()+.5
y_min,y_max = y.min()-.5,y.max()+.5

#scatter
plt.figure()
plt.title("iris dataset - classfication by Petal Sixes",fontweight='bold')
plt.scatter(x,y,c=species)
plt.xlabel('Petal length',fontweight='bold')
plt.ylabel('Petal width',fontweight='bold')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks()
plt.yticks()
plt.show()


#case-3:主成分分解-PCA:主成分分析法（Principal Component Analysis）
x = iris.data[:,2]  #花瓣的长和宽, 取第3列
y=iris.data[:,3]    #花瓣的宽, 取第4列
species=iris.target

#PCA（）构造函数，用n_components选项指定要降到几维（主成分）
# 调用fit_transform()函数就是用来降维，如下面传入四维的Iris数据集作业参数
x_reduced=PCA(n_components=3).fit_transform(iris.data)

#scatter 3D
fig=plt.figure()
#ax=Axes3D(fig)  #ax=Axes3D(fig.add_subplot(111,projection=''))
ax = fig.add_subplot(111, projection='3d')

ax.set_title("Iris dataset - by CAP",fontweight='bold',size=14)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel('First eigenvector',fontweight='bold')
ax.set_ylabel('Second eigenvector',fontweight='bold')
ax.set_zlabel('Third eigenvector',fontweight='bold')
#ax.xaxis.set_ticklables(())
plt.show()



# iris数据集（鸢尾花卉数据集），其数据格式及数据：
# iris的data属性和target属性
# iris.data，是一个包含150个元素的数组（150 x 4)，每个元素包含4个数值：分别为萼片和花瓣的的数据（长和宽）,eg [5.1, 3.5, 1.4, 0.2]
# iris.target:是一个包含150个数据值，其中共有3种取值（0，1，2），分别代表3种不同花卉的鸢尾类别。 访问iris.target_names属性了解每个值代表的花卉类别
# >> iris = datasets.load_iris()
# >>> iris.data
# array([[5.1, 3.5, 1.4, 0.2],
#        [4.9, 3. , 1.4, 0.2],
# >>> iris.target
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
# >>> iris.target_names
# array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
# >>>
