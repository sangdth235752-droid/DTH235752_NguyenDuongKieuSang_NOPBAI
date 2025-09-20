"""Để nhập dữ liệu từ bàn phím trong lập trình, bạn có thể sử dụng hàm input() trong Python, 
một hàm phổ biến để nhận dữ liệu đầu vào từ người dùng dưới dạng chuỗi, và chuyển đổi sang kiểu dữ liệu khác 
(ví dụ: int(), float()) nếu cần thiết để thực hiện các phép toán. 
Nhập chuỗi đơn giản:
Bạn có thể sử dụng input() mà không cần đối số, ví dụ: ten = input(). 
Khi đó, chương trình sẽ dừng lại và chờ người dùng nhập văn bản rồi nhấn Enter.
Hoặc bạn có thể truyền một chuỗi vào trong ngoặc đơn để làm thông báo cho người dùng, 
ví dụ: x = input("Nhập tên của bạn: ").
Nhập và chuyển đổi kiểu dữ liệu:
Hàm input() luôn trả về một chuỗi. Nếu bạn muốn nhập số, bạn cần chuyển đổi nó bằng các hàm 
như int() (cho số nguyên) hoặc float() (cho số thập phân).
Nhập danh sách (List):
Bạn cũng có thể sử dụng input() để nhập các phần tử của danh sách. Ví dụ, để tạo một danh sách từ chuỗi người dùng nhập, bạn có thể sử dụng list():
Tuy nhiên, cách này sẽ coi mỗi ký tự là một phần tử riêng biệt. Để nhập nhiều phần tử hơn, bạn có thể cần xử lý chuỗi sâu hơn, ví dụ như sử dụng 
phương thức split() để chia chuỗi thành danh sách các chuỗi con dựa trên dấu phân cách, sau đó chuyển đổi từng phần tử. 

"""