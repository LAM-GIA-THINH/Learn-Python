*   **Khái niệm cơ bản về chuỗi:**
    *   Chuỗi được sử dụng nhiều trong lập trình để xử lý văn bản.
    *   Có thể thực hiện nhiều thao tác trên chuỗi như ghép, tạo mới, xóa, thay đổi.
*   **Các cách in chuỗi:**
    *   In chuỗi bằng lệnh `print()`.
    *   Ghép chuỗi bằng dấu `+`.
    *   Nhân chuỗi bằng dấu `*` để in lặp lại.
        print("Hello" * 3)  # In chuỗi "Hello" lặp lại 3 lần
        >HelloHelloHello
    *   In nhiều chuỗi cách nhau bằng dấu phẩy `,` (dấu phẩy sẽ tự động thêm khoảng trắng).
        print("Xin chào", "thế giới", "Python!")
        >Xin chào thế giới Python!
*   **Thay đổi cách viết hoa/viết thường:**
    *   `.upper()`: Chuyển toàn bộ chuỗi thành chữ hoa.
    *   `.lower()`: Chuyển toàn bộ chuỗi thành chữ thường.
    *   `.capitalize()`: Viết hoa chữ cái đầu tiên của chuỗi và viết thường các chữ còn lại.
    *   `.title()`: Viết hoa chữ cái đầu tiên của mỗi từ trong chuỗi. Lưu ý, hàm này có thể không hoạt động tốt với các dấu nháy đơn (').
*   **Tìm thông tin về chuỗi:**
    *   `len()`: Trả về độ dài của chuỗi.
    *   `.count()`: Đếm số lần xuất hiện của một từ hoặc một ký tự trong chuỗi (có phân biệt chữ hoa chữ thường).
*   **Cắt chuỗi (slicing):**
    *   Chuỗi trong Python được đánh số bắt đầu từ 0.
    *   Sử dụng dấu ngoặc vuông `[]` để truy cập ký tự ở vị trí cụ thể, ví dụ `message` trả về ký tự đầu tiên.
    *   Có thể sử dụng chỉ số âm để truy cập từ cuối chuỗi, ví dụ `message[-1]` trả về ký tự cuối cùng.
    *   Sử dụng dấu hai chấm `:` để lấy một phần của chuỗi (slice), ví dụ `message[2:]` trả về tất cả các ký tự từ vị trí thứ 2 trở đi.
    *   `message[2:7]` trả về các ký tự từ vị trí 2 đến vị trí 6 (không bao gồm vị trí 7).
    *   `message[:6]` trả về các ký tự từ đầu chuỗi đến vị trí 5 (không bao gồm vị trí 6).

msg='welcome to Python 101: Strings'
    #012345678
print(msg)
#slicing
print(msg[:7])
›welcome to Python 101: Strings
›welcome