n = int(input("Nhập số(0-99)"))
don_vi = ["","một","hai","ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
if n < 0 or n > 99:
    print("Không hợp lệ!(0-99)")
elif n == 0:
    print("Không")
else:
    chuc = n // 10
    dv = n % 10

    if chuc == 0:
        print(don_vi[dv])
    elif chuc == 1:
        if dv == 0:
            print("Mười")
        elif dv == 5:
            print("Mười lăm")
        else:
            print("Mười", don_vi[dv])
    else:
        if dv == 0:
            print(hang_chuc[chuc])
        elif dv == 1:
            print(hang_chuc[chuc], "mốt")
        elif dv == 5:
            print(hang_chuc[chuc], "lăm")
        else:
            print(hang_chuc[chuc], don_vi[dv])