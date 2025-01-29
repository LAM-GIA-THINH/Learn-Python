```python
# Mục đích: Hàm enumerate được dùng để đánh số thứ tự các phần tử trong một chuỗi (ví dụ: list, tuple, string).
friends = ["Brian", "Judith", "Robert", "Jane", "Michael"]
for index, name in enumerate(friends):  # enumerate tự động đánh số thứ tự cho phần tử
    print(index, name)  # In số thứ tự và tên
    # Output: 
    # 0 Brian
    # 1 Judith
    # 2 Robert
    # 3 Jane
    # 4 Michael
```

```python
# Cách hoạt động: Hàm enumerate biến mỗi phần tử trong chuỗi thành một tuple, 
# trong đó phần tử đầu tiên là số thứ tự (bắt đầu từ 0 theo mặc định), và phần tử thứ hai là giá trị của phần tử đó.
for index, name in enumerate(friends):
    print((index, name))  # In tuple chứa số thứ tự và giá trị phần tử
    # Output:
    # (0, 'Brian')
    # (1, 'Judith')
    # (2, 'Robert')
    # (3, 'Jane')
    # (4, 'Michael')
```

```python
# Cú pháp: enumerate(iterable) trả về một đối tượng enumerate với số thứ tự bắt đầu từ 0.
for index, name in enumerate(friends):
    print(index, name)  # Mặc định số thứ tự bắt đầu từ 0
    # Output: 
    # 0 Brian
    # 1 Judith
    # 2 Robert
    # 3 Jane
    # 4 Michael
```

```python
# Cú pháp: enumerate(iterable, start) trả về một đối tượng enumerate với số thứ tự bắt đầu từ giá trị start.
for index, name in enumerate(friends, 1):  # Bắt đầu số thứ tự từ 1
    print(index, name)
    # Output: 
    # 1 Brian
    # 2 Judith
    # 3 Robert
    # 4 Jane
    # 5 Michael
```

```python
# Ứng dụng: In danh sách có đánh số thứ tự: 
# Với enumerate, bạn có thể dễ dàng in danh sách kèm theo số thứ tự mà không cần phải tự tạo biến đếm.
for index, name in enumerate(friends, 1):
    print(f"{index}. {name}")  # In danh sách kèm số thứ tự
    # Output:
    # 1. Brian
    # 2. Judith
    # 3. Robert
    # 4. Jane
    # 5. Michael
```

```python
# Ứng dụng: Truy cập và sửa đổi phần tử: Khi cần vừa truy cập phần tử, vừa cần biết vị trí của nó trong chuỗi,
# enumerate sẽ rất hữu ích khi cần thay đổi giá trị tại một vị trí cụ thể.
for index, name in enumerate(friends):
    if index == 2:
        friends[index] = "Charlie"  # Thay đổi tên ở vị trí 2
print(friends)  # In lại danh sách bạn bè sau khi thay đổi
# Output:
# ['Brian', 'Judith', 'Charlie', 'Jane', 'Michael']
```

```python
# Lưu ý: enumerate không có ý nghĩa nhiều đối với dictionaries và sets vì chúng không phải là các chuỗi có thứ tự.
# Ví dụ: Dùng enumerate với dictionary, nhưng không có thứ tự
friends_dict = {"Brian": 30, "Judith": 25, "Robert": 40}
for index, (name, age) in enumerate(friends_dict.items()):  # enumerate dùng cho dictionary
    print(index, name, age)
    # Output: 
    # 0 Brian 30
    # 1 Judith 25
    # 2 Robert 40
```

```python
# Các ví dụ nâng cao: Có thể kết hợp enumerate với các vòng lặp để in ra cả số thứ tự và giá trị của phần tử.
for index, name in enumerate(friends, 1):
    print(f"Index {index} is {name}")
    # Output: 
    # Index 1 is Brian
    # Index 2 is Judith
    # Index 3 is Robert
    # Index 4 is Jane
    # Index 5 is Michael
```

```python
# Ví dụ nâng cao: Sử dụng enumerate lồng nhau để đánh số thứ tự cho các tuple
nested_list = [["apple", "banana"], ["cat", "dog"], ["car", "bike"]]
for outer_index, inner_list in enumerate(nested_list, 1):
    print(f"Group {outer_index}:")
    for inner_index, item in enumerate(inner_list, 1):
        print(f"  {inner_index}. {item}")
    # Output:
    # Group 1:
    #   1. apple
    #   2. banana
    # Group 2:
    #   1. cat
    #   2. dog
    # Group 3:
    #   1. car
    #   2. bike
```

```python
# Ví dụ nâng cao: Sử dụng start với giá trị khác 0 để bắt đầu số thứ tự từ một giá trị mong muốn.
for index, name in enumerate(friends, start=100):  # Bắt đầu số thứ tự từ 100
    print(f"{index}. {name}")
    # Output: 
    # 100. Brian
    # 101. Judith
    # 102. Robert
    # 103. Jane
    # 104. Michael
```