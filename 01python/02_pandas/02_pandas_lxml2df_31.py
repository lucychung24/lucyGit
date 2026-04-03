'''
# lxml库的二级模块objectify :
lxml 是一个非常强大的库，用于处理 XML 和 HTML 数据。它提供了多种功能，包括解析、创建、修改、输出等。
lxml 的一个非常有用的特性是其 objectify 模块，它允许用户以面向对象的方式处理 XML 数据。

1、objectify使用：下面代码是：objectify 模块的一些使用示例
如：objectify,用parse()函数解析XML文件，并把树结构转换为DataFrame对象

pandas的所有I/O API函数中，没有专门处理XML格式的。Python有很多读写XML格式数据的库（除了pandas库）。
          其中一个库叫作lxml,他在处理大文件方面行能优异，因而从众多类库之中脱颖而出。"
      下面介绍用lxml处理XML文件，以及如何把它和pandas整合，最终从XML文件中获取到所需数据并将其转换为DataFrame。
从XML文件读数据:
1)lxml库的二级模块objectify,用parse()函数解析XML文件,返回树结构
2)把树结构转换为DataFrame对象

2、lxml库的etree模块使用：用parse()函数解析XML文件，并把树结构转换为DataFrame对象

'''


import pandas as pd
from lxml import objectify
import numpy as np

# -- 【start】lxml库的二级模块objectify,objectify 模块的一些使用示例--------#
def create_sample_xml():
    """创建示例XML文件"""
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
    <employees>
        <employee id="1">
            <name>张三</name>
            <age>28</age>
            <department>技术部</department>
            <salary>12000</salary>
        </employee>
        <employee id="2">
            <name>李四</name>
            <age>32</age>
            <department>销售部</department>
            <salary>10000</salary>
        </employee>
        <employee id="3">
            <name>王五</name>
            <age>25</age>
            <department>人事部</department>
            <salary>8000</salary>
        </employee>
    </employees>'''

    with open('employees.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)


def basic_objectify_example():
    """基础objectify使用示例"""
    print("=== 基础objectify使用示例 ===")

    # 解析XML文件
    with open('employees.xml', 'rb') as f:
        root = objectify.parse(f).getroot()

    # 访问根元素
    print(f"根元素: {root.tag}")

    # 遍历子元素
    for employee in root.employee:
        print(f"员工ID: {employee.get('id')}")
        print(f"姓名: {employee.name}")
        print(f"年龄: {employee.age}")
        print(f"部门: {employee.department}")
        print(f"薪资: {employee.salary}")
        print("-" * 20)


def convert_to_dataframe():
    """将objectify对象转换为DataFrame"""
    print("\n=== 转换为DataFrame示例 ===")

    # 解析XML
    with open('employees.xml', 'rb') as f:
        root = objectify.parse(f).getroot()

    # 提取数据
    data = []
    for employee in root.employee:
        row = {
            'id': int(employee.get('id')),
            'name': str(employee.name),
            'age': int(employee.age),
            'department': str(employee.department),
            'salary': float(employee.salary)
        }
        data.append(row)

    # 创建DataFrame
    df = pd.DataFrame(data)
    print(df)
    print(f"\n数据类型:\n{df.dtypes}")

    return df


def advanced_objectify_features():
    """高级objectify特性示例"""
    print("\n=== 高级objectify特性 ===")

    # 解析XML
    with open('employees.xml', 'rb') as f:
        root = objectify.parse(f).getroot()

    # 使用XPath查询
    print("技术部员工:")
    tech_employees = root.xpath('.//employee[department="技术部"]')
    for emp in tech_employees:
        print(f"  {emp.name}: {emp.salary}")

    # 访问特定索引的元素
    print(f"\n第一个员工: {root.employee[0].name}")

    # 获取属性值
    print(f"第二个员工ID: {root.employee[1].get('id')}")


def dataframe_operations(df):
    """DataFrame操作示例"""
    print("\n=== DataFrame操作示例 ===")

    # 数据统计
    print("薪资统计:")
    print(df['salary'].describe())

    # 按部门分组
    print("\n按部门分组平均薪资:")
    print(df.groupby('department')['salary'].mean())

    # 筛选数据
    print("\n薪资大于10000的员工:")
    high_salary = df[df['salary'] > 10000]
    print(high_salary[['name', 'salary']])

    # 排序
    print("\n按薪资排序:")
    print(df.sort_values('salary', ascending=False))


def handle_complex_xml():
    """处理复杂XML结构示例"""
    print("\n=== 复杂XML结构处理 ===")

    # 创建复杂XML
    complex_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <company>
        <name>科技有限公司</name>
        <departments>
            <department name="技术部">
                <manager>赵六</manager>
                <employees>
                    <employee id="1">
                        <name>张三</name>
                        <skills>
                            <skill>Python</skill>
                            <skill>Java</skill>
                        </skills>
                    </employee>
                </employees>
            </department>
            <department name="销售部">
                <manager>孙七</manager>
                <employees>
                    <employee id="2">
                        <name>李四</name>
                        <skills>
                            <skill>沟通</skill>
                            <skill>谈判</skill>
                        </skills>
                    </employee>
                </employees>
            </department>
        </departments>
    </company>'''

    with open('complex_company.xml', 'w', encoding='utf-8') as f:
        f.write(complex_xml)

    # 解析复杂XML
    with open('complex_company.xml', 'rb') as f:
        root = objectify.parse(f).getroot()

    # 提取嵌套数据
    data = []
    for dept in root.departments.department:
        dept_name = dept.get('name')
        manager = dept.manager
        for emp in dept.employees.employee:
            skills = [str(skill) for skill in emp.skills.skill]
            row = {
                'department': dept_name,
                'manager': str(manager),
                'employee_name': str(emp.name),
                'skills': ', '.join(skills)
            }
            data.append(row)

    df = pd.DataFrame(data)
    print(df)
# -- 【end】lxml库的二级模块objectify,objectify 模块的一些使用示例--------#

# -- 【start】lxml库的二级模块etree 模块,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象--------#
from lxml import etree
def etree_conver_to_dataframe():
    #with open('complex_company.xml', 'rb') as f:
    #    root = objectify.parse(f).getroot()

    tree = etree.parse('pandas数据读写/books.xml')
    root = tree.getroot()
    #print(f"-- 1)root : {root}")
    data = []
    for item in root.findall('book'):  # 假设XML(books.xml)中有多个<book>节点 book  (employees.xml文件XML中有多个<employee>节点 employee）
        row = {field.tag: field.text for field in item}
        data.append(row)

    df = pd.DataFrame(data)
    print(f"-- test function *********** df:\n {df}\n")

# -- 【start】lxml库的二级模块etree 模块,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象--------#
def main():
    """主函数"""
    print("\n=== lxml库的二级模块objectify,使用示例 ===")
    # 创建示例文件
    create_sample_xml()

    # 基础使用
    basic_objectify_example()

    # 转换为DataFrame
    df = convert_to_dataframe()

    # 高级特性
    advanced_objectify_features()

    # DataFrame操作
    dataframe_operations(df)

    # 复杂XML处理
    handle_complex_xml()

    print("\n=== lxml库的二级模块etree 模块,使用示例,用parse()函数解析XML文件，并把树结构转换为DataFrame对象 ===")
    #etree 模块,读xml文件数据转换为DataFrame
    etree_conver_to_dataframe()
    print("\n=== 教程完成 ===")


if __name__ == "__main__":
    main()
