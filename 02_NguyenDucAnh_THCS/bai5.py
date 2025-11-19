# Nhập n
n = int(input("Nhập n: "))
# tính  S1
S1 = 0
for i in range(1, n + 1):
    S1 += i
# Tính S2
S2 = 1
for i in range(1, n):
    S2 *= i
# Tính S3
S3 = 0
for i in range(1, n + 1):
    # (-1)**(i+1) tạo ra +, -, +, -
    S3 += ((-1)**(i+1)) * (1 / i)
# Tính S4
S4 = 0
for k in range(0, n + 1):
    S4 += k / (k + 2)
# In kết quả tính S1  S2, S3, S4
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)

