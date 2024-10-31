
# Nhập
ky_tu =float(input("Nhập một ký tự: "))

# Kiểm tra 
if ky_tu in 'aeiou':
    print(f"{ky_tu} là nguyên âm")
elif ky_tu.isalpha():
    print(f"{ky_tu} là phụ âm")
else:
    print(f"{ky_tu} không phải là ký tự trong bảng chữ cái tiếng Anh")
