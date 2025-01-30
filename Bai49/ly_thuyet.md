#### **1. Dictionary Comprehensions**

- **Dictionary comprehensions** cho phép tạo từ điển một cách ngắn gọn từ các danh sách hoặc dãy lặp đã có.
- Cú pháp cơ bản: `{key: value for item in iterable}`.
- Có thể thêm điều kiện `if` để lọc các phần tử.

##### **Ví dụ 1: Tạo từ điển từ hai danh sách**
```python
# Hai danh sách: phim và năm sản xuất
movies = ["Blade Runner", "Monty Python", "The Shining"]
years = [1982, 1975, 1980]

# Tạo từ điển với dictionary comprehension
movie_dict = {movie: year for movie, year in zip(movies, years)}
print("Từ điển phim:", movie_dict)
```

##### **Ví dụ 2: Lọc dữ liệu bằng điều kiện `if`**
```python
# Chỉ lấy phim được sản xuất trước năm 1981
filtered_dict = {movie: year for movie, year in movie_dict.items() if year < 1981}
print("Phim trước 1981:", filtered_dict)
```

##### **Ví dụ 3: Lọc dữ liệu với nhiều điều kiện**
```python
# Chỉ lấy phim trước năm 1981 và bắt đầu bằng "Monty"
filtered_dict = {
    movie: year 
    for movie, year in movie_dict.items() 
    if year < 1981 and movie.startswith("Monty")
}
print("Phim trước 1981 bắt đầu bằng 'Monty':", filtered_dict)
```

---

#### **2. List Comprehensions**

- **List comprehensions** tạo danh sách từ các dãy lặp hoặc danh sách đã có.
- Cú pháp cơ bản: `[expression for item in iterable]`.

##### **Ví dụ 1: Tạo danh sách từ một dãy số**
```python
# Tạo danh sách bình phương của các số từ 1 đến 5
squares = [x**2 for x in range(1, 6)]
print("Danh sách bình phương:", squares)
```

##### **Ví dụ 2: Kết hợp danh sách bằng `zip`**
```python
# Tạo danh sách tuple từ hai danh sách
movies = ["Blade Runner", "Monty Python", "The Shining"]
years = [1982, 1975, 1980]

combined_list = [(movie, year) for movie, year in zip(movies, years)]
print("Danh sách kết hợp:", combined_list)
```

##### **Ví dụ 3: Lọc dữ liệu bằng điều kiện `if`**
```python
# Lọc ra các phim được sản xuất trước năm 1981
filtered_list = [movie for movie, year in combined_list if year < 1981]
print("Phim trước 1981:", filtered_list)
```

##### **Ví dụ 4: Kết hợp nhiều danh sách**
```python
# Tạo danh sách tuple từ vòng lặp lồng nhau
letters = "AB"
numbers = [1, 2, 3]
tuples = [(letter, num) for letter in letters for num in numbers]
print("Danh sách tuple:", tuples)
```

##### **Ví dụ 5: Thao tác xử lý dữ liệu**
```python
# Tạo danh sách chuỗi chứa thông tin phim
info_list = [f"{movie} ({year})" for movie, year in combined_list]
print("Danh sách thông tin phim:", info_list)
```

---

#### **3. So sánh với vòng lặp `for`**

- Các comprehensions giúp code gọn gàng hơn so với việc sử dụng vòng lặp `for`.

##### **Ví dụ: Tạo danh sách bình phương**
```python
# Sử dụng vòng lặp `for`
squares = []
for x in range(1, 6):
    squares.append(x**2)
print("Sử dụng vòng lặp:", squares)

# Sử dụng list comprehension
squares_comp = [x**2 for x in range(1, 6)]
print("Sử dụng comprehension:", squares_comp)
```

##### **Ví dụ: Tạo từ điển bằng vòng lặp**
```python
# Sử dụng vòng lặp `for`
movies = ["Blade Runner", "Monty Python", "The Shining"]
years = [1982, 1975, 1980]
movie_dict = {}
for movie, year in zip(movies, years):
    movie_dict[movie] = year
print("Sử dụng vòng lặp:", movie_dict)

# Sử dụng dictionary comprehension
movie_dict_comp = {movie: year for movie, year in zip(movies, years)}
print("Sử dụng comprehension:", movie_dict_comp)
```

