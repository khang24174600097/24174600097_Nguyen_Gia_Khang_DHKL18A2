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



# nhập các điểm 
x1,y1,z1 = map(int, input("nhập A (x1,y1,z1) : ").split())
x2,y2,z2 = map(int, input("nhập B (x2,y2,z2) : ").split())
x3,y3,z3 = map(int, input("nhập C (x3,y3,z3) : ").split())
x4,y4,z4 = map(int, input("nhập A1 (x4,y4,z4) : ").split())
# tính đoạn thẳng 
AB = (((x2-x1)**2)+ ((y2-y1)**2) + ((z2-z1)**2))**(1/2)
AC = (((x3-x1)**2)+ ((y3-y1)**2) + ((z3-z1)**2))**(1/2)
AA1 =(((x4-x1)**2)+ ((y4-y1)**2) + ((z4-z1)**2))**(1/2)

the_tich = AB*AC*AA1
 #kết quả 
print("thể tích hình hộp vuông là : ", the_tich)