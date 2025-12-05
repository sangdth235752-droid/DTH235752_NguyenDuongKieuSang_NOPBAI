def ROI (dt, cp):
    return (dt-cp)/cp
def GoiYDauTu (roi):
    if roi >= 0.75:
        return "NNen dau tu "
    else:
        return "Khong nen dau tu"
print("Chuong trinh tinh ROI ")
dt=int(input("Nhap doanh thu: "))
cp=int(input("Nhap chi phi: "))
roi=ROI(dt,cp)
print("Chi so ROI la: ", roi)
print("==>", GoiYDauTu(roi))