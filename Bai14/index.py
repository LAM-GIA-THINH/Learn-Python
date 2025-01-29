# Danh sách - Bài tập
# =====================
# - Bạn bán nước chanh trong hai tuần, các danh sách hiển thị số lượng nước chanh được bán mỗi tuần

# - Lợi nhuận cho mỗi ly nước chanh bán được là 1.5$

# - Thêm một ngày khác vào danh sách tuần 2 bằng cách nhập một con số

# - Kết hợp hai danh sách thành một danh sách có tên 'sales'

# - Tính toán/in ra số tiền bạn kiếm được vào:
#   - Ngày tốt nhất
#   - Ngày tệ nhất
#   - Riêng lẻ và tổng cộng

# Gợi ý: 3 lần in tổng cộng

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')