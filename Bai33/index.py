print('python101 - Enumerate')  # In ra tiêu đề để giới thiệu về ví dụ sử dụng hàm enumerate.

friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']  # Danh sách bạn bè.
efriends = [(51, 'Brian'), (52, 'Judith'), (53, 'Reg'), (54, 'Loretta'), (55, 'Colin')]  # Danh sách bạn bè với số thứ tự.

# i = 51  # Biến đếm bắt đầu từ 51 (được sử dụng trong phần mã bị comment).
# for friend in friends:  # Duyệt qua danh sách friends.
#    print(i, friend)  # In ra số thứ tự và tên bạn.
#    i = i + 1  # Tăng giá trị i lên 1 sau mỗi lần lặp. (Cách thực hiện bằng vòng lặp thông thường, nhưng không dùng enumerate.)

for num, friend in enumerate(friends, 51):  # Dùng enumerate để đánh số từ 51 và duyệt qua friends.
    print(num, friend)  # In ra số thứ tự và tên bạn.
    # Output:
    # 51 Brian
    # 52 Judith
    # 53 Reg
    # 54 Loretta
    # 55 Colin

for friend in enumerate(friends, 51):  # Dùng enumerate nhưng không gán số thứ tự vào biến num.
    print(friend)  # In ra mỗi phần tử dưới dạng tuple (num, friend).
    # Output:
    # (51, 'Brian')
    # (52, 'Judith')
    # (53, 'Reg')
    # (54, 'Loretta')
    # (55, 'Colin')

for friend in enumerate(enumerate(friends, 51), -100):  # Dùng enumerate lồng nhau, bắt đầu từ -100.
    print(friend)  # In ra mỗi phần tử dưới dạng tuple lồng (index_outer, (index_inner, value)).
    # Output:
    # (-100, (51, 'Brian'))
    # (-99, (52, 'Judith'))
    # (-98, (53, 'Reg'))
    # (-97, (54, 'Loretta'))
    # (-96, (55, 'Colin'))

for num, letter in enumerate('python', start=5):  # Duyệt qua chuỗi 'python' và bắt đầu số thứ tự từ 5.
    print(num, letter)  # In ra số thứ tự và ký tự.
    # Output:
    # 5 p
    # 6 y
    # 7 t
    # 8 h
    # 9 o
    # 10 n

print(type(enumerate(friends)))  # In ra kiểu dữ liệu của đối tượng trả về từ hàm enumerate.
# Output:
# <class 'enumerate'>

print(list(enumerate(friends)))  # Chuyển đối tượng enumerate thành list và in ra.
# Output:
# [(51, 'Brian'), (52, 'Judith'), (53, 'Reg'), (54, 'Loretta'), (55, 'Colin')]
