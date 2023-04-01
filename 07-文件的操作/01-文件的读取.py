"""
文件的操作：
    - 打开文件
        - open(name, mode, encoding)
            - name: 文件的路径
            - mode: 只读(r)、写入(w)、追加(a)
            - encoding: utf-8,不能用位置参数，用关键字参数直接指定
    - 读写文件
        - read(num)
            - num表示要从文件中读取的数据的长度(字节), 如果没有传入num, 则表示读取文件中所有的数据
            - 返回的是一个str
        - readlines()
            - 按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
            - 返回一个list
        - readline()
            - 一次读取一行内容
            - 返回一个 str
        - for 循环读取文件行:
            - for line in open('xxx.txt', 'r')
            - line 为临时变量，记录了文件的一行数据
            - line 的数据类型是 str
    - 关闭文件
        - close()关闭文件对象，如果未关闭，则文件一直将被Python程序占用

    - with open() as f:
        - 通过 with open语法打开文件，可以自动关闭(无需显示调用close)
注意事项：
    - 可以只打开和关闭文件，不进行任何读写
"""

f = open('text.txt', 'r', encoding='utf-8')
# p = f.read(10)
# print(f'读取10个字节的数据:{p}')

# 在一个未关闭的文件读取操作中，将继续之前的读取获取数据
# p_all = f.read()
# print(f'读取所有的数据：{p_all}')

# r_lines = f.readlines()
# print(f'读取所有行数据, 返回一个list：{r_lines}')
# for line in r_lines:
#     # 移除首尾的空格与换行符
#     line = line.strip()
#     print(f'获取每一行的数据：{line}')

# r_line = f.readline()
# print(f'一次读取一行内容1：{r_line}')
# r_line = f.readline()
# print(f'一次读取一行内容2：{r_line}')

# for 循环读取文件行
for line in f:
    print(line, type(line))

f.close()

# with open 语法
# with open('text.txt', 'r', encoding='utf-8') as f:
#     # res = f.read()
#     res = f.readline()
#     # res = f.readlines()
#     print(f'with open读取文件：{res} => {type(res)}')
# 可以在操作完成后自动关闭close，避免遗忘掉close方法
