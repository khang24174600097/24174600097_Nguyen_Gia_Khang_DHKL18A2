# Nhập 
str_1 = input("Nhập vào xâu ký tự : ")
str_2 = input("Nhập vào xâu ký tự : ")

# Kiểm tra
if str_2 in str_1:
    print(f"'{str_2}' nằm trong '{str_1}'")
else:
    print(f"'{str_2}' không nằm trong '{str_1}'")
if str_1 in str_2:
    print(f"'{str_1}' nằm trong '{str_2}'")
else:
    print(f"'{str_1}' không nằm trong '{str_2}'")
