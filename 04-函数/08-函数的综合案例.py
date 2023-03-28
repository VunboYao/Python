money = 5000000
name = input('Please input your name:')


def search():
    print('------------查询余额--------------')
    print(f'{name}, 你好，您的余额为: {money}')
    menu()


def menu():
    print("""
    查询余额\t【1】
    存款\t\t【2】
    取款\t\t【3】
    退出\t\t【4】
    """)

    func = int(input('Please select func:'))

    if func == 1:
        search()
    elif func == 2:
        save()
    elif func == 3:
        withdraw()
    else:
        return None


def withdraw():
    print('------------取款--------------')
    count = int(input('Please input your money: '))
    global money
    money -= count
    print(f'取款{count}元, 当前余额 {money}')
    menu()


def save():
    print('------------存款--------------')
    count = int(input('Please input your money: '))
    global money
    money += count
    print(f'存款{count}元，当前余额 {money}')
    menu()


search()
