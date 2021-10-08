from DUBtils import *
database_name="三国集团"
sql="insert into information values (%s,%s,%s,%s,%s,%s,%s)"
param=['曹操',56,'男',106,'IBM',500,50]
updata(sql,param,database_name)
sql1="insert into information values (%s,%s,%s,%s,%s,%s,%s)"
param1=['大桥',19,'女',230,'微软',501,60]
updata(sql1,param1,database_name)
sql2="insert into information values (%s,%s,%s,%s,%s,%s,%s)"
param2=['小桥',19,'女',210,'Oracle',600,60]
updata(sql2,param2,database_name)
sql3="insert into information values (%s,%s,%s,%s,%s,%s,%s)"
param3=['许褚',45,'男',230,'Tencent',700,10]
updata(sql3,param3,database_name)

# 1.统计每个人的平均薪资
sql4="SELECT pay FROM information where age > %s"
param4=["0"]
mode="all"
sum=0
data= select(sql4,param4,mode,database_name)
for i in range(len(data)):
    sum=data[i][0]+sum
    adverge=sum/len(data)
print("平均薪资为：",adverge)

# 2.统计每个人的平均年龄
sql5="SELECT age FROM information where age > %s"
param5=["0"]
mode="all"
sum=0
data= select(sql5,param5,mode,database_name)
for i in range(len(data)):
    sum=data[i][0]+sum
    adverge1=sum/len(data)
print("平均年龄为：",adverge1)

#3.添加员工
sql6="insert into information values (%s,%s,%s,%s,%s,%s,%s)"
param6=['刘备',45,'男',220,'alibaba',500,30]
updata(sql6, param6,database_name)

#4.统计男女人数
sql7="SELECT sex FROM information where age>%s"
param7=[0]
mode="all"
num=0
num1=0
data= select(sql7,param7,mode,database_name)
for i in range(len(data)):
    if data[i][0]=="男":
        num=num+1
    elif data[i][0]=="女":
        num1=num1+1
print("男生人数为：",num)
print("女生人数为：",num1)

#5.每个部门人数
sql8="SELECT department_num FROM information where age> %s"
param9=["0"]
mode="all"
data=select(sql8,param9,mode,database_name)
list=[]
for i in range(len(data)):
    a=data[i][0]
    c = 0
    for n in range(len(data)):
        b = data[n][0]
        if a==b :
            c=c+1
    if a in list:
        continue
    else:
        list.append(a)
        print("部门编号：",a,"人数：",c)

list={"罗恩": [23, 35, 44],
      "哈利": [60, 77, 68, 88, 90],
      "赫敏": [97, 99, 89, 91, 95, 90],
      "马尔福": [100, 85, 90],
     }
print("罗恩总成绩：",sum(list["罗恩"]))
print("哈利总成绩：",sum(list["哈利"]))
print("赫敏总成绩：",sum(list["赫敏"]))
print("马尔福总成绩：",sum(list["马尔福"]))


a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
BubbleSort(a)