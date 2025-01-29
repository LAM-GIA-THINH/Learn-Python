1. **Sự khác biệt giữa phương thức `sort()` và hàm `sorted()`**:
    ```python
    # Sử dụng phương thức sort()
    my_list = [3, 1, 4, 1, 5, 9]
    my_list.sort()  # Sắp xếp trực tiếp list
    print(my_list)  # Output: [1, 1, 3, 4, 5, 9]

    # Sử dụng hàm sorted()
    my_tuple = (3, 1, 4, 1, 5, 9)
    sorted_tuple = sorted(my_tuple)  # Trả về list mới đã sắp xếp
    print(sorted_tuple)  # Output: [1, 1, 3, 4, 5, 9]
    print(my_tuple)  # Output: (3, 1, 4, 1, 5, 9) (không thay đổi tuple ban đầu)
    ```

2. **Tính chất mutable và immutable**:
    ```python
    # Mutable object
    my_list = [3, 1, 4, 1, 5, 9]
    my_list.sort()  # Sắp xếp list trực tiếp
    print(my_list)  # Output: [1, 1, 3, 4, 5, 9]

    # Immutable object (Không thể dùng .sort())
    my_string = "hello"
    # my_string.sort()  # Lỗi: 'str' object has no attribute 'sort'
    sorted_string = sorted(my_string)  # Trả về list đã sắp xếp
    print(sorted_string)  # Output: ['e', 'h', 'l', 'l', 'o']
    ```

3. **Sắp xếp các kiểu dữ liệu khác nhau**:
    ```python
    # Sắp xếp tuple (kết quả là list)
    my_tuple = (3, 1, 4, 1, 5, 9)
    sorted_tuple = sorted(my_tuple)
    print(sorted_tuple)  # Output: [1, 1, 3, 4, 5, 9]

    # Sắp xếp dictionary theo keys
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    sorted_keys = sorted(my_dict)
    print(sorted_keys)  # Output: ['a', 'b', 'c']

    # Sắp xếp dictionary theo values
    sorted_by_values = sorted(my_dict.items(), key=lambda x: x[1])
    print(sorted_by_values)  # Output: [('a', 1), ('b', 2), ('c', 3)]
    ```

4. **Sắp xếp đảo ngược**:
    ```python
    # Sắp xếp đảo ngược bằng reverse=True
    my_list = [3, 1, 4, 1, 5, 9]
    my_list.sort(reverse=True)
    print(my_list)  # Output: [9, 5, 4, 3, 1, 1]

    # Sắp xếp đảo ngược bằng sorted()
    my_list = [3, 1, 4, 1, 5, 9]
    sorted_list = sorted(my_list, reverse=True)
    print(sorted_list)  # Output: [9, 5, 4, 3, 1, 1]

    # Sử dụng phương thức reverse() (chỉ đảo ngược, không sắp xếp)
    my_list.reverse()
    print(my_list)  # Output: [9, 5, 1, 4, 1, 3]
    ```

5. **Sử dụng tham số `key`**:
    ```python
    # Sắp xếp theo giá trị tuyệt đối
    my_list = [-3, 1, -4, 1, 5, 9]
    my_list.sort(key=abs)  # Sắp xếp theo giá trị tuyệt đối
    print(my_list)  # Output: [1, 1, -3, -4, 5, 9]

    # Sắp xếp một list các list con theo index thứ 1 trong mỗi list con
    my_list_of_lists = [[1, 2], [3, 1], [5, 0]]
    my_list_of_lists.sort(key=lambda x: x[1])  # Sắp xếp theo phần tử ở index 1
    print(my_list_of_lists)  # Output: [[5, 0], [3, 1], [1, 2]]
    ```

6. **Reversed Object**:
    ```python
    my_list = [1, 2, 3, 4, 5]
    reversed_object = reversed(my_list)
    print(list(reversed_object))  # Output: [5, 4, 3, 2, 1]
    ```

7. **Slicing**:
    ```python
    my_list = [1, 2, 3, 4, 5]
    reversed_list = my_list[::-1]
    print(reversed_list)  # Output: [5, 4, 3, 2, 1]
    ```
