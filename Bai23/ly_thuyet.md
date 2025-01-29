### 1. **Chú thích code rất quan trọng**  
Chú thích giúp người khác và chính bạn hiểu code dễ dàng hơn, đặc biệt khi quay lại sau một thời gian dài.  
**Ví dụ:**  
```python
# Hàm tính tổng lương sau thuế
def calculate_salary(gross_salary, tax_rate):
    return gross_salary * (1 - tax_rate)
```
Chú thích trên giải thích mục đích của hàm, giúp người đọc hiểu ngay mà không cần phân tích logic bên trong.

---

### 2. **Tham số hàm thường được gọi theo thứ tự liệt kê**  
Khi gọi hàm, các tham số thường được truyền theo thứ tự khai báo.  
**Ví dụ:**  
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)  # Thứ tự đúng: name trước, age sau
```

---

### 3. **Chú thích tên cho phép đặt tên cho các tham số khi gọi hàm**  
Chú thích tên giúp bạn truyền giá trị vào hàm mà không cần quan tâm đến thứ tự.  
**Ví dụ:**  
```python
greet(age=25, name="Alice")  # Thứ tự không quan trọng khi dùng chú thích tên
```

---

### 4. **Cú pháp chú thích tên**  
Cú pháp chú thích tên bao gồm việc gán tên tham số cho giá trị khi gọi hàm.  
**Ví dụ:**  
```python
def create_profile(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

create_profile(name="Bob", age=30, country="USA")  # Sử dụng chú thích tên
```

---

### 5. **Chú thích tên tăng tính dễ đọc và rõ ràng của code**  
Chú thích tên giúp code trở nên dễ hiểu hơn, đặc biệt khi hàm có nhiều tham số.  
**Ví dụ:**  
```python
# Không dùng chú thích tên
calculate_discount(100, 0.1, 0.05)  # Khó hiểu các tham số là gì

# Dùng chú thích tên
calculate_discount(price=100, discount=0.1, tax=0.05)  # Rõ ràng và dễ hiểu
```

---

### 6. **Ví dụ về hàm có nhiều tham số không rõ ràng**  
Khi hàm có nhiều tham số, việc không dùng chú thích tên sẽ gây khó hiểu.  
**Ví dụ:**  
```python
# Không dùng chú thích tên
def create_user(id, name, age, email, is_admin):
    print(f"User {name} created with ID {id}")

create_user(1, "John", 28, "john@example.com", False)  # Khó hiểu các tham số

# Dùng chú thích tên
create_user(id=1, name="John", age=28, email="john@example.com", is_admin=False)  # Rõ ràng
```

---

### Tóm lại  
Sử dụng chú thích tên khi gọi hàm giúp code dễ đọc, dễ bảo trì và tránh nhầm lẫn, đặc biệt khi hàm có nhiều tham số hoặc các tham số không rõ ràng.  
