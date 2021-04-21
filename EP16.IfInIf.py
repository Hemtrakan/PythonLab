# if in if

age = int(input("ป้อนอายุของท่าน : "))

if age>= 13 and age <=15:
    if age == 15:
        print("ม.3")
    if age == 14:
        print("ม.2")
    if age == 13:
        print("ม.1")
elif age >= 16 and age <= 18:
    if age == 16:
        print("ม.4")
    if age == 17:
        print("ม.5")
    if age == 18:
        print("ม.6")
elif age >= 7 and age <= 12:
    print("ประถมศึกษา")
elif age >= 0 and age <= 6:
    print("เด็ก")
else:
    print("แก่แล้วนะ")
