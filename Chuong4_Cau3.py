def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif bmi <= 34.9:
        return "Obesity class I"
    elif 35 <= bmi <= 39.9:
        return "Obesity class II"
    else:
        return "Obesity class III"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"

# Chương trình chính
height = float(input("Nhap chieu cao (met): "))
weight = float(input("Nhap can nang (kg): "))
bmi = BMI(height, weight)

print("Chi so BMI cua ban la:", round(bmi, 2))
print("Phan loai:", PhanLoai(bmi))
print("Nguy co mac cac benh lien quan den beo phi:", NguyCoBenh(bmi))