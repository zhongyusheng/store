from DUBtils import *

import random,sys
import string
bank_account=0
bank_password=0
bank_balance=0

# 主界面
def display():
    print("************************************")
    print("*          中国工商银行              *")
    print("*          账户管理系统              *")
    print("*             V1.0                 *")
    print("************************************")
    print("                                    ")
    print("*1.开户                             *")
    print("*2.存钱                             *")
    print("*3.取钱                             *")
    print("*4.转账                             *")
    print("*5.查询                             *")
    print("*6.退出                             *")

# 检验信息界面
def display2():
    print('''
        请检验您的信息!
        姓名：{0}
        账号: {1}
        支付密码:{2}
        国家:{3}
        省份:{4}
        街道: {5}
        门牌号: {6}
        账户余额:{7}
        开户行: {8}
        '''.format(bank_name, bank_account, bank_password, bank_state, bank_province, bank_street, bank_gate,
                   bank_balance, opening_bank))

# 随机生成8位数密码
def bank_account_funtion():
    global bank_account
    number1 = "0123456789"
    number2 = []
    for i in range(8):
        number2.append(random.choice(number1))
    bank_account=int( ''.join(number2))
    print("您的账号为：", bank_account)

# 输入密码函数
def bank_password_funtion():
    global bank_password
    bank_password = int(input("您的支付密码："))
    bank_password1 = int(input("请再次输入您的支付密码："))
    while True:
        if bank_password == bank_password1:
            print("请继续输入")
            break
        else:
            print("密码不一致！别瞎弄！")
            bank_password = input("您的支付密码：")
            bank_password1 = input("请再次输入您的支付密码：")

# 开户函数
def bank_addUser():
    global bank_name
    global bank_state
    global bank_province
    global bank_street
    global bank_gate
    global bank_balance
    global opening_bank
    print("请输入您的信息：")
    bank_name = input("您的姓名：")
    bank_account_funtion()
    bank_password_funtion()
    print("地址")
    bank_state = input("您的国家：")
    bank_province = input("您的省份：")
    bank_street = input("您的街道：")
    bank_gate = input("您的门牌号：")
    bank_balance = int(input("您的存款余额："))
    opening_bank = "中国工商银行北京回龙观分行"

def saveuser(bank_name,bank_account,bank_password,bank_state,bank_province,bank_street,bank_gate,bank_balance,opening_bank):
    data=[]
    sql="SELECT * FROM information "
    param=[]
    data = select(sql,param,mode="all",database_name="bank")
    b=0
    if len(data)>=100:
        print("数据库已满，请前往其他银行")
        return 3
    else:
        for i in range(len(data)):
            na=data[i][0]
            if bank_name==na:
                b=1
        if b==0:
            c=1
            sql1 = "insert into information value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param=[bank_name,bank_account,bank_password,bank_state,bank_province,bank_street,bank_gate,bank_balance,opening_bank]
            updata(sql1,param,database_name="bank")
            # display2()
            return 1
        else:
            print("该用户已存在，请勿重复输入！")
            return 2
def speak1():
    speak1=input("请输入您的账号名：")
    return speak1
def speak2():
    speak2=input("请输入您的账号名：")
    return speak2
def speak3():
    speak3=input("请输入您的账号名：")
    return speak3
def speak4():
    speak4=input("请输入您的账号名：")
    return speak4

# 存钱函数
def bank_deposit(speak1,speak2,speak3,speak4):
    while True:
        bank_name2=speak1
        data = []
        sql = "SELECT * FROM information "
        param=[]
        data = select(sql,param,"all","bank")
        b = 0
        for i in range(len(data)):
            na = data[i][0]
            if bank_name2 == na:
                b=1
                d=i
        if b==1:
            print("您的现有存款为",data[d][7])
            number1=speak2
            bank_password3 =speak3
            if bank_password3 ==data[d][2]:
                print("请检验您要存入的金额：",number1)
                choose3=speak4
                if choose3=="是":
                    sql3="update information set bank_balance = bank_balance +  %s"
                    param=[number1]
                    updata(sql3,param,"bank")
                    print("存款成功！")
                    sql = "SELECT * FROM information "
                    param = []
                    data1 = select(sql, param, "all", "bank")
                    print("您的账户当前余额为：",data1[d][7])
                    return 1
                    break
                else:
                    print("取消成功！")
                    return 2
                    break
            else:
                print("密码错误！")
                return 3
        else:
            print("您输入的账户未录入！")
            return 4
