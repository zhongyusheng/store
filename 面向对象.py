import time
# class cup():
#     high=0
#     colour=""
#     volume=0
#     texture=""
#
#     def run(self) -> None:
#         print("高度为：",self.high,"厘米的",self.colour,self.texture,"杯能够装",self.volume,"升的液体")
#
# c1=cup()
# c1.high=66
# c1.colour="红色"
# c1.volume="88"
# c1.texture="玻璃"
# c1.run()
#
# class cumputer():
#     name=""
#     screen_size=0
#     price=0
#     cpu=""
#     memory=0
#     wait_time=0
#
#     def show(self):
#         print("这是一台价值",self.price,"元的",self.name,"电脑","屏幕尺寸为：",self.screen_size,"寸","cpu为：",self.cpu,"内存为：",self.memory,"G","待机时间为：",self.wait_time,"小时")
#     def write(self,hour):
#         print("我用这台电脑练习打字",hour,"小时")
#
#     def play(self,hour,game):
#         print("我用这台电脑玩",game,"游戏",hour,"小时")
#
#     def watch(self,hour,name):
#         print("我用这台电脑看",name, hour, "小时")
#
# c2=cumputer()
# c2. name="联想"
# c2.screen_size=33
# c2.price=32210
# c2.cpu="晓龙"
# c2.memory=1000
# c2.wait_time=9
#
# c2.show()
# c2.write(5)
# c2.play(2,"超级玛丽")
# c2.watch(5,"大清王朝")

# #题目二：
# class air():
#     __brand=""
#     __price=0
#     __time=0
#     #品牌
#     def setbrand(self,brand):
#         self.__brand=brand
#     def getbrand(self):
#         return self.__brand
#     #价格
#     def setprice(self,price):
#         if price>0:
#             self.__price=price
#         else:
#             print("输入非法！")
#     def getprice(self):
#         return self.__price
#     #定时时间
#     def settime(self,time):
#         if time>0:
#             self.__time=time
#         else:
#             print("输入非法！")
#     def gettime(self):
#         return self.__time
#     #展示
#     def show(self):
#         print("这是一台",self.__brand,"空调！","价格为：",self.__price)
#
#     #开机
#     def open(self):
#         print("空调正在开机")
#         for i in range(3):
#             print(".",end="")
#             time.sleep(1)
#         print("空调开机了！")
#     #定时关机
#     def close(self):
#         if self.__time<=0:
#             print("输入错误！")
#         else:
#             print("空调将在",self.__time,"分钟后自动关闭")
#
# class test(air):
#     def run(self):
#         super().show()
#         super().open()
#         super().close()
#
# a1 = test()
# a1.setbrand("海er兄弟")
# a1.setprice(3000)
# a1.settime(20)
# a1.run()

# # 题目二：
# class student():
#     __name=""
#     __age=0
#     #姓名
#     def setname(self,name):
#         self.__name=name
#     def getname(self):
#         return self.__name
#     #年龄
#     def setage(self,age):
#         if age>0 and age<120:
#             self.__age=age
#         else:
#             print("输入非法！")
#     def getage(self):
#         return self.__age
#
#     #展示
#     def show(self):
#         print("大家好，我叫:",self.__name,"今年",self.__age,"岁了！")
#
#     #比较
#     def compare(self,student):
#         if self.__age>student.getage():
#             a=self.__age-student.getage()
#             print("我是",self.__name,"我比我同桌大",a,"岁！")
#         elif self.__age==student.getage():
#             print("我是",self.__name,"我和同桌一样大！")
#         elif self.__age<student.getage():
#             a=student.getage()-self.__age
#             print("我是",self.__name,"我比我同桌小",a,"岁！")
# s=student()
# s.setname("在噶是的")
# s.setage(32)
#
# s1=student()
# s1.setname("阿萨德")
# s1.setage(56)
#
# s.show()
# s1.show()
# s1.compare(s)







