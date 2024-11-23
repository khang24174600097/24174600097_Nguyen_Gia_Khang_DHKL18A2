
# Nhập
ky_tu =(input("Nhập một ký tự: ")).lower()

# Kiểm tra 
if ky_tu in 'aeiou':
    print(f"{ky_tu} là nguyên âm")
elif ky_tu.isalpha():
    print(f"{ky_tu} là phụ âm")
else:
    print(f"{ky_tu} không phải là ký tự trong bảng chữ cái tiếng Anh")
