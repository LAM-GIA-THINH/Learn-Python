### **1. Lambda functions có thể được thay thế bằng function calls thông thường, nhưng có những trường hợp chúng thể hiện ưu điểm của mình.**
```python
# Hàm thông thường
def add(a, b):
    return a + b

# Lambda function
add_lambda = lambda a, b: a + b

print(add(3, 5))          # Output: 8
print(add_lambda(3, 5))   # Output: 8
```

---

### **2. Lambda functions có thể trả về một function khác.**
```python
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

---

### **3. Một function có thể trả về một lambda function, cho phép tạo ra các function tùy biến dựa trên các tham số đầu vào.**
```python
def price_calc(customer_type):
    if customer_type == "walk_in":
        return lambda price: price * 1.1  # Tăng 10% cho khách vãng lai
    elif customer_type == "premium":
        return lambda price: price * 0.9  # Giảm 10% cho khách hàng thân thiết
    else:
        return lambda price: price  # Không thay đổi giá

walk_in_cost = price_calc("walk_in")
premium_cost = price_calc("premium")

print(walk_in_cost(100))   # Output: 110.0
print(premium_cost(100))   # Output: 90.0
```

---

### **4. Lambda function có thể được gọi ngay lập tức sau khi được định nghĩa.**
```python
print((lambda x, y: x * y)(4, 5))  # Output: 20
```

---

### **5. Khi gọi lambda function, có thể sử dụng các tham số vị trí (positional arguments), tham số mặc định (default values), hoặc tham số được đặt tên (named arguments).**
```python
# Sử dụng tham số vị trí
print((lambda x, y: x + y)(3, 7))  # Output: 10

# Sử dụng tham số mặc định
default_add = lambda x, y=5: x + y
print(default_add(10))            # Output: 15

# Sử dụng tham số được đặt tên
print((lambda a, b: a * b)(a=4, b=6))  # Output: 24
```

---

### **6. Tham số mặc định phải được đặt ở cuối danh sách tham số.**
```python
# Đúng
correct_lambda = lambda x, y=3: x + y
print(correct_lambda(4))  # Output: 7

# Sai (sẽ gây lỗi)
# invalid_lambda = lambda x=3, y: x + y
```

---

### **7. Unpacking arguments (sử dụng `*args`) cho phép một lambda function nhận một số lượng tham số tùy ý.**
```python
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

---

### **8. Lambda function có thể được sử dụng để tạo các function có thể tái sử dụng một cách linh hoạt.**
```python
# Tạo một hàm lambda để kiểm tra số chẵn
is_even = lambda x: x % 2 == 0

# Kiểm tra danh sách số
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(is_even, nums))
print(even_nums)  # Output: [2, 4, 6]
```

---

### **Tóm lại:**  
Lambda functions rất mạnh mẽ, ngắn gọn và linh hoạt, giúp tạo ra các function nhỏ gọn, đơn giản mà không cần sử dụng `def`. Chúng hữu ích trong các tình huống cần tạo function nhanh hoặc tái sử dụng logic một cách linh hoạt.