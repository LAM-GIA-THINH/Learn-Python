# Bài tập 1: Sử dụng lambda để thực hiện các thao tác đơn giản
# 1. Viết một lambda function cộng thêm 5 vào một số.
# 2. Viết một lambda function loại bỏ khoảng trắng trong chuỗi.
# 3. Nhập một chuỗi và một số, sử dụng lambda để thực hiện các thao tác này.
add_five = lambda x: x + 5
remove_spaces = lambda s: s.replace(" ", "")
number = int(input("Nhập một số: "))
string = input("Nhập một chuỗi: ")
print("Kết quả cộng thêm 5:", add_five(number))
print("Chuỗi sau khi loại bỏ khoảng trắng:", remove_spaces(string))

# Bài tập 2: Kết hợp hai danh sách và loại bỏ các phần tử trùng lặp
# 1. Cho hai danh sách list1 = [1, 2, 3, 4] và list2 = [3, 4, 5, 6].
# 2. Sử dụng lambda để kết hợp hai danh sách và loại bỏ các phần tử trùng lặp.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merge_and_dedup = lambda l1, l2: list(set(l1 + l2))
result = merge_and_dedup(list1, list2)
print("Kết quả kết hợp và loại bỏ trùng lặp:", result)

# Bài tập 3: Sắp xếp danh sách theo các tiêu chí khác nhau
# 1. Cho danh sách players = [{"name": "Alice", "score": 15}, {"name": "Bob", "score": 20}, {"name": "Charlie", "score": 10}].
# 2. Sắp xếp danh sách theo thứ tự điểm từ cao đến thấp bằng lambda.
# 3. Cho danh sách ID ids = ["ID123", "ID45", "ID9", "ID100"].
# 4. Sắp xếp danh sách ID theo số cuối trong ID.
players = [{"name": "Alice", "score": 15}, {"name": "Bob", "score": 20}, {"name": "Charlie", "score": 10}]
sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)
print("Danh sách sắp xếp theo điểm số:", sorted_players)

ids = ["ID123", "ID45", "ID9", "ID100"]
sorted_ids = sorted(ids, key=lambda ID: int(ID[2:]))
print("Danh sách ID đã sắp xếp:", sorted_ids)
