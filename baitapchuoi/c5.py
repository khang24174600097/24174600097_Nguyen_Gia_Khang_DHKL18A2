# Nhập 
input_str = input("Nhập vào chuỗi ký tự: ")
#tạo biến đếm
count_viethoa = 0  
count_vietthuong = 0  
# kiểm tra  ký tự 
for char in input_str:
    if char.isupper():  
        count_viethoa += 1
    elif char.islower(): 
        count_vietthuong += 1
# kết quả
print(f"Số chữ cái viết hoa: {count_viethoa}")
print(f"Số chữ cái viết thường: {count_vietthuong}")
