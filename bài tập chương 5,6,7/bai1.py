#bai 1
import math
    # Nhập bán kính và chiều cao từ bàn phím
R  = float(input("nhap ban kinh (R): "))
H  = float(input("nhap chieu cao (H): "))
#diều kiện
if R > 0 and H > 0:
    pi = 3.14
     #Tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ
    S_x_q = 2 * math.pi * R * H
    S_t_p = 2 * math.pi * R * H + 2 * pi * R**2
    the_tich = pi * R**2 * H

     # Kết quả
    print(f"dien tich xung quanh: {round(S_x_q, 2)} ")
    print(f"dien tich toan phan: {round(S_t_p, 2)} ")
    print(f"the tich: {round(the_tich, 2)}")
else:
    print("R va H phai hon hon 0")