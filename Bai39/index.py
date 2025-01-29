# Mocking file read/write
from browser.local_storage import storage

# Lớp File mô phỏng hành vi của file trong Python
class File:

    # Hàm khởi tạo với tên file và chế độ hoạt động
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.content = ''

    # Hỗ trợ sử dụng context manager (with statement)
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        pass

    # Ghi dữ liệu vào file
    def write(self, data):
        if self.mode == "w":  # Chế độ ghi (write)
            self.content += data
            storage[self.name] = self.content
        elif self.mode == "a":  # Chế độ thêm (append)
            self.content += data
            storage[self.name] += self.content
        else:
            raise IOError("read only")  # Lỗi nếu file chỉ đọc

    # Đọc dữ liệu từ file
    def read(self, length=None):
        if self.name in storage:
            return storage[self.name][0:length]  # Đọc một phần hoặc toàn bộ file
        raise IOError("file not found")  # Lỗi nếu file không tồn tại

    # Đọc tất cả các dòng trong file
    def readlines(self):
        if self.name in storage:
            return storage[self.name].split('\n')  # Chia nội dung thành danh sách các dòng
        raise IOError("file not found")

    # Biến toàn cục để theo dõi dòng hiện tại khi sử dụng readline
    global currentline
    currentline = 0

    # Đọc từng dòng trong file
    def readline(self):
        if self.name in storage:
            output = storage[self.name].split('\n')[currentline]  # Lấy dòng hiện tại
            global currentline
            if currentline < len(output):
                currentline += 1  # Di chuyển đến dòng tiếp theo
            else:
                pass
            return output
        raise IOError("file not found")

    # Đóng file (không làm gì trong mock này)
    def close(self):
        pass

# Hàm mở file giả lập

def open(name, mode="r"):
    if name == 'movies.txt':
        my_file = File(name, mode)
        return my_file
    else:
        return File(name, mode)

# Tạo file greeting.txt
msg = 'Hello,\nWelcome to Monty Pythons Flying Circus!'
with open('greeting.txt', 'w') as f:
    f.write(msg)  # Ghi nội dung vào file

# Tạo file friends.csv
with open('friends.csv', 'w') as f:
    f.write('John, 1939\nEric, 1943\nMichael, 1943\nGraham, 1941\nTerryG, 1940\nTerryJ, 1942')  # Ghi danh sách bạn bè

# Tạo file cart.txt
msg = 'Iphone, 399\nHeadset, 65\nLaptop, 599\n'
with open('cart.txt', 'w') as f:
    f.write(msg)  # Ghi danh sách sản phẩm vào file

with open('cart.txt', 'a') as f:  # Thêm sản phẩm mới vào file
    f.write('display, 139\n')

# Tạo file movies.txt
with open('movies.txt', 'w') as f:
    f.write('Holy Grail, 1975\nLife of Brian, 1979\nMeaning of Life, 1983\n')  # Ghi danh sách phim

# Đọc nội dung file movies.txt
with open('movies.txt', 'r') as f:
    for line in f.readlines():  # Duyệt qua từng dòng của file
        print(line)  # In ra từng dòng
