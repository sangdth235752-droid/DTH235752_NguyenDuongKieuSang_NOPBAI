import datetime
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
try:
    current_date = datetime.date(year, month, day)
    next_day = current_date + datetime.timedelta(days=1)
    print("Ngày kế tiếp là:", next_day.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ. Vui lòng nhập lại.")   