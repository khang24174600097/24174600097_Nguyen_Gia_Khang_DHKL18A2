# Nhập 
nhi_phan_str = input("Nhập vào chuỗi ký tự nhị phân: ")

# Kiểm tra 
if all(c in '01' for c in nhi_phan_str):
    thap_phan_value = int(nhi_phan_str, 2)
    print(f"{nhi_phan_str} là số nhị phân, chuyển sang thập phân: {thap_phan_value}")
else:
    print(f"{nhi_phan_str} không phải là số nhị phân hợp lệ.")
