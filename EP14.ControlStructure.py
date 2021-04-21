'''
โครงสร้างควบคุม (Control Structure)
1. แบบลำดับ
2. แบบเลือก
3. แบบทำซ้ำ
'''

'''
if expression: => True OR False
    statement
'''
age = int(input("ป้อนอายุของคุณ : "))
name = 'ชิรพล เหมตระการ'
if age >= 15 and age <= 100:
    print("นาย",name)
elif age > 0 :
    print("เด็กชาย",name)
else:
    print("Error")

