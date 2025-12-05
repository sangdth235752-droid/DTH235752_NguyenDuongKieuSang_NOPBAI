# viết chương trinh logxa
import math
def logxa(a, b):
    return math.log(b, a)
a = float(input("Nhap co so a: "))
b = float(input("Nhap so b: "))
if a>0 and a!=1 and b>0:
    print("KKet qua loga(b) la:", round(logxa(a, b), 2))
else:
    print("Du lieu khong hop le")