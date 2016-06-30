'''
用户启动程序时先输入工资，打印商品列表
允许用户选择购买商品
允许用户不断的购买商品
购买时检测： 余额是否足够-如果足够-直接扣款
                      -如果不够-打印余额不足
允许用户主动退出程序--退出时打印已购商品列表
'''
'''
1.优化购物程序，购买时允许用户选择购买多少件
2.允许多用户登录，下次登录后，继续按上次的余额继续购买
3.允许用户查看之前的购买记录（记录显示商品购买时间）
4.商品列表分级展示，例如
第一层菜单
    1.家电类
    2.服装类
    3.数码类
    4.汽车类
    。。
    随便进入一个，比如车类，进入第2层
    1.car1 50000
    2.car2 60000
    ...
5.显示已购买商品时，如果有重复的商品，不打印多好，而是在一行展示
id    shop_name   num  shop_cost       total
1.      手机       1      6000
2.      鼠标       2       100

###  会用到文件，datatime模块，json
'''
#商品原列表
shop_list = [
    ('电脑',5000),
    ('鼠标',50),
    ('手机',6000),
    ('显示器',2000),
    ('显卡',5888),
    ('香烟',100),
    ('眼镜',70)
]
shop_car = []
#用户输入购买金额，并判断是否为数字
cost = input("请输入圈入金额：")
if not cost.isdigit() :
    exit("输入错误，请输入数字")
else:
    cost = int(cost)
print("商品列表".center(50,'-'))
for shop_list_for in enumerate(shop_list):
    shop_num_base = shop_list_for[0]
    shop_num = shop_num_base +1     #商品编号
    shop_name = shop_list_for[1][0] #商品名
    shop_cost = shop_list_for[1][1] #商品金额
    print(shop_num,'.',shop_name,shop_cost)
for i in range(99):
    user_num = input("请选择商品编号进行购买，Q=QUIT,C=CHECK: \n")
    if user_num.isdigit():
        user_num = int(user_num)-1
        if user_num < len(shop_list):
            if cost >= int(shop_list[user_num][1]):
                cost -= shop_list[user_num][1]
                shop_car.append(shop_list[user_num])
                print('购买成功，您的余额还剩余',cost)
            else:
                print("当前余额",cost,"\n余额不足，本次购买商品如下\n",shop_car)
                exit()
        else:
            print('该商品编号不存在')
    if user_num=="q":
        print("欢迎您下次再来\n",shop_car)
        exit()
    if user_num=="c":
        print("购物车列表".center(50,'-'),"\n")
        for check_car in shop_car:
            check_name = check_car[0]
            check_cost = check_car[1]
            print(check_name,"\t",check_cost,"\n")
        print("----------当前余额：",cost,"￥----------")