import random
guess = random.randint(1,101)

i = 1
while True:
    print("第%d次猜，请输入一个完整数字："%(i))
    try:
        temp = int(input())
        i += 1
    except ValueError:
        print("无效的数字")
        continue
    if temp==guess:
        print("恭喜你猜想正确，就是这个数字",guess)
        break
    elif temp>guess:
        print("大了")
    elif temp<guess:
        print("小了")

    