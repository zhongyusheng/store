
def goshoping() :
    money = input("请输入您的支付宝余额：")
    money = int(money)
    laoganma = 1
    lenovo = 1
    shop = [
        ["劳力士手表", 200000],
        ["Ipone 12X plus", 12000],
        ["lenovo PC", 6000],
        ["HUA WEI WATCH", 1200],
        ["Mac PC", 15000],
        ["辣条", 2.5],
        ["老干妈", 13]
    ]

    choose1 = input("您是否需要抽取1张优惠券，如果输入‘是’将会随机抽取一张购物优惠券，如果输入‘否’将会正常购物  请输入：")
    if choose1 == "是":
        import random
        card = random.randint(0, 29)
        if 0 <= card and card <= 9:
            laoganma = 0.7
            print("\033[31m恭喜您获得老干妈7折优惠券一张\033[0m")
            print("\033[32m欢迎您进入购物界面：\033[0m")
            new1 = laoganma * shop[6][1]
            shop[6] = ["老干妈 折后价为：", new1]
        else:
            lenovo = 0.1
            print("\033[31m恭喜您获得联想电脑1折优惠券一张\033[0m")
            print("\033[32m欢迎您进入购物界面：\033[0m")
            new2 = lenovo * shop[2][1]
            shop[2] = ["lenovo PC 折后价为：", new2]
    elif choose1=="是":
        shop = [
            ["劳力士手表", 200000],
            ["Ipone 12X plus", 12000],
            ["lenovo PC", 6000],
            ["HUA WEI WATCH", 1200],
            ["Mac PC", 15000],
            ["辣条", 2.5],
            ["老干妈", 13]
        ]
    else:
        print("别瞎弄!请输入正确字符！您的折扣券飞了！！")

    mycard = []
    i = 0
    while i < 20:
        for key, value in enumerate(shop):
            print(key, value)
        choose2 = input("请输入您要选择的商品编号：")
        if choose2.isdigit():
            choose2 = int(choose2)
            if choose2 > 6:
                print("\033[31m您输入的商品不存在，别瞎弄!\033[0m")
            else:
                if money >= shop[choose2][1]:
                    money = money - shop[choose2][1]
                    print("\033[32m恭喜您购买商品成功！\033[0m")
                    print("您现在的余额为：", money)
                    mycard.append(shop[choose2])

                else:
                    print("您的余额不足，请进行充值！")
        elif choose2 == "q" or choose2 == "Q":
            print("\033[32m欢迎下次光临\033[0m")
            break
        else:
            print("\033[31m输入有误，请重新输入！\033[0m")
        i = i + 1
    choose3 = input("是否需要打印购物清单？")
    if choose3 == "是":
        print("您的购物清单如下：")
        for key, value in enumerate(mycard):
            print(key, value)
        print("您的余额为：", money)
        print("欢迎您下次光临！")
    else:
        print("欢迎您下次光临！")
    return

def shopping() :
    choose4=input("是否购买土特产？")
    if choose4=="是":
        goshoping()
    elif choose4=="否":
        print("好嘞！拜拜！")
    else:
        print("别瞎弄！重输！")

data={
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库","沙河水库"],
            "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学"],
            "天通苑":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"],
            "景区":["北京植物园","香山公园","玉渊潭公园"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡景区"]
        }
    },
    "四川":{
        "成都":{
            "高升桥":["锦里古街","成都武侯祠"],
            "成华区":["成都大熊猫繁育研究基地","升仙湖","多宝寺公园"],
            "都江堰市":["都江堰景区","青城山景区","青城后山"],
            "青龙":["成都动物园","昭觉寺"],
            "东大街":["春熙路"],
            "人民中路":["天府广场","成都博物馆"],
            "天府新区":["黄龙溪","成都海昌极地海洋公园","南湖公园"],
            "龙泉驿区":["洛带古镇","龙泉山风景区","蔚然花海","龙泉山城市森林公园"]
        }
    }
}
def print_place(choice):
    for i in choice:
        print(i)

for i in data:
    print(i)
city1=input("请输入您要去的地区：")
while True:
    if city1 in data:
        print_place(data[city1])
        city2=input("请输入二级地区：")
        if city2 in data[city1]:
            choose5=input("您是选择进入商场？还是浏览下级地区景点？进入商城请输入1，浏览下级地区请输入2：")
            choose5 = int(choose5)
            if choose5==1:
                shopping()
                break
            elif choose5==2:
                print_place(data[city1][city2])
                city3=input("请输入三级地区：")
                if city3 in data[city1][city2]:
                    print_place(data[city1][city2][city3])
                    shopping()
                elif city3 == "q" or city3 == "Q":
                    print("欢迎下次使用本系统！")
                    break
                else:
                    print("当前三级地区未录入，别瞎搞！请输入其他地区！")
            else:
                print("别瞎弄！重输！")
        elif city2 == "q" or city2 == "Q":
            print("欢迎下次使用本系统！")
            break
        else:
            print("当前二级地区未录入，别瞎搞！请输入其他地区！")
    elif city1=="q" or city1=="Q":
        print("欢迎下次使用本系统！")
        break
    else:
        print("当前地区未录入，别瞎搞！请输入其他地区！")
        break