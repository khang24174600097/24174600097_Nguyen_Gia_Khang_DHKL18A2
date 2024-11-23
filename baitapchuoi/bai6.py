# Nhập chuỗi 
input_str = input("Nhập vào chuỗi ký tự: ")

# Kiểm tra 
if input_str.startswith('-') and input_str[1:].isdigit():
    print("Đây là số âm.")
else:
    print("Đây không phải là số âm.")
