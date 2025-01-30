#Dự án Euler #4 - số palindrome lớn nhất của hai số có 3 chữ số
#số palindrome là số đọc xuôi ngược đều giống nhau, như 101 hoặc 990099

import time 

#Hàm kiểm tra xem một số có phải là palindrome không
def is_palindrome(val):
   val = str(val) #chuyển số thành chuỗi
   if val == val[::-1]: #so sánh chuỗi gốc với chuỗi đảo ngược
       return(True)
   else:
       return(False)

#Cách viết ngắn gọn hơn cho hàm is_palindrome        
#def is_palindrome(val):
#   return str(val) == str(val)[::-1]

#Hàm tạo palindrome từ các chữ số riêng lẻ
def palindrome_create():
   nums=('9','8','7','6','5','4','3','2','1','0') #tạo list các chữ số dưới dạng chuỗi 
   iterations = 0 #biến đếm số lần lặp
   
   for dig1 in range(10):
       for dig2 in range(10):
           for dig3 in range(10):
               #tạo chuỗi palindrome bằng cách ghép các chữ số
               pal_str = nums[dig1] + nums[dig2] + nums[dig3] + nums[dig3] + nums[dig2] +nums[dig1]  
               palindrome = int(pal_str) #chuyển chuỗi thành số nguyên
               
               #giới hạn dưới để kiểm tra các ước số
               low_val = int(palindrome/999) 
               #giới hạn trên là căn bậc hai của palindrome
               high_val = int(palindrome**0.5) + 1
               
               #kiểm tra xem palindrome có chia hết cho số nào trong khoảng không
               for digit in range(low_val,high_val):
                   iterations += 1
                   if palindrome % digit == 0: #nếu tìm thấy ước số
                       return 'palindrome:', palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations

#Hàm tạo palindrome bằng cách tính giá trị hàng chữ số
def palindrome_create2():
   iterations = 0
   
   for dig1 in range(9,0,-1):
       for dig2 in range(9,-1,-1):
           for dig3 in range(9,-1,-1):
               #tạo palindrome bằng phép tính với giá trị hàng
               palindrome = dig1*100000 + dig2*10000 + dig3*1000 + dig3*100 + dig2*10 + dig1
               
               low_val = int(palindrome/999)
               high_val = int(palindrome**0.5)+1
               for digit in range(low_val,high_val):
                   iterations += 1
                   if palindrome % digit == 0:
                       return 'palindrome:',palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations

#Chạy thử nghiệm hai hàm mới
for func in ['palindrome_create','palindrome_create2']:
   runs = 10
   start = time.time() 
   for run in range(runs):
       return_value = locals()[func]()
       end =time.time()
   print(return_value, 'Average run-time:', (end-start)/runs)

# So sánh hiệu năng các phương pháp:
# Phương pháp 1: 110 giây - x1 lần        - phương pháp tổng quát
# Phương pháp 1 với tìm kiếm một nửa: 55 giây - x2 lần     - phương pháp tổng quát 
# Phương pháp 2 ngược với giới hạn: 0.6 giây - ~150-180x    - phương pháp tổng quát
# Phương pháp 3,4 tạo ngược: 0.06 giây - ~1500-1800x       - số được hardcode, có thể tổng quát hóa

# Điểm khác biệt chính:
# 1. Code mới sử dụng phương pháp tạo palindrome trực tiếp thay vì tìm kiếm
# 2. palindrome_create() tạo số bằng cách ghép chuỗi
# 3. palindrome_create2() tạo số bằng phép tính với giá trị hàng
# 4. Code mới nhanh hơn nhiều (~1500-1800 lần) nhưng ít linh hoạt hơn do được tối ưu riêng cho số 3 chữ số
# 5. Code cũ tổng quát hơn, có thể dùng cho mọi độ dài số