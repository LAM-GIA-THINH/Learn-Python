1. **Comprehensions là một công cụ mạnh mẽ để tạo danh sách (lists), bộ (tuples), tập hợp (sets), và từ điển (dictionaries) một cách ngắn gọn hơn.**
   ```python
   # Tạo danh sách các số bình phương từ 1 đến 5
   squares = [x**2 for x in range(1, 6)]
   print("Danh sách bình phương:", squares)
   ```

---

2. **Comprehensions có thể thay thế các vòng lặp `for` kết hợp với `map` và `filter`.**

   - Bằng cách sử dụng comprehensions, bạn có thể thay thế những thao tác phức tạp như dùng `map` và `filter`, đồng thời làm code dễ hiểu hơn.

   ```python
   # Sử dụng vòng lặp `for` để tạo danh sách bình phương
   numbers = [1, 2, 3, 4, 5]
   squares = []
   for num in numbers:
       squares.append(num**2)
   print("Sử dụng vòng lặp:", squares)

   # Sử dụng comprehension để tạo danh sách bình phương
   squares_comp = [num**2 for num in numbers]
   print("Sử dụng comprehension:", squares_comp)
   ```

---

3. **Ví dụ về tạo danh sách bằng comprehension:**

   - Thay vì sử dụng vòng lặp `for`, ta có thể tạo danh sách chỉ với một dòng code bằng cách sử dụng comprehension. 
   - Cấu trúc: `[biểu_thức for biến in dãy_lặp]`.

   ```python
   # Tạo danh sách bình phương bằng comprehension
   numbers = [1, 2, 3, 4, 5]
   squares = [num * num for num in numbers]
   print("Danh sách bình phương:", squares)
   ```

---

4. **Thêm điều kiện `if` vào comprehension:**

   - Bạn có thể thêm điều kiện `if` để chỉ chọn những phần tử thỏa mãn điều kiện.

   ```python
   # Lọc ra các số chẵn trong danh sách
   numbers = [1, 2, 3, 4, 5, 6, 7, 8]
   even_numbers = [num for num in numbers if num % 2 == 0]
   print("Danh sách số chẵn:", even_numbers)
   ```

---

5. **Ví dụ về sử dụng `filter` và `lambda`:**

   - `filter` kết hợp với `lambda` có thể đạt được mục tiêu tương tự như comprehension, nhưng cách viết dài dòng và khó hiểu hơn.

   ```python
   # Lọc ra số chẵn bằng `filter` và `lambda`
   numbers = [1, 2, 3, 4, 5, 6, 7, 8]
   even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   print("Sử dụng filter và lambda:", even_numbers)

   # Cách làm tương tự bằng comprehension
   even_numbers_comp = [num for num in numbers if num % 2 == 0]
   print("Sử dụng comprehension:", even_numbers_comp)
   ```

---

6. **Tạo danh sách chứa các tuple bằng comprehension:**

   - Comprehensions cũng hỗ trợ vòng lặp lồng nhau, cho phép tạo danh sách chứa các tuple một cách dễ dàng.

   ```python
   # Tạo danh sách tuple là cặp chữ cái và số
   letters = "ABCD"
   tuples = [(letter, num) for letter in letters for num in range(4)]
   print("Danh sách các tuple:", tuples)
   ```

---

7. **Mối tương quan giữa vòng lặp `for` và comprehension:**

   - Mọi thứ bạn làm với vòng lặp `for` cũng có thể làm với comprehension. 
   - Comprehension tương ứng với vòng lặp `for`, nhưng chỉ khác ở cách sắp xếp thành phần.

   ```python
   # Sử dụng vòng lặp `for` để tạo danh sách
   numbers = [1, 2, 3]
   squares = []
   for num in numbers:
       squares.append(num**2)
   print("Sử dụng vòng lặp:", squares)

   # Sử dụng comprehension để làm tương tự
   squares_comp = [num**2 for num in numbers]
   print("Sử dụng comprehension:", squares_comp)
   ```

---

8. **Comprehension không chỉ dùng cho danh sách (sets, tuples, dictionaries):**

   - Comprehensions không chỉ giới hạn trong danh sách mà còn có thể áp dụng cho tập hợp, bộ giá trị, và từ điển.

   ```python
   # Set comprehension
   unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4]}
   print("Tập hợp các số bình phương:", unique_squares)

   # Dictionary comprehension
   numbers = [1, 2, 3, 4]
   square_dict = {num: num**2 for num in numbers}
   print("Từ điển số và bình phương:", square_dict)

   # Tuple comprehension (dùng generator)
   squares_tuple = tuple(x**2 for x in range(5))
   print("Tuple các số bình phương:", squares_tuple)
   ```
