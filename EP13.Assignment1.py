# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)


weight = int(input("ป้อนน้ำหนักของคุณ (kg) : "))
hight = int(input("ป้อนส่วนสูงของคุณ (cm) : "))

# process
# cm => m
hight/=100

bmi = weight/(hight**2)

print("BMI = ", bmi)

