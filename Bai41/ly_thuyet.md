*   **Lớp (Class)**:
    *   Là một kiểu dữ liệu tùy chỉnh, được sử dụng để mô tả các khái niệm trừu tượng như xe hơi, giày, phim, học sinh.
    *   Đóng vai trò như một bản thiết kế (blueprint).
    *   Bao gồm các **thuộc tính (attributes)**, là các biến (variables) và các **phương thức (methods)**, là các hàm (functions).
    *   Khi đặt tên lớp, nên sử dụng quy tắc camel casing (chữ cái đầu của mỗi từ viết hoa).

*   **Đối tượng (Object)**:
    *   Là một phiên bản thực tế được tạo ra từ một lớp (class), được xây dựng dựa trên bản thiết kế của lớp.
    *   Ví dụ, "Life of Brian" là một đối tượng của lớp "Movie".
    *   Để tạo một đối tượng, cần sử dụng cú pháp tương tự như khi gọi hàm.
        *   Ví dụ: `film_one = Movie("Life of Brian", 1979, 8.1, True)`
    *   Mỗi đối tượng có các giá trị riêng cho các thuộc tính.

*   **Thuộc tính (Attributes)**:
    *   Là các biến bên trong lớp, mô tả các đặc điểm của đối tượng.
    *   Trong lớp, cần sử dụng từ khóa `self` để truy cập các thuộc tính của đối tượng hiện tại.
        *   Ví dụ: `self.title`, `self.year`.

*   **Phương thức (Methods)**:
    *   Là các hàm bên trong lớp, định nghĩa các hành động mà đối tượng có thể thực hiện.
    *   Phương thức cũng cần sử dụng từ khóa `self` để truy cập các thuộc tính của đối tượng hiện tại.
    *   Khi gọi một phương thức của một đối tượng, đối tượng đó sẽ được truyền vào làm tham số `self` một cách ngầm định.
    *   Ví dụ: `film_two.nice_print()` tương đương với `Movie.nice_print(film_two)`.

*   **Hàm khởi tạo (\_\_init\_\_)**:
    *   Là một phương thức đặc biệt được gọi khi một đối tượng được tạo ra.
    *   Sử dụng để gán các giá trị ban đầu cho các thuộc tính của đối tượng.
    *   Ví dụ, trong lớp `Movie`, hàm `__init__` được sử dụng để nhận các thông tin như title, year, score, have_seen khi tạo một đối tượng Movie.

*   **Từ khóa `self`**:
    *   Là tham chiếu đến đối tượng hiện tại.
    *   Được sử dụng để truy cập các thuộc tính và phương thức của đối tượng bên trong lớp.
    *   Theo quy ước, `self` thường được sử dụng, nhưng có thể thay thế bằng các tên khác.

*   **Ứng dụng**:
    *   Có thể sử dụng danh sách để tạo ra một cơ sở dữ liệu các đối tượng.
    *   Ví dụ: `films = [film_one, film_two]`.
    *   Có thể truy cập các thuộc tính và phương thức của các đối tượng trong danh sách.
    *  Ví dụ `films.nice_print()`.
