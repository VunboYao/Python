"""
- a 模式，文件不存在则会创建
- a 模式，文件存在，则会追加写入的文件
- 写入时可增加 "\n" 来写入换行符
"""

f = open('python.txt', 'a')

f.write('\nHello Python')

# f.flush()
f.close()
