from threading import Thread
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import bank


da = [
    ["jason","123", "123456", "cn", "安徽省", "桃源路", "s001", 6000, "回龙观分行",1],
    ["jason","123", "123456", "cn", "安徽省", "桃源路", "s001", 6000,  "回龙观分行",2]
]
for i in range(1,99):
    n=[i,"123","123456","cn","安徽省","桃源路","s001",6000, "回龙观分行",1]
    da.append(n)
n1=[100,"123","123456","cn","安徽省","桃源路","s001",6000, "回龙观分行",1]
n2=[101,"123","123456","cn","安徽省","桃源路","s001",6000, "回龙观分行",1]
da.append(n1)
da.append(n2)
@ddt
class testaddUser(TestCase):
    @data(*da)
    @unpack
    def testadduser(self,a,b,c,d,e,f,g,h,i,j):

        result=bank.saveuser(a,b,c,d,e,f,g,h,i)
        self.assertEqual(result,j)

da1=[
    ["jason", 500, 123456,"是",1],
    ["jason",0,123456,"是",1],
    ["jason",-1,123456,"是",1],
    ["ja",500,123456,"是",4],
    ["jason",500,1234,"是",3],
    ["jason",500,1234,"否",2]
]

@ddt
class testsave(Thread):
    def run(self) -> None:
        class testsavemony(TestCase):
            @data(*da1)
            @unpack

            def testdeposit(self,speak1,speak2,speak3,speak4,h):
                result1=bank.bank_deposit(speak1,speak2,speak3,speak4)
                self.assertEqual(result1,h)

da2=[
    ["jason", 500, 123456,"是",1],
    ["jason",0,123456,"是",1],
    ["jason",-1,123456,"是",1],
    ["ja",500,123456,"是",4],
    ["jason",500,1234,"是",3],
    ["jason",500,1234,"否",2]
]

@ddt
class testdrawal(Thread):
    def run(self) -> None:
        class withdrawal1():
            @data(*da2)
            @unpack

            def testwithdrawal(self,speak1,speak2,speak3,speak4,h):
                result1=bank.withdrawal(speak1,speak2,speak3,speak4)
                self.assertEqual(result1,h)

t=testsave()
t1=testdrawal()
t.start()
t1.start()





