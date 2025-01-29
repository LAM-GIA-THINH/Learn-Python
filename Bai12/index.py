# Tạo một danh sách có tên là 'friends' chứa 5 phần tử
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

# In phần tử thứ 2 (chỉ số 1) và phần tử thứ 5 (chỉ số 4) trong danh sách
# friends[1]: Là 'Michael'
# friends[4]: Là 'Graham'
print(friends[1], friends[4])

# Tính số phần tử trong danh sách bằng hàm len()
# len(friends): Trả về 5 vì danh sách có 5 phần tử
print(len(friends))

# Đếm số lần xuất hiện của 'Eric' trong danh sách bằng hàm count()
# friends.count('Eric'): Trả về 1 vì 'Eric' xuất hiện 1 lần
print(friends.count('Eric'))
