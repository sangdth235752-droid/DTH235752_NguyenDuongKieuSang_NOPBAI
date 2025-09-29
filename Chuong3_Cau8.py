a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

operator = input("Nhập phép toán (+, -, *, /): ")

if operator == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operator == "/":
    if b == 0:
        print("Không chia cho 0")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Phép toán không hợp lệ. Vui lòng nhập +, -, *, hoặc /.")