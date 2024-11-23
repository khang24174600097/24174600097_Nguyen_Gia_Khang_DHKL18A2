
# Nhập họ tên 
full_ten = input("Nhập vào họ tên đầy đủ: ")

# Tách họ tên 
name_parts = full_ten.split()
# Lấy họ và tên
ho = name_parts[0]
ten = name_parts[-1]

# kết quả
print(f"Ho: {ho}, Ten: {ten}")
