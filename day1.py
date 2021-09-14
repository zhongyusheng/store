import xlrd
import xlwt
wd=xlrd.open_workbook(filename="12月份衣服销售数据.xlsx",encoding_override=True)
st=wd.sheet_by_name("12月份各种服饰销售情况")
rows= st.nrows
cols= st.ncols

for i in range(rows):
   for j in range(cols):
        print(st.cell_value(i,j),"     ",end="  ")
   print()

sum=0
for i in range(1,rows):
    data=st.row_values(i)
    number1=data[2]
    number2=data[4]
    sum=float(sum+number1*number2)
print("总销售额为：")
print("%.2f" %sum)

average=0
time=0
sum1=0
for i in range(1,rows):
    time=time+1
    data1=st.row_values(i)
    sum1=sum1+data1[4]
average=sum1/time
print("平均每日销售量为：")
print("%.0f" %average)

sum2=0
s1=0
sum3=0
s2=0
sum4=0
s3=0
sum5=0
s4=0
sum6=0
s5=0
sum7=0
s6=0
for i in range(1,rows):
    data2=st.row_values(i)
    if data2[1]=="羽绒服":
        sum2=sum2+data2[4]
    elif data2[1]=="牛仔裤":
        sum3=sum3+data2[4]
    elif data2[1]=="风衣":
        sum4=sum4+data2[4]
    elif data2[1]=="皮草":
        sum5=sum5+data2[4]
    elif data2[1] == "T血":
        sum6 = sum6 + data2[4]
    elif data2[1] == "衬衫":
        sum7 = sum7 + data2[4]
    s1=sum2/sum1
    s2=sum3/sum1
    s3= sum4/ sum1
    s4 = sum5 / sum1
    s5 = sum6 / sum1
    s6 = sum7 / sum1
print("羽绒服月销售量占比为：")
print('{:.2%}'.format(s1))
print("牛仔裤月销售量占比为：")
print('{:.2%}'.format(s2))
print("风衣月销售量占比为：")
print('{:.2%}'.format(s3))
print("皮草销售量占比为：")
print('{:.2%}'.format(s4))
print("T血销售量占比为：")
print('{:.2%}'.format(s5))
print("衬衫销售量占比为：")
print('{:.2%}'.format(s6))