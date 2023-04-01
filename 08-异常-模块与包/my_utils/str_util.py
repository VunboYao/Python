# 字符串相关工具

def str_reverse(s):
    """
    接受传入字符串，将字符串反转返回
    :param s: 参数字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照下标x和y，对字符串进行切片
    :param s: 将被切片的字符串
    :param x: 切片的起始下标
    :param y: 切片的终点下标
    :return: 切片后的字符串
    """
    return s[x:y]


# 测试专用
if __name__ == '__main__':
    res = str_reverse('SB')
    print(res)

    res2 = substr('HelloWorld', 2, 6)
    print(res2)
