# Nhập 
n = int(input("Nhập vào số nguyên dương n: "))
# In ra dãy số nguyên tố nhỏ hơn n
print("Các số nguyên tố nhỏ hơn", n, "là:")
# Kiểm tra
for num in range(2, n):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
