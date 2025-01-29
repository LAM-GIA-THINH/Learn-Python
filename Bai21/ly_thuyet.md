*   **Định nghĩa và Mục đích:**
    *   Hàm là một cách để **gom các đoạn mã thường dùng** lại với nhau, giúp dễ dàng **tái sử dụng** sau này.
    *   Hàm giúp **chia nhỏ code**, làm cho code **dễ đọc và dễ hiểu** hơn cho cả người viết và người khác.
    *   Nên đặt **tên hàm dễ hiểu** để thuận tiện cho việc đọc và sử dụng code.

*   **Khai báo hàm:**
    *   Cần **khai báo hàm trước khi sử dụng**.
    *   Sử dụng từ khóa **`def`** để bắt đầu định nghĩa một hàm, theo sau là **tên hàm**, **dấu ngoặc đơn** và **dấu hai chấm**.
    *   Tất cả các dòng code nằm trong hàm đều phải được **thụt vào** (indented).

*   **Gọi hàm:**
    *   Để sử dụng một hàm, cần phải **gọi hàm** bằng cách viết **tên hàm** và **dấu ngoặc đơn**.

*   **Tham số (Parameters) và Đối số (Arguments):**
    *   **Tham số** là các **biến** được khai báo trong định nghĩa hàm, dùng để nhận giá trị từ bên ngoài.
    *   **Đối số** là các **giá trị** được truyền vào khi gọi hàm.
    *   Có thể **truyền nhiều tham số** vào một hàm, cách nhau bằng dấu phẩy.

*   **Giá trị mặc định (Default values):**
    *   Có thể **đặt giá trị mặc định** cho tham số bằng cách gán giá trị cho nó trong khai báo hàm.
    *   Nếu không truyền đối số tương ứng khi gọi hàm, **giá trị mặc định sẽ được sử dụng**.

*   **Ví dụ:**
    *   Hàm `greeting(name, age)` có hai tham số là `name` và `age`.
    *   Khi gọi `greeting("Brian", 32)`, `"Brian"` là đối số cho `name`, và `32` là đối số cho `age`.
    *   Khi gọi `greeting("Judith")`, vì không có đối số cho `age` nên giá trị mặc định là `28` sẽ được dùng.

*   **Định dạng chuỗi (Formatted strings):**
    *   Sử dụng f-strings (ví dụ: `f"Hello, {name}. You are {age}!"`) giúp **đơn giản hóa việc tạo chuỗi** và **dễ đọc hơn** so với việc nối chuỗi bằng `+`.
    *   Không cần chuyển đổi kiểu dữ liệu (ví dụ: từ số sang chuỗi) khi dùng f-strings.

*   **Nhập dữ liệu từ người dùng (User Input):**
    *   Có thể sử dụng hàm `input()` để **nhận dữ liệu nhập vào từ người dùng**.
    *   Giá trị nhập vào từ `input()` luôn là một chuỗi, cần chuyển đổi sang kiểu dữ liệu khác nếu cần.

Tóm lại, hàm là một công cụ quan trọng trong lập trình, giúp code trở nên có cấu trúc, dễ hiểu và tái sử dụng được. Việc hiểu rõ các khái niệm về khai báo, gọi hàm, tham số, đối số, và giá trị mặc định sẽ giúp bạn viết code hiệu quả hơn.
