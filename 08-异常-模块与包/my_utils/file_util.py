# 文件处理相关工具

def print_file_info(file_path):
    """
    根据传入文件的路径，打印文件的全部内容，文件不存在则捕获并输出提示信息，finally中关闭文件对象
    :param file_path: 文件路径
    :return: None
    """

    f = None
    try:
        f = open(file_path, 'r', encoding='UTF-8')
        content = f.read()
        print(f'文件中的内容是：{content}')
    except FileNotFoundError as e:
        print(f'文件名未找到错误：{e}')
    finally:
        if f:
            f.close()


def append_to_file(file_path, data):
    """
    接收文件路径以及传入数据，将数据追 加写入到文件中
    :param file_path: 文件路径
    :param data: 数据
    :return: None
    """
    with open(file_path, 'a') as f:
        f.write('\n')
        f.write(data)
        print('内部打印：数据追加写入成功')


# 测试专用
if __name__ == '__main__':
    print_file_info('../python.txt')
    append_to_file('../python.txt', 'I don\'t know say what')
