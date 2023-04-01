"""
- 直接调用 write, 内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
- 当调用 flush 的时候，内容会真正写入文件
- 这样做是避免频繁的操作硬盘，导致效率下降

注意：
    - 文件如果不存在，使用 “w” 模式，会创建新文件
    - 文件如果存在，使用 “w” 模式，会将原有内容清空
    - close()方法，带有 flush() 方法的功能
"""

# 1.open file
f = open('python.txt', 'w')

# 2.execute writing
f.write('Hello World')

# 3.flush content
f.flush()
