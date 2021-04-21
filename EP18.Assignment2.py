# เขียนโปรแกรมหาตัวเลข มาก / น้อย

a = int(input("ป้อนตัวเลขที่ 1 : "))
b = int(input("ป้อนตัวเลขที่ 2 : "))


if a > b:
    print(a ," มากกว่า ", b)
elif a < b:
    print(a, " น้อยกว่า " ,b)
else :
    print(a, " เท่ากัน ",b)