# Math Tutor - Dự án
# Bảng cửu chương
# Mục tiêu: Tạo ứng dụng để luyện tập bảng cửu chương

# Người dùng xác định số lượng câu hỏi luyện tập ngẫu nhiên
# Người dùng được hiển thị câu hỏi ví dụ: 5 X 5 = và nhập câu trả lời cho từng câu hỏi
# Khi tất cả câu hỏi được trả lời: in ra các thông tin sau
# a. Một dạng 'lời cảm ơn đã tham gia'
# b. Số câu trả lời đúng/tổng số câu hỏi
# c. Phần trăm chính xác

# Sử dụng các dòng khác nhau tùy ý.
# Lưu ý \n (xuống dòng) hoặc "" không hoạt động đúng với Brython
# Bonus 1: đồng thời đo/hiển thị thời gian để trả lời câu hỏi: tổng thời gian và thời gian cho mỗi câu
# Bonus 2: cho phép người dùng xác định các số được sử dụng cao đến đâu
# Bonus 3: hiển thị tất cả câu hỏi và câu trả lời ở cuối

#nhập các modules
from random import randrange as r
from time import time as t

# hỏi người dùng muốn bao nhiêu câu hỏi
no_questions = int(input('How many questions do you want?: '))
max_num =int(input('Highest number used in practice?: '))

#đặt điểm bắt đầu là số không
score = 0
answer_list = []

#lặp qua số lượng câu hỏi
start = t()
for q in range(no_questions):
    num1,num2 = r(1,max_num+1),r(1,max_num+1)
    ans = num1 * num2
    u_ans =int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
    if u_ans == ans:
        score += 1
    end = t()

print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_questions,1)}seconds/question)')
for a in answer_list:
    print(a)

# tạo hai số ngẫu nhiên và tính kết quả
# hiển thị câu hỏi cho người dùng
# ghi nhận câu trả lời và sửa đổi điểm người dùng 
# xuất điểm cuối cùng