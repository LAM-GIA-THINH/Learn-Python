# Đây không thực sự là một game phiêu lưu...
# Phiên bản 1.0
# Làng của bạn đang bị tấn công bởi 'một bộ tộc Germanic' và bạn cần chạy đến các cửa hàng để lấy đúng những thứ cần thiết để cứu làng của bạn, và có lẽ cả một cô gái hoặc chàng trai ưa nhìn mà bạn muốn kết hôn. Tất cả giá cả đều tính bằng vàng, chưa bao gồm VAT... nhanh lên!! người German đang đến!
# Code nên cho phép bạn lấy 1 món đồ từ mỗi cửa hàng và mỗi món đồ bạn lấy nên được loại bỏ khỏi kho của cửa hàng, sau đó làm tương tự cho cửa hàng tiếp theo...
# một cách để mua là nhập từ khóa 'newt' vào ô nhập liệu... hoặc gì đó tương tự
# ở cuối, bạn nên in ra 'các món đồ' bạn đã lấy.. trong phiên bản này, bạn không cần phải trả tiền cho đồ hoặc tính tổng số tiền
# Phiên bản 1.2 thêm khả năng thoát khỏi cửa hàng mà không mua gì và chuyển sang cửa hàng tiếp theo bằng cách nhập 'exit', và thoát nếu mua một món đồ không tồn tại (nhập sai)
# Thêm ví tiền với 1000 đồng vàng và thanh toán cho các món đồ trong hoặc cuối code, hiển thị thông báo về tổng chi phí và số vàng còn lại
# Phiên bản 1.4 sửa lỗi ngẫu nhiên, 'tương thích trình duyệt', tối ưu code... cơ bản là lười biếng.. ngừng lướt TikTok/Facebook đi! ;-)
# Phiên bản 1.5 in kho hàng trước và sau khi mua như một cửa hàng tổng hợp (kết hợp kho hàng từ tất cả các cửa hàng thành một... giả vờ rằng Big Biz đã mua tất cả các cửa hàng địa phương và muốn báo cáo liên tục để quản lý kho hàng...)
# như trong tất cả các game, có một cách đặc biệt để làm điều này thực sự kiếm được tiền và giải quyết vấn đề... bạn có thể tìm ra 'chúng' không? Bạn có biết tại sao không? Có thể yêu cầu kiến thức về 'lore' thực tế của Python

# Tạo các cửa hàng
freelancers = {'name':'Cửa hàng Freelancing','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Cửa hàng Đồ cổ','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Cửa hàng Thú cưng','blue parrot':10, 'white rabbit':5, 'newt': 2}

# Kho hàng buổi sáng
department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print('Kho hàng buổi sáng của các cửa hàng', sorted(department_store.items()))
print('-----------------')

# Tạo một giỏ hàng trống
cart = {}
# Tạo ví tiền với 1000 đồng vàng
purse = 1000
buy_items1 = ''

# Lặp qua các cửa hàng/dict
for shop in (freelancers,antiques,pet_shop) :
    # Ô nhập liệu để hiển thị những gì bạn có thể mua... chụp chuỗi văn bản của thứ được mua... chuyển thành chữ thường
    buy_item = input(f'Chào mừng đến {shop["name"]}! (nhập exit để thoát cửa hàng) bạn muốn mua gì: {shop}').lower()
    # Thoát nếu nhập 'exit' hoặc mua một món đồ không tồn tại
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    # Cập nhật chuỗi
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
    # Cập nhật giỏ hàng
    cart.update({buy_item:shop.pop(buy_item)}) # sử dụng pop...
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'Bạn đã mua {buy_items}. Tổng số tiền là {total_sum} Gp. Số tiền còn lại của bạn là {purse - total_sum} Gp. Chúc bạn có một ngày hỗn loạn vui vẻ!')
print(f'Bạn đã mua {buy_items1}. Tổng số tiền là {total_sum} Gp. Số tiền còn lại của bạn là {purse - total_sum} Gp. Chúc bạn có một ngày hỗn loạn vui vẻ!')

# Kho hàng buổi tối
department_store_after = {**freelancers, **antiques, **pet_shop} # Python 3.5
department_store_after.pop('name')
print('-----------------')
print('Kho hàng buổi tối của các cửa hàng', sorted(department_store_after.items()))