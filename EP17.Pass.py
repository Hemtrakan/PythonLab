# Pass

number = int(input("ป้อนตัวเลขของท่าน : "))


if number >= 0 and number <= 5:
    if number == 5:
        print("ตัวเลข" , number)
    elif number == 4:
        pass
    elif number == 3:
        pass
    else:
        print("จบโปแกรม")
else:
    print("จบโปแกรมโดยไม่ได้ทำอะไรเลย")