# Nhập chuỗi 
nhap_str = input("Nhập vào chuỗi ký tự: ")

# Kiểm tra 
if nhap_str.startswith('-') and nhap_str[1:].isdigit():
    print(" là số âm.")
else:
    print("không phải là số âm.")
