from HTMLTestRunner import  HTMLTestRunner
import unittest
from threading import Thread
tests=unittest.defaultTestLoader.discover(r"E:\python 练习\参数化",pattern="Test*.py")

runner=HTMLTestRunner.HTMLTestRunner(
    title="银行系统测试报告",
    description="银行添加用户测试报告",
    verbosity=1,
    stream=open(file="银行添加用户测试报告.html",mode="w+",encoding="utf-8")
)

runner.run(tests)