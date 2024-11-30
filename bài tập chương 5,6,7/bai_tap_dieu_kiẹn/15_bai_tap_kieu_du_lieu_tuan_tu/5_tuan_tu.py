# Nhập số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Tạo ma trận đơn vị I kích cỡ n*n
I = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# In ra ma trận đơn vị I
print("Ma trận đơn vị I kích cỡ", n, "x", n, "là:")
for row in I:
    print(row)
