# Tạo một chương trình chuyển đổi khoảng cách từ Km sang dặm
# Nhận hai đầu vào từ người dùng: Tên của họ và khoảng cách tính bằng km
# In ra: Chào người dùng bằng tên và hiển thị giá trị km, giá trị dặm
# 1 dặm bằng 1.609 km
# Gợi ý: Sử dụng kiểu dữ liệu phù hợp để tính toán và in kết quả
# Bạn đã viết hoa tên chưa?
name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')