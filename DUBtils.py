import pymysql

host="localhost"
user="root"
password=""
#数据库的增删改
def updata(sql,param,database_name):
    database = database_name
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

#数据库的查询
def select(sql,param,mode,database_name):
    database = database_name
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    if mode=="all":
        return cursor.fetchall()
    elif mode=="one":
        return cursor.fetchall()()
    elif mode=="many":
        return cursor.fetchon
        return cursor.fetmany()
    con.commit()
    con.close()
    cursor.close()

#冒泡排序
def BubbleSort(array): #array 数组
    n=len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print("排列后的数组：",array)
    return array

#for星号金字塔
def pyramind():
    a = "*"
    b = "  "
    c = int(input("请输入金字塔的层数"))
    k=0
    m=0
    for i in range(c):
        for n in range(k,10):
            print(b, end="")
        k = k + 1
        while True:
            if m < k:
                print(a, b, end="")
                m = m + 1
            else:
                m = 0
                print()
                break
#whlie星号金字塔
def pyramind1():
    a = "*"
    b = "  "
    c = int(input("请输入金字塔的层数"))
    m = 0
    k = 0
    while m < c:
        i = 0
        i = i + k
        l = 0
        while i <= 10:
            print(b, end="")
            i = i + 1
        while True:
            print(a, b, end="")
            if k <= l:
                print()
                k = k + 1
                m = m + 1
                break
            else:
                l = l + 1


#乘法表
def mul_table(num):
    i = 1
    a = "*"
    c = "="
    pro = 1
    n = 1
    while n <= num:
        while i <= num:
            if i <= n:
                pro = i * n
                print(i, a, n, c, pro, end="\t")
                i = i + 1
            else:
                print(end=" ")
                i = i + 1
        n = n + 1
        i = 1
        print()

#乘法表
def mul_table1(num):
    a = "*"
    c = "="
    pro = 1
    n = 1
    i=1
    for l in range(n,num+1):
        for k in range(num+1):
            if i <= n:
                pro = i * n
                print(i, a, n, c, pro, end="\t")
                i = i + 1
            else:
                print(end=" ")
                i = i + 1
        n = n + 1
        i = 1
        print()


#倒乘法表
def umul_table(n):
    i = 1
    a = "*"
    c = "="
    pro = 1
    while n >= 1:
        while i <= n:
            if i <= n:
                pro = i * n
                print(i, a, n, c, pro, end="\t")
                i = i + 1
            else:
                print(end=" ")
                i = i + 1
        n = n - 1
        i = 1
        print()

#三角形判断函数
def parseTrigon(a,b,c):
    if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
        if 1<=a<=10 and 1<=b<=10 and 1<=c<=10:
            if a+b>c and a+c>b and b+c>a:
                if a==b or a==c or c==b:
                    if a==b and b==c:
                        return 3
                    else:
                        return 2
                else:
                    return 1
            else:
                return 0
        else:
            return -1
    else:
        return -1

#斐波那契数列
def  Fibonacci(n):
    a=1
    b=1
    for i in range(n):
        if i<2:
            print(1)
        else:
            c=a+b
            print(c)
            a=b
            b=c





















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































