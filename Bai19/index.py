#Tập hợp - Bài tập

#1. Kiểm tra xem 'Eric' và 'John' có tồn tại trong danh sách friends không
#2. Kết hợp hoặc thêm hai tập hợp
#3. Tìm tên xuất hiện trong cả hai tập hợp
#4. Tìm tên chỉ có trong friends
#5. Chỉ hiển thị những tên chỉ xuất hiện trong một trong các danh sách
#6. Tạo một danh sách cars mới không có phần tử trùng lặp

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl =list(set(cars))
print(cars_no_dupl)