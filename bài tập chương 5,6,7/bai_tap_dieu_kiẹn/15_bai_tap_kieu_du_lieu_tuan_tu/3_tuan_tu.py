#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n

#Sắp xếp dãy số theo thứ tự giảm dần
#Nhập số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))
#Tạo danh sách A gồm các số lẻ nhỏ hơn n
A = [i for i in range(1, n) if i % 2 != 0]
# Tạo danh sách B gồm các số chẵn nhỏ hơn n
B = [i for i in range(1, n) if i % 2 == 0]
A.sort(reverse=True)
B.sort(reverse=True)
#kết quả
print("Danh sách A gồm các số lẻ nhỏ hơn n (giảm dần):", A)
print("Danh sách B gồm các số chẵn nhỏ hơn n (giảm dần):", B)
