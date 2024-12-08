# Khởi tạo ma trận 
A = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
# Nhập
i = int(input("Nhập chỉ số cột i : "))
j = int(input("Nhập chỉ số cột j : "))

# Kiểm tra
if 0 <= i < len(A[0]) and 0 <= j < len(A[0]):
    # Đảo vị trí i và j
    for row in A:
        # Đổi giá trị i và j
        row[i], row[j] = row[j], row[i]

    # đã đảo
    print("Ma trận sau khi đảo:")
    for row in A:
        print(" ".join(map(str, row)))
else:
    print("Chỉ số cột i hoặc j không hợp lệ.")
