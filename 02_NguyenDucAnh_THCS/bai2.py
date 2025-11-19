# Nhập vào 2 số bất kì
i = int(input("Nhập số thứ nhất: "))
j = int(input("Nhập số thứ hai: "))
# Dùng cấu trúc lặp while để kiểm tra trước khi các câu lệnh thực hiện
while j != 0:
    i, j = j, i % j
# In ra màn hình kiểm tra xem số đó có phải là chính phương hay không 
print("Ước chung lớn nhất là:",i)
