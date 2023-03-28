for i in range(1, 10):
    for j in range(1, i + 1):
        # \t 制表符，保证每一行对其
        # end="", 打印不换行
        print(f'{j} * {i} = {j * i}\t', end="")
    print()
else:
    print('All OK')