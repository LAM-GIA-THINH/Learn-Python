1. **Chuỗi nhiều dòng:**  
   - Bạn có thể tạo một chuỗi nhiều dòng bằng cách sử dụng **ba dấu nháy đơn (`'''`)** hoặc **ba dấu nháy kép (`"""`)**.  
   - **Ví dụ:**  
     ```python
     message = """Đây là chuỗi nhiều dòng.
     Mỗi dòng được ngăn cách bởi dấu xuống dòng (\n).
     Bạn có thể viết bao nhiêu dòng tùy ý."""
     print(message)
     ```
     **Kết quả:**  
     ```
     Đây là chuỗi nhiều dòng.
     Mỗi dòng được ngăn cách bởi dấu xuống dòng (\n).
     Bạn có thể viết bao nhiêu dòng tùy ý.
     ```

2. **Tìm kiếm (find):**  
   - Dùng hàm `find()` để tìm vị trí xuất hiện đầu tiên của ký tự hoặc chuỗi con.  
   - **Ví dụ:**  
     ```python
     message = "Python is fun and powerful!"
     print(message.find('f'))       # Tìm chữ 'f', trả về vị trí đầu tiên
     print(message.find('Python')) # Tìm "Python", trả về vị trí bắt đầu
     print(message.find('Java'))   # Không tìm thấy, trả về -1
     ```
     **Kết quả:**  
     ```
     10
     0
     -1
     ```

3. **Thay thế (replace):**  
   - Hàm `replace()` thay thế chuỗi con này bằng chuỗi con khác.  
   - **Ví dụ:**  
     ```python
     message = "Python is fun!"
     new_message = message.replace('Python', 'Java')
     print(new_message)  # Thay thế "Python" bằng "Java"
     ```
     **Kết quả:**  
     ```
     Java is fun!
     ```

4. **Kiểm tra thành viên (membership):**  
   - Dùng toán tử `in` và `not in` để kiểm tra sự tồn tại của chuỗi con.  
   - **Ví dụ:**  
     ```python
     message = "I love programming in Python."
     print('Python' in message)      # Kiểm tra "Python" có trong message
     print('Java' in message)        # Kiểm tra "Java" có trong message
     print('Python' not in message) # Kiểm tra "Python" không có trong message
     ```
     **Kết quả:**  
     ```
     True
     False
     False
     ```

5. **Định dạng chuỗi (string formatting):**  
   - **Cách 1:** Sử dụng toán tử `+` để nối chuỗi.  
     ```python
     name = "Alice"
     color = "blue"
     message = name + " loves the color " + color + "."
     print(message)
     ```
     **Kết quả:**  
     ```
     Alice loves the color blue.
     ```

   - **Cách 2:** Sử dụng **f-string**.  
     ```python
     name = "Bob"
     color = "green"
     message = f"{name} loves the color {color.upper()}."  # Chuyển màu thành chữ in hoa
     print(message)
     ```
     **Kết quả:**  
     ```
     Bob loves the color GREEN.
     ```

     Bạn cũng có thể gọi hàm trong `{}`:  
     ```python
     age = 25
     print(f"{name} is {age + 1} years old next year.")
     ```
     **Kết quả:**  
     ```
     Bob is 26 years old next year.
     ```
     ```python
      name='TERRY'
      color = 'RED'
      msg = '[' + name + '] loves the color ' + color.lower() + '!'
      msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
      print(msg)
      print(msg1)
      ```
      ›[TERRY] loves the color red!
      ›[Terry] loves the color red!