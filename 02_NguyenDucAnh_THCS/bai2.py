# Nhập số kẹo và số học sinh từ bàn phím
so_keo = int(input("Nhap so keo :"))
so_hoc_sinh = int(input("Nhap so hoc sinh :"))
# Tính số kẹo mỗi học sinh nhận được và số kẹo còn thừa
so_keo_moi_hoc_sinh = so_keo // so_hoc_sinh
so_keo_con_thua = so_keo % so_hoc_sinh
# In ra kết quả số kẹo mỗi học sinh nhận được và số kẹo còn thừa
print(f"So keo moi hoc sinh nhan duoc : {so_keo_moi_hoc_sinh} kẹo ")
print(f"So keo con thua : {so_keo_con_thua} kẹo ")


