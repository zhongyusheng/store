import random
count=0
i=2000
a=30
choose="是"
while True:
    if choose=="是":
        num = random.randint(0, 20000)
        while  a>=1:
            if i > 0 :
                data = input("请输入您要猜测的数字:")
                a=a-1
                data = int(data)
                if data>num:
                    print("大了！")
                    i=i-200
                    count=count+1
                elif data < num:
                    print("小了！")
                    i = i - 200
                    count = count + 1
                else:
                    print("恭喜您猜对了！幸运数字为：",num,"，本次共猜了",count,"次！")
                    i=i+3000
                    print("金币+3000")
                    print("您现在的金币为:",i)
                    choose = input("您是否选择继续游戏(请输入“是”或“否”)：")
                    if choose=="否":
                        break
                    elif choose=="是":
                        num = random.randint(0, 20000)
            else:
                charge = input("是否需要进行充值(请输入“是”或“否”)：")
                if charge == "是":
                    money = int(input("请输入充值金额："))
                    i = i + money
                else:
                    break
        print("下次再见！")
        break
    elif  choose=="否":
        break