# 取钱函数
def withdrawal(speak1,speak2,speak3,speak4):
    while True:
        bank_name4 = speak1
        sql = "SELECT * FROM information "
        param = []
        data = select(sql, param, "all", "bank")
        b = 0
        for i in range(len(data)):
            na = data[i][0]
            if bank_name4 == na:
                b = 1
                d = i
        if b==1:
            print("您的现有存款为", data[d][7])
            number1 = speak2
            bank_password3 = speak3
            if bank_password3 == data[d][2]:
                print("请检验您要取走的金额：", number1)
                choose3 = speak4
                if choose3 == "是":
                    sql3 = "update information set bank_balance = bank_balance -  %s"
                    param = [number1]
                    updata(sql3, param, "bank")
                    print("取款成功！")
                    sql = "SELECT * FROM information "
                    param = []
                    data1 = select(sql, param, "all", "bank")
                    print("您的账户当前余额为：", data1[d][7])
                    return 1
                    break
                else:
                    print("取消成功！")
                    return 2
                    break
            else:
                print("密码错误！")
                return 3
        else:
            print("您输入的账户未录入！")
            return 4

# 转账函数
def bank_tansfer():
    while True:
        bank_name1=input("请输入您需要转账的账户名:")
        bank_name2=input("请输入您的账户名：")
        number=int(input("请输入您需要转账的数额:"))
        bank_password=int(input("请输入您的密码："))
        sql = "SELECT * FROM information "
        param = []
        data = select(sql, param, "all", "bank")
        b = 0
        c = 0
        for i in range(len(data)):
            if bank_name1 == data[i][0]:
                b = 1
                d = i
        if b == 1:
            for n in range(len(data)):
                if bank_name2 == data[n][0]:
                    c = 1
                    e = n
            if c == 1:
                if bank_password == data[e][2]:
                    print("请检验您要转账的金额：", number)
                    choose3 = input("是否确认转账？")
                    if choose3 == "是":
                        sql3 = "update information set bank_balance = bank_balance + %s  where bank_name = %s"
                        param = [number,bank_name1]
                        updata(sql3, param, "bank")
                        sql4 = "update information set bank_balance = bank_balance - %s  where bank_name = %s"
                        param1 = [number, bank_name2]
                        updata(sql4, param1 , "bank")
                        print("转账成功！")
                        sql = "SELECT * FROM information "
                        param = []
                        data1 = select(sql, param, "all", "bank")
                        print("您的账户当前余额为：", data1[e][7])
                        break
                    else:
                        print("取消成功！")
                        break
                else:
                    print("密码错误！")
            else:
                print("您的账户未注册！请核对后重新输入！")
        else:
            print("您转账的账户未注册！请核对后重新输入!")

# 查询函数
def refer():
    print("请输入您要查询的账户信息!输入任意以下一项均可！")
    bank_name3 = input("请输入您的账户名：")
    bank_account3=input("请输入您的账号:")
    sql = "SELECT * FROM information "
    param = []
    data = select(sql, param, "all", "bank")
    b = 0
    c = 0
    for i in range(len(data)):
        if bank_name3 == data[i][0]:
            b = 1
            d = i
    for n in range(len(data)):
        if bank_account3 == data[n][1]:
            c = 1
            e = n
    if b==1 :
        print('''
                请检验您的信息:
                姓名：{0}
                账号: {1}
                支付密码:{2}
                国家:{3}
                省份:{4}
                街道: {5}
                门牌号: {6}
                账户余额:{7}
                开户行: {8}
                '''.format(data[d][0], data[d][1], data[d][2], data[d][3], data[d][4], data[d][5], data[d][6],data[d][7], data[d][8]))
    elif c == 1:
        print('''
                请检验您的信息:
                姓名：{0}
                账号: {1}
                支付密码:{2}
                国家:{3}
                省份:{4}
                街道: {5}
                门牌号: {6}
                账户余额:{7}
                开户行: {8}
                '''.format(data[e][0], data[e][1], data[e][2], data[e][3], data[e][4], data[e][5], data[e][6],
                                   data[e][7], data[e][8]))
    else:
        print("您要查询的账号未录入！")

# # 主函数
# while True:
#     display()
#     choose1=int(input("请输入业务序号："))
#     if choose1==1:
#         bank_addUser()
#         saveuser(bank_name,bank_account,bank_password,bank_state,bank_province,bank_street,bank_gate,bank_balance,opening_bank)
#         choose2=input("请选择“返回主界面“、”退出系统”：")
#         if choose2=="退出系统":
#             sys.exit(0)
#     elif choose1==2:
#         bank_deposit(speak1,speak2,speak3,speak4)
#     elif choose1==3:
#         withdrawal()
#     elif choose1==4:
#         bank_tansfer()
#     elif choose1==5:
#         refer()
#     elif choose1==6:
#         choose4=input("是否确认退出系统？")
#         if choose4=="是":
#             sys.exit(0)
#     else:
#         print("该命令为无效指令！")
