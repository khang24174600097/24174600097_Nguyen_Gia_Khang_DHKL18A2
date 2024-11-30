# Nhập 
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
# Khởi tạo ma trận
A = []
print("Nhập các phần tử cho ma trận A:")
for i in range(m):
    hàng = []
    for j in range(n):
        phần_tử = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        hàng.append(phần_tử)
    A.append(hàng)
# In ra ma trận
print("Ma trận A kích cỡ", m, "x", n, "là:")
for hàng in A:
    print(hàng)
