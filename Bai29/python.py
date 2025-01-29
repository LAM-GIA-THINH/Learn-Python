
i = 0  # Khởi tạo biến i với giá trị 0
while i < 5:  # Lặp lại vòng lặp khi i nhỏ hơn 5
    i += 1  # Tăng giá trị của i lên 1 ở mỗi vòng lặp
    print(f"{i}." + "*"*i + "Loops are awesome" + "*"*i*2)  
    # In ra i, sau đó là một chuỗi dấu * số lần bằng giá trị của i, rồi đến câu "Loops are awesome", 
    # và cuối cùng là dấu * với số lần gấp đôi giá trị của i

# 1.*Loops are awesome**
# 2.**Loops are awesome****
# 3.***Loops are awesome******
# 4.****Loops are awesome********
# 5.*****Loops are awesome**********
