# Tạo một danh sách có tên là 'friends' chứa 5 phần tử
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

# Sắp xếp danh sách tăng dần
friends.sort()
print("Danh sách sau khi sắp xếp tăng dần:", friends)

# Sắp xếp danh sách giảm dần
friends.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", friends)

# Đảo ngược danh sách
friends.reverse()
print("Danh sách sau khi đảo ngược:", friends)

# Tìm giá trị nhỏ nhất trong danh sách
print("Giá trị nhỏ nhất:", min(friends))

# Tìm giá trị lớn nhất trong danh sách
print("Giá trị lớn nhất:", max(friends))

# Thêm phần tử mới vào cuối danh sách
friends.append('Alice')
print("Danh sách sau khi thêm Alice:", friends)

# Chèn phần tử mới vào vị trí xác định
friends.insert(2, 'Bob')
print("Danh sách sau khi chèn Bob vào vị trí 2:", friends)

# Xóa phần tử có giá trị 'Eric'
friends.remove('Eric')
print("Danh sách sau khi xóa Eric:", friends)

# Xóa phần tử cuối danh sách
last_friend = friends.pop()
print("Phần tử bị xóa:", last_friend)
print("Danh sách sau khi xóa phần tử cuối:", friends)

# Xóa phần tử tại vị trí 1
removed_friend = friends.pop(1)
print("Phần tử bị xóa tại vị trí 1:", removed_friend)
print("Danh sách sau khi xóa:", friends)

# Xóa tất cả các phần tử trong danh sách
friends.clear()
print("Danh sách sau khi xóa tất cả phần tử:", friends)

# Tạo lại danh sách để minh họa xóa danh sách toàn bộ
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
del friends
# print(friends)  # Lệnh này sẽ báo lỗi vì danh sách đã bị xóa

# Tạo lại danh sách để minh họa xóa phần tử theo chỉ số
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
del friends[2]
print("Danh sách sau khi xóa phần tử tại chỉ số 2:", friends)

# Tạo bản sao danh sách bằng slicing
friends_copy = friends[:]
print("Bản sao danh sách bằng slicing:", friends_copy)

# Tạo bản sao danh sách bằng copy()
friends_copy_2 = friends.copy()
print("Bản sao danh sách bằng copy():", friends_copy_2)
