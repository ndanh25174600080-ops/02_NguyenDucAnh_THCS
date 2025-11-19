# Nhập mẫu số và tử số 
i = int(input("Nhap tu so:"))
j = int(input("Nhap mau so:"))
# Dùng câu lệnh while để kiểm tra sau khi thực hiện câu lệnh 
while j != 0:
    i, j = j, i % j
ucln=i
# In ra màn hình phân số tối giản
print("Phân số tối giản là :", i // ucln,"/",  j // ucln )