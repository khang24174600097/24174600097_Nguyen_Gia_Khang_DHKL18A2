# Nhập kích cỡ ma trận m và n
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

# Tạo ma trận K kích cỡ m*n chỉ chứa số 0
K = [[0 for _ in range(n)] for _ in range(m)]

# In ra ma trận K
print("Ma trận K kích cỡ", m, "x", n, "chỉ chứa số 0:")
for row in K:
    print(row)
