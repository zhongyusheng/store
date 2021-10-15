class chef():
    __username=""
    __age=0
    def setusername(self,username):
        self.__username=username
    def getusername(self):
        return self.__username
    def setage(self,age):
        if age>0 and age<120:
            self.__age=age
        else:
            print("输入非法！")
    def getage(self):
        return self.__age
    def rice(self):
        print(self.__username,"正在蒸饭！")

class dish(chef):
    __vegetable=""

    def setvegetable(self,vegetable):
        self.__vegetable=vegetable
    def getvegetable(self):
        return self.__vegetable
    def menu(self):
        print(super().getusername(),"正在炒",self.__vegetable)

class grandson(dish):
    def rice(self):
        print("年龄为：",super().getage(),"岁的",super().getusername(),"正在蒸饭！")
    def menu(self):
        print("年龄为：",super().getage(),"岁的",super().getusername(),"正在炒",super().getvegetable())
class test(grandson):
    def run(self):
        n=grandson()
        n.setusername("张三")
        n.setage(55)
        n.setvegetable("白菜")
        n.rice()
        n.menu()

t=test()
t.run()