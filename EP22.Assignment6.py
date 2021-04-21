# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)


weight = int(input("ป้อนน้ำหนักของคุณ (kg) : "))
hight = int(input("ป้อนส่วนสูงของคุณ (cm) : "))

# process
# cm => m
hight/=100

bmi = weight/(hight**2)

print("BMI = ", bmi)

if bmi < 18.50:
    print("น้ำหนักน้อย / ผอม")
elif bmi >= 18.50 and bmi <= 22.90:
    print("ปกติ (สุขภาพดี)")
elif bmi >= 23  and bmi <= 24.90:
    print("ท้วม / โรคอ้วนระดับ 1")
elif bmi >= 25 and bmi <= 29.90:
    print("อ้วน / โรคอ้วนระดับ 2")
else:
    print("อ้วนมาก / โรคอ้วนระดับ 3")
