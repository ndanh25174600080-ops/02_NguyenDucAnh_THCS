# Nhập số kWh điện đã tiêu thụ từ bàn phím
kWh_1 = int(input("Nhập số kWh bac 1(kWh): "))
kWh_2 = int(input("Nhap so kWh bac 2(kWh): "))
kWh_3 = int(input("Nhap so kWh bac 3(kWh): "))
# Tính số tiền điện phải trả 
tong_so_tien_dien_phai_tra = kWh_1 * 1.678 + kWh_2 * 1.734 + kWh_3 * 2.014
# In ra kết quả số tiền điện phải trả
print(f"So tien dien phai tra: {tong_so_tien_dien_phai_tra} VND ")