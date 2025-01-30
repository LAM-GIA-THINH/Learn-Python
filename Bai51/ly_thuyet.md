#### **1. Mục tiêu**
- Module `timeit` được sử dụng để đo lường hiệu suất thực thi của các đoạn code. Điều này rất hữu ích khi cần so sánh hiệu suất giữa các cách tiếp cận khác nhau.

---

#### **2. Nhập module**
- Để sử dụng `timeit`, chỉ cần import module:
```python
import timeit
```

---

#### **3. Cú pháp cơ bản của `timeit.timeit()`**
- Hàm `timeit.timeit()` đo thời gian thực thi của đoạn code. Cú pháp:
```python
timeit.timeit(stmt, setup, number)
```
- **`stmt`**: Đoạn code cần kiểm tra, thường được viết dưới dạng string.
- **`setup`**: Phần chuẩn bị trước khi chạy `stmt`, thường là khai báo hàm hoặc import thư viện.
- **`number`**: Số lần chạy đoạn code để tính thời gian trung bình.

---

#### **4. Ví dụ minh họa: Tìm số nguyên tố**

##### **Hàm kiểm tra số nguyên tố**
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

##### **Ba cách tiếp cận:**
```python
# Cách 1: Sử dụng list comprehension (test1)
def test1():
    return [x for x in range(1000) if is_prime(x)]

# Cách 2: Sử dụng list comprehension có thêm điều kiện (test2)
def test2():
    return [x for x in range(1000) if x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

# Cách 3: Sử dụng vòng lặp for và biến boolean (test3)
def test3():
    primes = []
    for x in range(1000):
        if is_prime(x):
            primes.append(x)
    return primes
```

##### **Đo thời gian chạy của từng cách tiếp cận**
```python
import timeit

# Đo thời gian của test1
time1 = timeit.timeit("test1()", setup="from __main__ import test1, is_prime", number=10)
print("Thời gian test1:", time1)

# Đo thời gian của test2
time2 = timeit.timeit("test2()", setup="from __main__ import test2", number=10)
print("Thời gian test2:", time2)

# Đo thời gian của test3
time3 = timeit.timeit("test3()", setup="from __main__ import test3, is_prime", number=10)
print("Thời gian test3:", time3)
```

---

#### **5. Kết quả**
- **Test1 và Test2 (List Comprehension):** Chậm hơn do phải thực hiện các vòng lặp phức tạp.
- **Test3 (Vòng lặp for):** Nhanh hơn, dù code dài dòng hơn.

Ví dụ kết quả:
```
Thời gian test1: 0.3254 giây
Thời gian test2: 0.4158 giây
Thời gian test3: 0.2153 giây
```

---

#### **6. Lưu ý**
- **Đo nhiều lần:** Thông qua tham số `number`, hãy đo thời gian lặp lại nhiều lần để có kết quả chính xác.
- **Đo các đoạn code nhỏ:** Module `timeit` phù hợp để đo các đoạn code nhỏ và độc lập, không phù hợp cho các ứng dụng lớn.
- **Code ngắn gọn chưa chắc nhanh:** Hãy thử nghiệm hiệu suất để chọn giải pháp tốt nhất.

---

#### **7. Ví dụ khác: So sánh cách tạo danh sách**

##### **So sánh `list()` và vòng lặp**
```python
# Cách 1: Dùng list comprehension
def list_comprehension():
    return [x for x in range(1000)]

# Cách 2: Dùng vòng lặp for
def loop_append():
    result = []
    for x in range(1000):
        result.append(x)
    return result

# Đo thời gian
time_list = timeit.timeit("list_comprehension()", setup="from __main__ import list_comprehension", number=1000)
time_loop = timeit.timeit("loop_append()", setup="from __main__ import loop_append", number=1000)

print("List comprehension:", time_list)
print("Vòng lặp for:", time_loop)
```

Kết quả:
```
List comprehension: 0.0245 giây
Vòng lặp for: 0.0312 giây
```

- **Kết luận:** List comprehension thường nhanh hơn trong trường hợp đơn giản.

---

Module `timeit` là một công cụ mạnh mẽ để tối ưu hóa code. Thử nghiệm nhiều cách tiếp cận sẽ giúp bạn viết code hiệu quả hơn!