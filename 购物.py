money=input("请输入您的支付宝余额：")
money=int(money)
laoganma=1
lenovo=1
shop = [
    ["劳力士手表", 200000],
    ["Ipone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["HUA WEI WATCH", 1200],
    ["Mac PC", 15000],
    ["辣条", 2.5],
    ["老干妈", 13]
]

choose1=input("您是否需要抽取1张优惠券，如果输入‘是’将会随机抽取一张购物优惠券，如果输入‘否’将会正常购物  请输入：")
if choose1=="是":
    import random
    card=random.randint(0,29)
    if 0<=card and card<=9:
        laoganma=0.7
        print("\033[31m恭喜您获得老干妈7折优惠券一张\033[0m")
        print("\033[32m欢迎您进入购物界面：\033[0m")
        new1 = laoganma * shop[6][1]
        shop[6]= ["老干妈 折后价为：",new1]
    else:
        lenovo=0.1
        print("\033[31m恭喜您获得联想电脑1折优惠券一张\033[0m" )
        print("\033[32m欢迎您进入购物界面：\033[0m")
        new2 = lenovo * shop[2][1]
        shop[2]=["lenovo PC 折后价为：",new2]
else:
    shop=[
        ["劳力士手表",200000],
        ["Ipone 12X plus",12000],
        ["lenovo PC",6000],
        ["HUA WEI WATCH",1200],
        ["Mac PC",15000],
        ["辣条",2.5],
        ["老干妈",13]
    ]


mycard=[]
i=0
while i<20:
    for key,value in enumerate(shop):
        print(key,value)
    choose2=input("请输入您要选择的商品编号：")
    if choose2.isdigit():
       choose2=int(choose2)
       if choose2 >6:
           print("\033[31m您输入的商品不存在，别瞎弄!\033[0m")
       else:
           if money>=shop[choose2][1]:
               money=money-shop[choose2][1]
               print("\033[32m恭喜您购买商品成功！\033[0m")
               print("您现在的余额为：",money)
               mycard.append(shop[choose2])

           else:
               print("您的余额不足，请进行充值！")
    elif choose2=="q" or choose2=="Q":
        print("\033[32m欢迎下次光临\033[0m")
        break
    else :
        print("\033[31m输入有误，请重新输入！\033[0m")
    i=i+1
choose3=input("是否需要打印购物清单？")
if choose3=="是":
    print("您的购物清单如下：")
    for key,value in enumerate(mycard):
        print(key,value)
    print("您的余额为：",money)
    print("欢迎您下次光临！")
else:
    print("欢迎您下次光临！")
