from threading import Thread
import  time
price=5
bread = 0
basket=500
a=0
class person(Thread):
    __username=""
    count=0

    def setusername(self,username):
        self.__username=username
    def getName(self) -> str:
        return self.__username

    def run(self) -> None:
        global bread
        global basket
        global a
        while True:
            if bread < basket:
                self.count=self.count+1
                bread=bread+1
                print(self.__username,"生产了一个汉堡","现有汉堡",bread)
                print(self.__username, "共生产了", self.count, "个汉堡")
                time.sleep(0.1)
            elif bread == basket :
                a=a+0.1
                time.sleep(a)
                continue
            elif a>=2:
                break

class people(Thread):
    __customer=""
    num = 0
    __money=500

    def setcustomer(self, customer):
        self.__customer = customer
    def getcustomer(self):
        return self.__customer

    def setmoney(self,money):
        self.__money=money
    def getmoney(self):
        return self.__money

    def run(self) -> None:
        global bread
        global price

        while True:
            if self.__money >0 and bread>0:
                self.__money=self.__money-price
                bread=bread-1
                self.num=self.num+1
                print(self.__customer,"购买了一个汉堡","总共购买了",self.num)
                time.sleep(0.1)
            elif bread==0:
                time.sleep(1)
                continue
            elif self.__money==0:
                break

p1=person()
p2=person()
p3=person()

r1=people()
r2=people()
r3=people()
r4=people()
r5=people()
r6=people()

p1.setusername("厨师1")
p2.setusername("厨师2")
p3.setusername("厨师3")
r1.setcustomer("顾客1")
r2.setcustomer("顾客2")
r3.setcustomer("顾客3")
r4.setcustomer("顾客4")
r5.setcustomer("顾客5")
r6.setcustomer("顾客6")

p1.start()
p2.start()
p3.start()
r1.start()
r2.start()
r3.start()
r4.start()
r5.start()
r6.start()

