#### **1. Tính ngẫu nhiên giả**
- Module `random` tạo ra các số ngẫu nhiên giả (pseudo-random). Chúng được tính toán dựa trên thuật toán và không phải hoàn toàn ngẫu nhiên.
- Nếu cần độ ngẫu nhiên thực sự, đặc biệt trong bảo mật (như tạo mật khẩu), hãy sử dụng module `secrets` hoặc `os.urandom()`.

---

#### **2. Nhập module**
- Sử dụng lệnh `import random` để sử dụng các hàm của module này.
```python
import random
```

---

#### **3. Các hàm ngẫu nhiên**

##### **Hàm `random()`**
- Tạo một số thực ngẫu nhiên từ `0` đến gần `1` (không bao gồm `1`).
```python
print("Số ngẫu nhiên:", random.random())
```

##### **Hàm `uniform(a, b)`**
- Tạo một số thực ngẫu nhiên trong khoảng `[a, b]`.
```python
print("Số thực ngẫu nhiên từ 1 đến 10:", random.uniform(1, 10))
```

##### **Hàm `randint(a, b)`**
- Tạo một số nguyên ngẫu nhiên trong khoảng `[a, b]`.
```python
print("Số nguyên ngẫu nhiên từ 1 đến 100:", random.randint(1, 100))
```

##### **Hàm `randrange(start, stop, step)`**
- Tạo một số nguyên ngẫu nhiên trong khoảng từ `start` đến `stop` (không bao gồm `stop`), với bước nhảy là `step`.
```python
print("Số nguyên ngẫu nhiên từ 0 đến 10 (bước nhảy 2):", random.randrange(0, 10, 2))
```

##### **Hàm `choice(seq)`**
- Chọn ngẫu nhiên một phần tử từ một chuỗi (list, tuple, string).
```python
fruits = ["apple", "banana", "cherry", "date"]
print("Trái cây ngẫu nhiên:", random.choice(fruits))
```

##### **Hàm `sample(population, k)`**
- Chọn `k` phần tử ngẫu nhiên không trùng lặp từ một chuỗi.
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("3 số ngẫu nhiên không trùng lặp:", random.sample(numbers, 3))
```

##### **Hàm `shuffle(list)`**
- Xáo trộn thứ tự các phần tử trong một danh sách.
```python
letters = ["A", "B", "C", "D"]
random.shuffle(letters)
print("Danh sách sau khi xáo trộn:", letters)
```

---

#### **4. Làm việc với danh sách**

##### **Chọn ngẫu nhiên một phần tử**
```python
movies = ["Blade Runner", "The Matrix", "Inception", "Interstellar"]
print("Phim ngẫu nhiên:", random.choice(movies))
```

##### **Chọn nhiều phần tử ngẫu nhiên không trùng lặp**
```python
actors = ["Ryan Gosling", "Keanu Reeves", "Leonardo DiCaprio", "Christian Bale"]
print("2 diễn viên ngẫu nhiên:", random.sample(actors, 2))
```

##### **Xáo trộn danh sách**
```python
random.shuffle(movies)
print("Danh sách phim sau khi xáo trộn:", movies)
```

---

#### **5. Làm việc với chuỗi**

##### **Nhập module `string`**
```python
import string
print("Chữ cái thường:", string.ascii_lowercase)
print("Chữ cái hoa:", string.ascii_uppercase)
print("Chữ số:", string.digits)
```

##### **Tạo chuỗi ký tự ngẫu nhiên với vòng lặp**
```python
length = 8
random_string = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
print("Chuỗi ngẫu nhiên:", random_string)
```

##### **Tạo chuỗi ký tự ngẫu nhiên không trùng lặp**
```python
length = 8
random_string = "".join(random.sample(string.ascii_letters + string.digits, length))
print("Chuỗi không trùng lặp:", random_string)
```

---

#### **6. Lưu ý**
- Hàm `random.choices()` có thể được sử dụng để chọn ngẫu nhiên phần tử (cho phép trùng lặp), nhưng có thể không hoạt động trong một số môi trường hạn chế.

##### **Ví dụ `random.choices()`**
```python
letters = "ABCDE"
print("Chọn 5 ký tự ngẫu nhiên có thể trùng:", random.choices(letters, k=5))
```

---

Module `random` là một công cụ hữu ích cho nhiều tác vụ liên quan đến tính ngẫu nhiên, từ làm việc với số, danh sách, chuỗi, cho đến các ứng dụng phức tạp hơn như tạo dữ liệu giả hoặc trò chơi.