### 1. **Mục đích của `return`**  
Câu lệnh `return` được sử dụng để một hàm trả về một giá trị hoặc dữ liệu sau khi thực hiện xong tác vụ.  
**Ví dụ:**  
```python
def add(a, b):
    return a + b  # Trả về tổng của a và b

result = add(3, 5)
print(result)  # Output: 8
```

---

### 2. **Hàm không có `return`**  
Nếu một hàm không có câu lệnh `return`, nó sẽ trả về `None`.  
**Ví dụ:**  
```python
def greet(name):
    print(f"Hello, {name}!")  # Không có return

result = greet("Alice")
print(result)  # Output: None
```

---

### 3. **Trả về một giá trị**  
Hàm có thể trả về một giá trị duy nhất, chẳng hạn như một số thực (float).  
**Ví dụ:**  
```python
def calculate_vat(price, vat_rate):
    return price * vat_rate  # Trả về số tiền thuế VAT

vat_amount = calculate_vat(100, 0.1)
print(vat_amount)  # Output: 10.0
```

---

### 4. **Trả về nhiều giá trị**  
Hàm có thể trả về nhiều giá trị cùng một lúc.  
**Ví dụ:**  
```python
def get_user_info():
    name = "John"
    age = 30
    email = "john@example.com"
    return name, age, email  # Trả về nhiều giá trị dưới dạng tuple

user_info = get_user_info()
print(user_info)  # Output: ('John', 30, 'john@example.com')
```

---

### 5. **Trả về tuple**  
Khi các giá trị được trả về không được đặt trong dấu ngoặc vuông `[]` hay dấu ngoặc nhọn `{}`, chúng sẽ được trả về dưới dạng tuple.  
**Ví dụ:**  
```python
def get_coordinates():
    return 10, 20  # Trả về tuple

coordinates = get_coordinates()
print(coordinates)  # Output: (10, 20)
```

---

### 6. **Trả về list**  
Nếu các giá trị được bao quanh bởi dấu ngoặc vuông `[]`, hàm sẽ trả về một list.  
**Ví dụ:**  
```python
def get_scores():
    return [85, 90, 78]  # Trả về list

scores = get_scores()
print(scores)  # Output: [85, 90, 78]
```

---

### 7. **Trả về set**  
Nếu các giá trị được bao quanh bởi dấu ngoặc nhọn `{}`, hàm sẽ trả về một set.  
**Ví dụ:**  
```python
def get_unique_numbers():
    return {1, 2, 2, 3, 4}  # Trả về set (các giá trị trùng lặp bị loại bỏ)

unique_numbers = get_unique_numbers()
print(unique_numbers)  # Output: {1, 2, 3, 4}
```

---

### 8. **Truy cập các phần tử trong list bằng chỉ số**  
Có thể truy cập các phần tử trong list bằng chỉ số của chúng.  
**Ví dụ:**  
```python
def get_student_info():
    return ["Alice", 22, "Computer Science"]  # Trả về list

info = get_student_info()
print(info[0])  # Output: Alice (truy cập phần tử đầu tiên)
```

---

### 9. **Trả về string**  
Hàm cũng có thể trả về một string, ví dụ như một chuỗi được định dạng bằng f-string.  
**Ví dụ:**  
```python
def greet_user(name):
    return f"Hello, {name}! Welcome back."  # Trả về string

message = greet_user("Bob")
print(message)  # Output: Hello, Bob! Welcome back.
```

---

### 10. **Kiểm tra kiểu dữ liệu**  
Có thể sử dụng hàm `type()` để kiểm tra kiểu dữ liệu của giá trị trả về.  
**Ví dụ:**  
```python
def get_data():
    return 42  # Trả về một số nguyên

data = get_data()
print(type(data))  # Output: <class 'int'>
```

---

### Tóm lại  
Câu lệnh `return` cho phép các hàm trong Python trả về các giá trị hoặc dữ liệu sau khi hoàn thành tác vụ. Các giá trị trả về có thể có nhiều kiểu dữ liệu khác nhau, tùy theo cách chúng được định dạng trong câu lệnh `return`.  
