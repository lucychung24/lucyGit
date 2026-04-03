#数组数据文件的读写
import numpy as np
print(f"2.5-数组数据文件的读写\n ")
print(f"  数组数据文件的读写操作:\n "
      f"二进制文件操作：使用np.save/np.load实现高效数组存储与读取，文件扩展名自动处理。如save()参数有两个：要保存的文件名和要保存的数组，其中文件名的.npy扩展名系统会自动添加。\n "
      f"文本文件操作：np.savetxt/np.loadtxt支持自定义分隔符、格式化字符串和标题行。\n "
      f"多数组压缩文件：np.savez/np.load实现多个数组的打包存储，支持命名索引。\n "
      f"自定义格式保存：支持CSV格式输出，保留小数位数并添加表头\n "
      f"np.genfromtxt()函数可以从文本文件中读取数据并将其参入数组中。这函数接收3个参数：存放数据的文件名、用于分隔的字符、是否含有列标题。")


import numpy as np

# 二进制文件读写
def save_load_binary():
    arr = np.array([[1, 2], [3, 4]])
    np.save('output/binary_data.npy', arr)  # 保存二进制文件
    loaded_arr = np.load('output/binary_data.npy')  # 加载二进制文件
    return loaded_arr

# 文本文件读写
def save_load_text():
    data = np.array([[1.1, 2.2], [3.3, 4.4]])
    np.savetxt('output/text_data.txt', data, delimiter=',')  # 保存文本文件
    loaded_data = np.loadtxt('output/text_data.txt', delimiter=',')  # 加载文本文件
    return loaded_data

# 多数组压缩文件读写
def save_load_archive():
    np.savez('output/archive.npz', a=np.array([1, 2]), b=np.array([3, 4]))  # 保存多个数组
    archive = np.load('output/archive.npz')
    return archive['a'], archive['b']

# 自定义格式文本保存
def save_custom_format():
    data = np.array([[1, 2.5], [3, 4.7]])
    np.savetxt('output/custom_data.csv', data, delimiter=',', fmt='%.2f', header='Col1,Col2', comments='')
    return np.loadtxt('output/custom_data.csv', delimiter=',', skiprows=1)

def read_csv_file_2():
    data = np.genfromtxt('output/custom_data.csv', delimiter=',',names=True)
    return data

if __name__ == '__main__':
    print(f"二进制文件操作：使用np.save/np.load实现, 如自定义函数save_load_binary()使用np.save/np.load实现，返回内容：\n {save_load_binary()} \n")
    print( f"文本文件操作：np.savetxt/np.loadtxt支持自定义分隔符、格式化字符串和标题行, 如自定义函数save_load_text()，返回内容：\n {save_load_text()} \n")
    print( f"多数组压缩文件：np.savez/np.load实现多个数组的打包存储，支持命名索引, 如自定义函数save_load_archive()，返回内容：\n {save_load_archive()} \n")
    print(f"自定义格式保存：支持CSV格式输出，保留小数位数并添加表头, 如自定义函数save_custom_formatt()生成和读CSV格式文件，返回内容：\n {save_custom_format()} \n")
    print(f"np.genfromtxt()函数可以从文本文件中读取数据并将其参入数组中, 如自定义函数read_csv_file_2()，返回内容：\n {read_csv_file_2()} \n")
