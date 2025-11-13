# Nhập cân nặng và chiều cao từ bàn phím
can_nang = float(input("Nhap can nang (kg):  "))
chieu_cao = float(input("Nhap chieu cao (mét): "))
# Tính chỉ số BMI
BMI = can_nang / (chieu_cao * chieu_cao)
# In ra kết quả BMI
print(f"Ket qua BMI: {BMI}")