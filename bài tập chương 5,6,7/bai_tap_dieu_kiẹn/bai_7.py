# Nhập 
a1 = float(input("hệ số a1: ")) 
b1 = float(input("hệ số b1: ")) 
c1 = float(input("hệ số c1: ")) 
a2 = float(input("hệ số a2: "))
b2 = float(input("hệ số b2: ")) 
c2 = float(input("hệ số c2: "))
# Tính 
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
# Giải và in kết quả
if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")
else:
    if Dx == 0 and Dy == 0:
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
