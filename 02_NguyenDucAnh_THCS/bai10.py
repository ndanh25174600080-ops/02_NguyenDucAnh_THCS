# Nhập mức lương cơ bản và số ngày công trong tháng từ bàn phím
muc_luong_co_ban = float(input("Nhap muc luong co ban: "))
so_ngay_cong_trong_thang = int(input("Nhap so ngay cong trong thang: "))
so_ngay_cong_trong_thang_tren_22_ngay = int(input("Nhap so ngay cong trong thang tren 22 ngay: "))
so_ngay_cong_trong_thang_duoi_22_ngay = int(input("Nhap so ngay cong trong thang duoi 22 ngay: "))
# Tính tổng tiền lương nhận của nhân viên 
tien_luong_cua_nhan_vien = (muc_luong_co_ban / 22) * (0.1 * so_ngay_cong_trong_thang_tren_22_ngay - 0.05 * so_ngay_cong_trong_thang_duoi_22_ngay)
# In ra kết quả tổng tiền lương nhận của nhân viên
print(f"Tong tien luong nhan cua nhan vien: {tien_luong_cua_nhan_vien} VND" )