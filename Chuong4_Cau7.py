# tính độ dài AB
import math
def do_dai_AB(xA, yA, xB, yB):
    return math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
xA = float(input("Nhap hoanh do diem A: "))
yA = float(input("Nhap tung do diem A: "))
xB = float(input("Nhap hoanh do diem B: "))
yB = float(input("Nhap tung do diem B: "))
print("Do dai doan AB la:", round(do_dai_AB(xA, yA, xB, yB), 2))