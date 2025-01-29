*   **Sets sử dụng dấu ngoặc nhọn `{}`**. Tương tự như tuples sử dụng dấu ngoặc đơn `()` và lists sử dụng dấu ngoặc vuông `[]`.

*   **Sets là unordered (không có thứ tự)**. Điều này có nghĩa là các phần tử trong set không được lưu trữ theo một thứ tự cụ thể. Thứ tự in ra có thể khác nhau tùy theo trình thông dịch Python, nhưng đôi khi nó có thể in ra theo cùng một thứ tự.

*   **Sets loại bỏ các phần tử trùng lặp**. Mỗi phần tử chỉ xuất hiện một lần trong set.

*   **Sets nhanh hơn lists trong việc tìm kiếm thành viên**. Có thể nhanh hơn đến 100 lần.

*   **Các thao tác với sets:**
    *   **`intersection`**: Tìm các phần tử chung giữa hai sets. Ví dụ, `friends_set.intersection(my_friends_set)` sẽ trả về các phần tử có mặt trong cả hai set `friends_set` và `my_friends_set`.
    *   **`difference`**: Tìm các phần tử chỉ có trong set đầu tiên mà không có trong set thứ hai. Ví dụ, `friends_set.difference(my_friends_set)` sẽ trả về các phần tử có trong `friends_set` nhưng không có trong `my_friends_set`.
    *   **`union`**: Kết hợp hai sets thành một set mới, loại bỏ các phần tử trùng lặp. Ví dụ,  `friends_set.union(my_friends_set)` sẽ trả về một set chứa tất cả các phần tử từ cả hai set, không có trùng lặp.

*   **Tạo set rỗng:**
    *   Không thể tạo set rỗng bằng cách sử dụng `{}`. Thay vào đó, cần sử dụng lệnh `set()`.
    *   Sử dụng `{}` sẽ tạo ra một dictionary chứ không phải set.
    *   Có thể tạo set có chứa các phần tử bằng cách sử dụng `{}`. Không cần dùng lệnh `set` trong trường hợp này.

*   **Tạo list rỗng:** Sử dụng `[]` hoặc `list()` với một tuple rỗng.
*   **Tạo tuple rỗng:** Sử dụng `()` hoặc `tuple()`.
