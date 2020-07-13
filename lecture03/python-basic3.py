"""
    综合应用——石头剪刀布
"""

import random
while True:
    player = int(input("请输入您要出的拳 石头(1)/剪刀(2)/布(3):"))

    computer = random.randint(1, 3)

    print("玩家出的拳是 %d -- 电脑出的拳是 %d" % (player, computer))

    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):

        print("电脑弱爆了！")
        break
    # 平局
    elif player == computer:
        print("真是心有灵犀，再来一盘")
    # 电脑获胜
    else:
        print("不服气，决战到天亮！")