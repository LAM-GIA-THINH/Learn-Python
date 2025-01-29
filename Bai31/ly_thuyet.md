### 1. **Vòng lặp `for` và `while`**
- **Vòng lặp `for`**:
  ```python
  for i in range(5):  # Lặp 5 lần
      print("Hít đất lần:", i + 1)  # Output: Hít đất lần: 1, 2, 3, 4, 5
  ```

- **Vòng lặp `while`**:
  ```python
  count = 0
  while count < 5:  # Lặp cho đến khi count >= 5
      print("Hít đất lần:", count + 1)  # Output: Hít đất lần: 1, 2, 3, 4, 5
      count += 1
  ```

---

### 2. **Cú pháp cơ bản của vòng lặp `for`**
```python
for i in [1, 2, 3, 4, 5]:  # Lặp qua danh sách
    print(i)  # Output: 1, 2, 3, 4, 5
```

---

### 3. **Lặp qua chuỗi**
```python
for letter in "Norwegian":  # Lặp qua từng ký tự trong chuỗi
    print(letter)  # Output: N, o, r, w, e, g, i, a, n
```

---

### 4. **Sử dụng `range()`**
- `range(8)`:
  ```python
  for i in range(8):  # Tạo dãy số từ 0 đến 7
      print(i)  # Output: 0, 1, 2, 3, 4, 5, 6, 7
  ```
- `range(2, 8)`:
  ```python
  for i in range(2, 8):  # Tạo dãy số từ 2 đến 7
      print(i)  # Output: 2, 3, 4, 5, 6, 7
  ```
- `range(1, 15, 3)`:
  ```python
  for i in range(1, 15, 3):  # Tạo dãy số từ 1 đến 14, bước nhảy 3
      print(i)  # Output: 1, 4, 7, 10, 13
  ```

---

### 5. **Lặp qua danh sách**
```python
friends = ["Alice", "Bob", "Charlie"]
for name in friends:  # Lặp qua từng phần tử trong danh sách
    print(name)  # Output: Alice, Bob, Charlie
```

---

### 6. **Sử dụng chỉ số (index) để lặp qua danh sách**
```python
friends = ["Alice", "Bob", "Charlie"]
for i in range(len(friends)):  # Lặp qua chỉ số của danh sách
    print("Bạn thứ", i + 1, "là:", friends[i])  
    # Output: 
    # Bạn thứ 1 là: Alice
    # Bạn thứ 2 là: Bob
    # Bạn thứ 3 là: Charlie
```

---

### 7. **Câu lệnh `break`**
```python
for i in range(10):
    if i == 5:  # Thoát khỏi vòng lặp khi i = 5
        break
    print(i)  # Output: 0, 1, 2, 3, 4
```

---

### 8. **Câu lệnh `continue`**
```python
for i in range(10):
    if i % 2 == 0:  # Bỏ qua các số chẵn
        continue
    print(i)  # Output: 1, 3, 5, 7, 9
```

---

### 9. **Vòng lặp lồng nhau**
```python
names = ["Alice", "Bob"]
numbers = [1, 2, 3]

for name in names:  # Vòng lặp bên ngoài
    for number in numbers:  # Vòng lặp bên trong
        print(name, "kết hợp với số", number)  
        # Output:
        # Alice kết hợp với số 1
        # Alice kết hợp với số 2
        # Alice kết hợp với số 3
        # Bob kết hợp với số 1
        # Bob kết hợp với số 2
        # Bob kết hợp với số 3
```

