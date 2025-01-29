*   **Mở tệp:** Để làm việc với tệp, trước tiên cần mở nó bằng hàm `open()`. Cần chỉ định tên tệp và chế độ mở (ví dụ: 'r' cho đọc, 'w' cho ghi, 'a' cho thêm vào).

*   **Đọc tệp:**
    *   Có thể đọc toàn bộ nội dung tệp bằng `read()`.
    *   Có thể đọc một số lượng ký tự cụ thể bằng `read(n)`.
    *   Có thể đọc từng dòng một bằng `readline()`.
    *   Có thể đọc tất cả các dòng vào một danh sách bằng `readlines()` hoặc `splitlines()`.
    *  `splitlines()` tốt hơn trong việc tách các dòng.

*  **Đóng tệp:** Sau khi làm việc xong với tệp, cần đóng nó bằng `close()`. Việc này rất quan trọng để tránh các vấn đề tiềm ẩn.
    *   Có thể dùng **context manager** `with open(...) as f:` để tự động đóng tệp sau khi sử dụng, giúp đơn giản hóa code.
    
*   **Xử lý dữ liệu đọc từ tệp:**
    *   Dữ liệu đọc từ tệp thường ở dạng chuỗi.
    *   Có thể dùng `split()` để tách dữ liệu theo dấu phân cách (ví dụ: dấu phẩy trong tệp CSV).
    *   Có thể loại bỏ khoảng trắng thừa bằng `strip()`.
    *   Có thể chuyển đổi dữ liệu từ chuỗi sang kiểu dữ liệu khác (ví dụ: `int()` để chuyển chuỗi thành số nguyên).

*   **Duyệt qua các dòng trong tệp:**
    *   Có thể duyệt qua từng dòng trong tệp bằng vòng lặp `for line in f`
