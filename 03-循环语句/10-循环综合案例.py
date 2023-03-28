"""
某公司，账户余额1万元，给20名员工发工资
    员工编号从1到20，从编号1开始，依次领取工资，没人可领取1000
    领工资时，财务判断员工的绩效分(1-10)(随机生成)，如果低于5，不发工资，换下一位
    如果工资发完，结束发工资
"""
import random

total = 10000

for i in range(1, 21):
    num = random.randint(1, 10)

    if num < 5:
        print(f'员工{i}, 绩效分{num}, 不发工资， 下一位')
        continue
    else:
        total -= 1000
        print(f'向员工{i}发放工资1000元，账户余额还剩余{total}元')

    if total == 0:
        print('工资发完了，下个月领取吧')
        break

print('Done')
