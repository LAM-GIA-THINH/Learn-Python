### **1. Định nghĩa và Cú pháp**
- **Lambda functions là các hàm ẩn danh cho phép định nghĩa hàm một dòng.**  
  ```python
  square = lambda x: x * x
  print(square(4))  # Output: 16
  ```

- **Cú pháp cơ bản là `lambda arguments: expression`.**  
  ```python
  multiply = lambda x, y: x * y
  print(multiply(3, 5))  # Output: 15
  ```

- **`lambda` là từ khóa để khai báo một lambda function.**  
  ```python
  increment = lambda n: n + 1
  print(increment(10))  # Output: 11
  ```

---

### **2. Đặc điểm**
- **Lambda functions có thể được gán cho một tên biến để sử dụng nhiều lần hoặc dùng một lần.**  
  ```python
  add = lambda a, b: a + b
  print(add(5, 7))  # Output: 12
  print((lambda x: x**3)(2))  # Output: 8
  ```

- **Giá trị trả về của lambda function luôn là giá trị của biểu thức (expression).**  
  ```python
  is_even = lambda x: x % 2 == 0
  print(is_even(4))  # Output: True
  ```

- **Lambda function luôn trả về một giá trị.**  
  ```python
  greet = lambda name: f"Hello, {name}!"
  print(greet("Alice"))  # Output: "Hello, Alice!"
  ```

---

### **3. So sánh với hàm thông thường**
- **Lambda function thay thế hàm thông thường có định nghĩa một dòng.**  
  ```python
  # Hàm thông thường
  def square(x):
      return x * x

  # Lambda function
  square = lambda x: x * x

  print(square(5))  # Output: 25
  ```

---

### **4. Ví dụ minh họa**
- **Hàm bình phương:**  
  ```python
  square = lambda x: x * x
  print(square(6))  # Output: 36
  ```

- **Hàm nhân đôi:**  
  ```python
  double_product = lambda x, y: 2 * x * y
  print(double_product(3, 4))  # Output: 24
  ```

- **Hàm xử lý chuỗi:**  
  ```python
  format_name = lambda name, alias: name.strip().title() + " : " + alias.strip().title()
  print(format_name(" alice ", " genius "))  # Output: "Alice : Genius"
  ```

- **Sắp xếp danh sách theo tiêu chí khác nhau:**  
  ```python
  names = ["John Smith", "Alice Brown", "Charlie Doe"]

  # Sắp xếp theo tên đầu tiên
  names.sort(key=lambda name: name.split()[0])
  print(names)  # Output: ['Alice Brown', 'Charlie Doe', 'John Smith']

  # Sắp xếp theo tên cuối cùng
  names.sort(key=lambda name: name.split()[-1])
  print(names)  # Output: ['Alice Brown', 'John Smith', 'Charlie Doe']
  ```

---

### **5. Tính ẩn danh**
- **Lambda functions thường được sử dụng khi truyền vào làm đối số cho một hàm khác.**  
  ```python
  nums = [1, 2, 3, 4, 5]

  # Lọc các số chẵn
  even_nums = list(filter(lambda x: x % 2 == 0, nums))
  print(even_nums)  # Output: [2, 4]

  # Nhân đôi tất cả các số
  doubled_nums = list(map(lambda x: x * 2, nums))
  print(doubled_nums)  # Output: [2, 4, 6, 8, 10]
  ```

---

### **6. Ứng dụng**
- **Sử dụng trong hàm `sort()`:**  
  ```python
  students = [
      {"name": "Alice", "score": 85},
      {"name": "Bob", "score": 90},
      {"name": "Charlie", "score": 75},
  ]

  # Sắp xếp theo điểm
  students.sort(key=lambda student: student["score"])
  print(students)
  # Output: [{'name': 'Charlie', 'score': 75}, {'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}]
  ```

- **Sử dụng trong `reduce()` để tính tổng:**  
  ```python
  from functools import reduce

  nums = [1, 2, 3, 4, 5]
  total = reduce(lambda x, y: x + y, nums)
  print(total)  # Output: 15
  ```

---

### **Tóm lại:**
Lambda functions là công cụ mạnh mẽ giúp viết các hàm ngắn gọn, thích hợp cho các trường hợp cần sự nhanh gọn và không cần định nghĩa một hàm riêng biệt. Chúng được ứng dụng rộng rãi trong xử lý danh sách, sắp xếp, lọc, và tính toán.