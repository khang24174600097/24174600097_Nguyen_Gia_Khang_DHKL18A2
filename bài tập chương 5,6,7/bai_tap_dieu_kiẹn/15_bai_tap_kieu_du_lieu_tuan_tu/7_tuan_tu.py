
# nhập
i = int(input("nhập số hàng i: "))
j = int(input("nhập số cột j :"))
ma_tran_don_vi = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1] 
]
# Đảo vị trí hai hàng i và j
if 0 <= i < len(ma_tran_don_vi) and 0 <= j < len(ma_tran_don_vi):
    # Thực hiện đảo
    temp = ma_tran_don_vi[i]
    ma_tran_don_vi[i] = ma_tran_don_vi[j]
    ma_tran_don_vi[j] = temp
    
    # In ra ma trận sau khi đã đảo
    print("Ma trận sau khi đảo:")
    for row in ma_tran_don_vi:
        print(row)
else:
    print("Chỉ số hàng i hoặc j không hợp lệ.")
