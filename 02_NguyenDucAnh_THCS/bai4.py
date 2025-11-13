# Nhập số tiền bằng VND 
tien_bang_vnd = float(input("Nhap so tien bang vnd :"))
# Tỷ giá
ty_gia = 24500
# Chuyển sang tiền bằng USD
tien_bang_usd = tien_bang_vnd / ty_gia
# in ra kết quả số tiền bằng USD
print(f"Tien USD : {tien_bang_usd :.2f}")