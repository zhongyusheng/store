# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# #1、请循环遍历出所有的key
# print(sorted(dict.keys()))
# #2、请循环遍历出所有的value
# # for value in dict.items():
# #     print(value[1])
# # # 3、请在字典中增加一个键值对,"k4":"v4"
# # dict["k4"]="v4"
# # print(dict)
# #
# # Friuts = {
# # 	"苹果":12.3,  # 水果和单价
# # 	"草莓":4.5,
# #     "香蕉":6.3,
# #     "葡萄":5.8,
# #     "橘子":6.4,
# #     "樱桃":15.8
# # }
# # fruits={'葡萄':19, '橘子':12, '樱桃':30}
# # money=0
# # for a in fruits.items():
# #     for b in Friuts.items():
# #         if a[0]==b[0]:
# #             money1=a[1]*b[1]
# #     money=money+money1
# # print(money)

#
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# list={}
# for i in range(len(names)):
#     list[names[i][0]]=names[i]
#     del names[i][0]
# print(list)

# list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
from DUBtils import *
# list=BubbleSort(list)
# n=1
# a=1
# while True:
#     for i in range(n,len(list)):
#         if list[i]==list[i-1]:
#             del list[i]
#             a=a+1
#             i=i-1
#         else:
#             n=n+1
#             c=a
#             a=1
#             break
#     if n==len(list)-1:
#         break
#     print(list[i - 1], c)





