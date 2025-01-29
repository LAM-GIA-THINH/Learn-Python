mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
# Tạo một máy tính có thể xử lý các phép tính +, -, *, / và đưa ra kết quả dựa trên chế độ/toán tử được sử dụng
# Gợi ý: Sử dụng 3 đầu vào riêng biệt
# Phần thưởng: Mở rộng chức năng bằng cách thêm chế độ chuyển đổi độ C sang độ F
# Công thức là: nhiệt độ C * 9/5 + 32 = nhiệt độ F
