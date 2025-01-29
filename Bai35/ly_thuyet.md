* **Khái niệm:**
    * Từ điển trong Python lưu trữ các cặp "tên-giá trị" hoặc "khóa-giá trị".
        * Ví dụ: `student = {"name": "Alice", "age": 22, "major": "Computer Science"}`.
        * Khóa là `"name"`, `"age"`, `"major"`, và giá trị tương ứng là `"Alice"`, `22`, `"Computer Science"`.

* **Cú pháp:**
    * Tạo một từ điển bằng cách sử dụng dấu ngoặc nhọn `{}`.
        * Ví dụ: `movie = {"title": "Life of Brian", "year": 1979, "cast": ["John", "Eric", "Michael", "George", "Terry"]}`.
    * Các cặp khóa-giá trị được phân tách bằng dấu hai chấm `:` và các cặp được phân tách bằng dấu phẩy `,`.
    * Ví dụ: `person = {"name": "Bob", "age": 30, "location": "New York"}`.
    * Khóa có thể là chuỗi, số hoặc các kiểu dữ liệu khác. Giá trị có thể là bất kỳ kiểu dữ liệu nào như chuỗi, số, danh sách.

* **Truy cập giá trị:**
    * Sử dụng cú pháp dấu ngoặc vuông `[]` với khóa để truy cập giá trị tương ứng. 
        * Ví dụ: `movie["title"]` sẽ trả về `"Life of Brian"`.
    * Nếu khóa không tồn tại, sẽ gây ra lỗi.
        * Ví dụ: `movie["director"]` sẽ gây lỗi `KeyError` nếu khóa "director" không có trong từ điển.
    * **Phương thức `get()`:**
        * Sử dụng `movie.get("budget")` để truy cập giá trị của khóa "budget". Nếu khóa không tồn tại, nó sẽ trả về `None` thay vì gây ra lỗi.
            * Ví dụ: `movie.get("budget")` trả về `None`.
        * Có thể thiết lập giá trị mặc định nếu khóa không tồn tại bằng cách sử dụng `movie.get("budget", "not found")`.
            * Ví dụ: `movie.get("budget", "not found")` trả về `"not found"`.

* **Cập nhật từ điển:**
    * Có thể thay đổi giá trị của một khóa hiện có bằng cú pháp dấu ngoặc vuông `[]`. 
        * Ví dụ: `movie["title"] = "The Holy Grail"` sẽ thay đổi giá trị của "title".
    * Có thể thêm một khóa-giá trị mới bằng cách gán giá trị cho một khóa chưa có trong từ điển.
        * Ví dụ: `movie["budget"] = 250000` sẽ thêm khóa "budget" vào từ điển.
    * **Phương thức `update()`:**
        * Cập nhật nhiều khóa-giá trị cùng một lúc bằng phương thức `update()` và truyền vào một từ điển khác.
            * Ví dụ: `movie.update({"year": 1980, "rating": 8.5})` sẽ cập nhật các khóa "year" và "rating" trong từ điển.

* **Xóa mục:**
    * **Lệnh `del`:** Xóa một mục bằng lệnh `del` và khóa tương ứng.
        * Ví dụ: `del movie["year"]` sẽ xóa khóa "year" khỏi từ điển.
    * **Phương thức `pop()`:** Xóa một mục và trả về giá trị của mục đó.
        * Ví dụ: `year = movie.pop("year")` sẽ xóa khóa "year" và lưu giá trị của nó vào biến `year`.

* **Các thao tác khác:**
    * **`len()`:** Lấy số lượng mục trong từ điển.
        * Ví dụ: `len(movie)` sẽ trả về số lượng mục trong từ điển `movie`.
    * **`keys()`:** Lấy danh sách các khóa trong từ điển.
        * Ví dụ: `movie.keys()` sẽ trả về `dict_keys(['title', 'year', 'cast'])`.
    * **`values()`:** Lấy danh sách các giá trị trong từ điển.
        * Ví dụ: `movie.values()` sẽ trả về `dict_values(['Life of Brian', 1979, ['John', 'Eric', 'Michael', 'George', 'Terry']])`.
    * **`items()`:** Lấy danh sách các cặp khóa-giá trị (dưới dạng tuple).
        * Ví dụ: `movie.items()` sẽ trả về `dict_items([('title', 'Life of Brian'), ('year', 1979), ('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])])`.

* **Vòng lặp qua từ điển:**
    * Duyệt qua các khóa: `for key in movie:`.
        * Ví dụ:
            ```python
            for key in movie:
                print(key)
            ```
        * Kết quả sẽ là: `title`, `year`, `cast`.
    * Duyệt qua các cặp khóa-giá trị: `for key, value in movie.items():`.
        * Ví dụ:
            ```python
            for key, value in movie.items():
                print(f"{key}: {value}")
            ```
        * Kết quả sẽ là:
            ```
            title: Life of Brian
            year: 1979
            cast: ['John', 'Eric', 'Michael', 'George', 'Terry']
            ```
