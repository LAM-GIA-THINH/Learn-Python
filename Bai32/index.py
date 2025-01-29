# Vòng lặp for - Bài tập
# Lời mời dự tiệc
# Bạn đang tổ chức một bữa tiệc và muốn mời bạn bè của mình.
# Bạn muốn in ra các lời mời cho từng người bạn bằng cách sử dụng vòng lặp for.
# Các tên nằm trong hai danh sách, 'names' và 'names1'.
# Bạn cũng cần thêm hai tên vào danh sách bằng cách sử dụng hộp nhập liệu khi chạy mã.
# In ra một lời mời cho mỗi người bạn trên mỗi dòng.
# Các tên cần được viết hoa đúng cách.
# Ví dụ về in ra:
# John Chessel! Bạn được mời đến bữa tiệc vào thứ bảy.
# Bric Idle! Bạn được mời đến bữa tiệc vào thứ bảy.
# Gợi ý: Bạn có thể cần hai vòng lặp (for) để giải bài tập này.
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
#names.extend(names1)
names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    #msg1 = f'{name.title()}! {msg}'
    msg1 = name.title() + '! ' + msg
    print(msg1)