# bank={'张':{
#     "账号": 11,
#     "支付密码": 1,
#     "国家": 1,
#     "省份": 1,
#     "街道": 1,
#     "门牌号": 1,
#     "账户余额": 100,
#     "开户行": 1,
# },
# '王':{
#     "账号": 22,
#     "支付密码": 1,
#     "国家": 1,
#     "省份": 1,
#     "街道": 1,
#     "门牌号": 1,
#     "账户余额": 100,
#     "开户行": 1,
# },
#
# }

bank={}
import random,sys
import string
bank_account=0
bank_password=0
bank_balance=0

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

def bank_account_funtion():
    global bank_account
    number1 = "0123456789"
    number2 = []
    for i in range(8):
        number2.append(random.choice(number1))
    bank_account = ''.join(number2)
    print("您的账号为：", bank_account)

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
            bank_password = int(input("您的支付密码："))
            bank_password1 = int(input("请再次输入您的支付密码："))



def bank_addUser():
    global bank_balance
    global bank_name
    global bank_state
    global bank_province
    global bank_street
    global bank_gate
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
    if len(bank)>=100:
        print("用户库已满！请到其他银行办理业务！")
    elif bank_name in bank:
        print("该用户已存在，请勿重复输入！")
    else:
        bank[bank_name] = {
            "账号": bank_account,
            "支付密码": bank_password,
            "国家": bank_state,
            "省份": bank_province,
            "街道": bank_street,
            "门牌号": bank_gate,
            "账户余额": bank_balance,
            "开户行": opening_bank,
        }
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
        '''.format(bank_name,bank_account,bank_password,bank_state,bank_province,bank_street,bank_gate,bank_balance,opening_bank))

def deposit():
    while True:
        bank_name3=input("请输入您的账号名：")
        if  bank_name3 in bank:
            number1=int(input("请输入您的存款金额："))
            bank_password3 = int(input("请输入您的密码："))
            if bank_password3 == int(bank[bank_name3]['支付密码']):
                print("请检验您的存款金额：",number1)
                choose5=input("是否确定存款？")
                if choose5=="是":
                    bank[bank_name3]['账户余额'] = bank[bank_name3]['账户余额']+number1
                    print("存款成功！")
                    print("您的账户当前余额为：",bank[bank_name3]['账户余额'])
                    break
                else:
                    break
        else:
            print("您输入的账户未录入！")

def withdrawal():
    while True:
        bank_name4 = input("请输入您的账号名：")
        if bank_name4 in bank:
            number2 = int(input("请输入您的取款金额："))
            print("请检验您的取款金额：", number2)
            bank_password3 = int(input("请输入您的密码："))
            if bank_password3 == int(bank[bank_name4]['支付密码']):
                print("请检验您的存款金额：", number2)
                choose5 = input("是否确定存款？")
                if choose5 == "是":
                    bank[bank_name4]['账户余额'] = bank[bank_name4]['账户余额'] - number2
                    print("取款成功！")
                    print("您的账户当前余额为：", bank[bank_name4]['账户余额'])
                    break
                else:
                    print("取消成功！")
                    break
            else:
                print("输入密码错误！")
        else:
            print("您输入的账户未录入！")

def tansfer():
    while True:
        bank_name1=input("请输入您需要转账的账户名:")
        bank_name2=input("请输入您的账户名：")
        bank_number=int(input("请输入您需要转账的数额:"))
        bank_password2=int(input("请输入您的密码："))
        if bank_name1 in bank:
            if bank_name2 in bank:
                if bank_password2==int(bank[bank_name2]['支付密码']):
                    choose3=input("是否确认转账：")
                    if choose3=="是":
                        bank[bank_name1]['账户余额']=int(bank[bank_name1]['账户余额']) +bank_number
                        bank[bank_name2]['账户余额']=int(bank[bank_name2]['账户余额']) -bank_number
                        print("恭喜您：转账成功")
                        print("您的账户余额为：",bank[bank_name2]['账户余额'])
                        break
                    else:
                        print("退出成功！")
                        break
                else:
                    print("密码错误！")
            else:
                print("您的账户未注册！请核对后重新输入！")
        else:
            print("您转账的账户未注册！请核对后重新输入!")

def refer():
    print("请输入您要查询的账户信息!输入任意一项均可！")
    bank_name3 = input("请输入您的账户名：")
    bank_account3=input("请输入您的账号:")
    if bank_name3 in bank or bank_account3 in bank:
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
                '''.format(bank_name3, bank_account, bank_password, bank_state, bank_province, bank_street, bank_gate,
                           bank_balance, opening_bank))
    else:
        print("您要查询的账号未录入！")




while True:
    display()
    choose1=int(input("请输入业务序号："))
    if choose1==1:
        bank_addUser()
        choose2=input("请选择“返回主界面“、”退出系统”：")
        if choose2=="退出系统":
            sys.exit(0)
    elif choose1==2:
        deposit()
    elif choose1==3:
        withdrawal()
    elif choose1==4:
        print(bank)
        tansfer()
    elif choose1==5:
        refer()
    else:
        choose4=input("是否确认退出系统？")
        if choose4=="是":
            sys.exit(0)
