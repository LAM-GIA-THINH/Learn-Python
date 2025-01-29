# Đoán số chính xác trong 3 lần đoán. Nếu bạn không đoán đúng sau 3 lần đoán, bạn sẽ thua cuộc.
# Cung cấp hộp nhập liệu cho người dùng: 1. Để ghi nhận các lần đoán,
# in (và hộp nhập liệu) 1. Nếu người dùng thắng 2. Nếu người dùng thua
# Mẹo: (nhớ rằng bạn sẽ không thấy các câu lệnh in trong quá trình thực thi, vì vậy nếu bạn muốn xem các bản in trong vòng lặp, hãy in vào hộp nhập liệu)

# Sửa đổi 1: số từ 1-100, thông báo cho người dùng nếu đoán quá cao/thấp và cho họ 5-10 lần đoán.
# Mẹo: (nhớ rằng bạn sẽ không thấy các câu lệnh in trong quá trình thực thi, vì vậy nếu bạn muốn xem các bản in trong vòng lặp, hãy in vào hộp nhập liệu (Điều này cụ thể cho nền tảng này)
# Ba câu hỏi về vòng lặp:
# 1. Tôi muốn lặp lại điều gì?
#  -> các tiên đoán
# 2. Tôi muốn thay đổi điều gì mỗi lần?
#  -> số lần đoán và số đoán
# 3. Chúng ta nên lặp lại trong bao lâu?
#  -> cho đến khi bạn thua/thắng hoặc hết dự đoán
print('Guessing game') 
num = 76
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-100: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')