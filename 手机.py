import time
class phone():
    __brand=""
    __num=None

    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    def setnum(self,num):
        self.__num=num
    def getnum(self):
        return self.__num
    def show(self):
        print("这是一部",self.__brand,"手机","号码为:",self.__num)
    def ring(self,num1):
        print("正在给",num1,"打电话")

class newphone(phone):
    def ring1(self,num1):
        super().show()
        super().ring(num1)
    def show1(self):
        print("语音拨号中")
        for i in range(3):
            print(".",end="")
            time.sleep(1)
        print()
    def showbrand(self):
        print("品牌为：",super().getbrand(),"的手机很好用！")

n=newphone()
n.setbrand("摩托摩拉")
n.setnum("123456789")
n.ring1(input("请输入对方电话"))
n.show1()
n.showbrand()
