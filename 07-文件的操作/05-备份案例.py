"""
- 读取文件
- 将文件写出到bill.txt.bak文件作为备份
- 同时，将文件内标记为测试的数据行丢弃
"""

# 1.读取文件
r = open('bill.txt', 'r', encoding='utf-8')

# 2.开启写入文件 => 此处的写入模式，“w" 为每次写入时会清空文件中之前的数据
w = open('bill.backup.txt', 'w', encoding='utf-8')

# 3.读取每一行文件
for r_line in r:
    # 3.1去除空格、换行符，并分割
    line = r_line.strip().split(',')
    if line[-1] == '正式':
        # 3.2数据写入
        w.write(f'{line}\n')

# 4.close文件操作
r.close()
w.close()
