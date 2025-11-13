# Nhập số tiền gửi ban đầu và và lãi xuất hàng năm từ bàn phím
so_tien_gui_ban_dau = float(input("Nhap so tien hui ban dau: "))
lai_xuat_hang_nam = float(input("Nhap lai xuat hang nam: "))
# Tính số tiền lãi nhận được sau 1 tháng , 2 quý , 3 năm (lãi đơn)
tien_lai_sau_1_thang = so_tien_gui_ban_dau * lai_xuat_hang_nam * (1/12)
tien_lai_sau_2_quy = so_tien_gui_ban_dau * lai_xuat_hang_nam * (6/12)
tien_lai_sau_3_nam_laidon = so_tien_gui_ban_dau * lai_xuat_hang_nam * 3
# In ra kết quả số tiền lãi nhận được sau 1 tháng , 2 quý , 3 năm (lãi đơn)
print(f"So tien lai sau 1 thang: {tien_lai_sau_1_thang} VND")
print(f"So tien lai sau 2 quy: {tien_lai_sau_2_quy} VND")
print(f"So tien lai sau 3 nam: {tien_lai_sau_3_nam_laidon} VND")