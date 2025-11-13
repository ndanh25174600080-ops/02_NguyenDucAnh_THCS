# Nhập giá sản phẩm và số lượng mua từ bàn phím
gia_san_pham=float(input("Nhap gia san pham :"))
so_luong=int(input("Nhap so luong mua :"))
# Tổng chi phí và thuế VAT 10%
tong_chi_phi= gia_san_pham + so_luong
thue_vat = tong_chi_phi * 0.10
tong_tien_phai_tra = tong_chi_phi + thue_vat
# In tổng tiền phải trả, làm tròn đến 2 chữ số thập phân
print(f"tong_tien_phai_tra :{tong_tien_phai_tra:.2f} ")
