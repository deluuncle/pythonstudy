# 根据奖金的范围来划分提成
sale_money = input("请输入你这个月的奖金：")
try:
    sale_money = float(sale_money)
except:
    print("薪资应该是数字形式的")

if sale_money < 100000:
    bounce = sale_money*0.1
elif sale_money >= 100000 & sale_money <= 200000:
    bounce = 100000*0.1 + (sale_money-100000)*0.075
elif sale_money > 200000 & sale_money <= 400000:
    bounce = (sale_money - 200000)*0.05 + 200000*(0.1+ 0.075)
elif sale_money > 400000 & sale_money <= 600000:
    bounce = (sale_money - 600000)*0.015 + 100000*0.1 + 200000*0.05 +
    300000*0.05
else:
    bounce = (sale_money-1000000)*0.01+ 10

print("这个月的奖金是{}元".format(bounce))