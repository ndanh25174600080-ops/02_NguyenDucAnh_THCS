# Nhập tên đăng nhập và mật khẩu từ bàn phím 
ten_dang_nhap = input("Nhap ten dang nhap:  ")
mat_khau = input("Nhap mat khau: ")
# Kiểm tra quyền truy cập 
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")
# In ra kết quả quyền truy cập
print(f"Ket qua quyen truy cap : {quyen_truy_cap}")