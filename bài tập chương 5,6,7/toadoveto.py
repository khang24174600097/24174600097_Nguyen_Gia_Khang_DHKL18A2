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





# Nhập 
chuyen_can = float(input("Nhập điểm chuyên cần: "))
giua_ky = float(input("Nhập điểm giữa kỳ: "))
cuoi_ky = float(input("Nhập điểm cuối kỳ: "))

# Tính
diem_trung_binh = (chuyen_can + giua_ky + cuoi_ky) / 3

# xếp loại
if diem_trung_binh >= 9:
    loai_diem = "A"
elif diem_trung_binh >= 7:
    loai_diem = "B"
elif diem_trung_binh >= 5:
    loai_diem = "C"
else:
    loai_diem = "D"

# Kết quả
print("Điểm trung bình:", round(diem_trung_binh, 3))
print("Xếp loại điểm:", loai_diem)
