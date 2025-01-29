# 1. Thêm một câu lệnh in mới - trên một dòng mới  
#    in ra dòng chữ: 'We hear you like the color  xxx!' (xxx là một chuỗi chứa tên màu).

# 2. Mở rộng hàm bằng cách thêm một tham số đầu vào mới là `color`, với giá trị mặc định là `'red'`.

# 3. Nhập màu sắc thông qua một hộp nhập liệu và lưu vào biến `color`.

# 4. Thay đổi đoạn văn bản 'You are xx!' thành 'Bạn sẽ được xx+1 tuổi vào sinh nhật tới!'  
#    (thêm 1 vào tuổi hiện tại).

# 5. Viết hoa chữ cái đầu tiên của tên (`name`), các chữ còn lại viết thường.

# 6. Màu sắc yêu thích nên được in ra dưới dạng chữ thường.
def greeting(name, age=28, color = 'red'):
# Chào người dùng với 'name' từ 'hộp nhập liệu' và 'age' vào năm tới, nếu có, tuổi mặc định được sử dụng
# cũng bao gồm màu sắc yêu thích
    print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter favorite color: ')
greeting(name, int(age), color)