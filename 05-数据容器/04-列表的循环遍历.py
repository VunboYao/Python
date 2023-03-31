name_list = ['Emma', 'Anna', 'Duo', 'Ben', 'Juli']


# while方式遍历
def list_while_func():
    length = len(name_list)
    index = 0
    while index < length:
        print(f'list_while: {name_list[index]}')
        index += 1
    else:
        print(f'while方式遍历完成:{index}')


# for方式遍历
def list_for_func():
    for i in name_list:
        print(f'list_for: {i}')
    else:
        print(f'for方式遍历完成')


list_while_func()
list_for_func()
