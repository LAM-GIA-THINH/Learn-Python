* **Dictionaries không có thứ tự và không thể chứa các key trùng lặp**, tuy nhiên có thể chứa các giá trị trùng lặp.
    * Ví dụ:
      ```python
      my_dict = {"a": 1, "b": 2, "c": 3}
      my_dict["a"] = 4  # Chỉnh sửa giá trị của khóa "a"
      print(my_dict)  # Output: {"a": 4, "b": 2, "c": 3}
      ```

* **Kiểm tra membership (sự tồn tại) trong dictionary diễn ra rất nhanh**, tương tự như sets.
    * Ví dụ kiểm tra sự tồn tại của một key:
      ```python
      holy_grail = {"Arthur": "King", "Lancelot": "Knight", "Galahad": "Knight"}
      if "Arthur" in holy_grail:
          print("Arthur exists in the dictionary")  # Output: Arthur exists in the dictionary
      if "Merlin" not in holy_grail:
          print("Merlin does not exist in the dictionary")  # Output: Merlin does not exist in the dictionary
      ```

* **Có nhiều cách để kết hợp các dictionaries lại với nhau**:
    * **Phương pháp update:** Sử dụng phương thức `.update()` để thêm một dictionary vào một dictionary đã có.
      * Ví dụ:
        ```python
        people = {"Alice": 25, "Bob": 30}
        python = {"Guido": 60, "Van Rossum": 65}
        people.update(python)
        print(people)  # Output: {"Alice": 25, "Bob": 30, "Guido": 60, "Van Rossum": 65}
        ```
    * **Phương pháp comprehension:** Sử dụng vòng lặp `for` để duyệt qua các dictionaries và cập nhật vào một dictionary đích.
      * Ví dụ:
        ```python
        python = {"Guido": 60, "Van Rossum": 65}
        holy_grail = {"Arthur": "King", "Lancelot": "Knight"}
        people1 = {}
        for group in [python, holy_grail]:
            for key, value in group.items():
                people1[key] = value
        print(people1)  # Output: {"Guido": 60, "Van Rossum": 65, "Arthur": "King", "Lancelot": "Knight"}
        ```
    * **Phương pháp unpacking:** Sử dụng toán tử `**` để "unpack" các dictionaries và gộp chúng lại.
      * Ví dụ:
        ```python
        python = {"Guido": 60, "Van Rossum": 65}
        holy_grail = {"Arthur": "King", "Lancelot": "Knight"}
        life_of_brian = {"Brian": "Lead", "Reg": "Support"}
        people2 = {**python, **holy_grail, **life_of_brian}
        print(people2)  # Output: {"Guido": 60, "Van Rossum": 65, "Arthur": "King", "Lancelot": "Knight", "Brian": "Lead", "Reg": "Support"}
        ```

* **Khi kết hợp các dictionaries, thứ tự của các phần tử có thể không được giữ nguyên.** Có thể sử dụng hàm `sorted()` để sắp xếp các key hoặc các item (key-value pairs).
    * Ví dụ sắp xếp các cặp khóa-giá trị:
      ```python
      people = {"Alice": 25, "Bob": 30, "Charlie": 35}
      sorted_people = sorted(people.items())
      print(sorted_people)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
      ```

* **Để tính tổng các giá trị** trong một dictionary, có thể sử dụng phương thức `.values()` để lấy các giá trị và sau đó sử dụng hàm `sum()`.
    * Ví dụ tính tổng các giá trị:
      ```python
      people = {"Alice": 25, "Bob": 30, "Charlie": 35}
      total_age = sum(people.values())
      print(total_age)  # Output: 90
      ```
    * **Lưu ý**: Phương pháp này sẽ không hoạt động nếu một trong các giá trị là string.
      * Ví dụ:
        ```python
        people = {"Alice": "twenty-five", "Bob": 30, "Charlie": 35}
        total_age = sum(people.values())  # Gây lỗi TypeError
        ```

* **Lựa chọn phương pháp kết hợp dictionaries:**
    * **Nếu chỉ có hai dictionaries, phương thức `.update()` là đủ.**
      * Ví dụ:
        ```python
        people = {"Alice": 25, "Bob": 30}
        python = {"Guido": 60}
        people.update(python)
        print(people)  # Output: {"Alice": 25, "Bob": 30, "Guido": 60}
        ```
    * **Nếu có nhiều hơn hai dictionaries, cả phương pháp comprehension và unpacking đều là các lựa chọn tốt.**
      * Ví dụ sử dụng phương pháp unpacking:
        ```python
        python = {"Guido": 60}
        holy_grail = {"Arthur": "King", "Lancelot": "Knight"}
        life_of_brian = {"Brian": "Lead"}
        combined = {**python, **holy_grail, **life_of_brian}
        print(combined)  # Output: {"Guido": 60, "Arthur": "King", "Lancelot": "Knight", "Brian": "Lead"}
        ```