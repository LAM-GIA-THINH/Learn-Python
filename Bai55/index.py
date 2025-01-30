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

#Hàm tìm palindrome theo thứ tự từ thấp đến cao
def palindrome():
   start_time = time.time() #bắt đầu đếm thời gian
   palindromes_list=[] #danh sách các palindrome tìm được
   debug_list=[] #danh sách debug để theo dõi quá trình
   low_val =900 #giá trị thấp nhất cho số 3 chữ số
   high_val = 999 #giá trị cao nhất cho số 3 chữ số
   iterations = 0 #đếm số lần lặp
   
   #vòng lặp lồng nhau để thử tất cả các cặp số
   for num1 in range(low_val,high_val):
       for num2 in range(low_val,high_val):
           iterations += 1
           #print(num1,num2)
           if is_palindrome(num1*num2): #nếu tích là palindrome
               palindromes_list.append(num1*num2) #thêm vào danh sách
               debug_list.append([num1,num2,num1*num2])
           if num1 == num2: #tránh trùng lặp các cặp số
               break
               
   #In kết quả
   print('print of palindromes:',palindromes_list, num1, num2)
   print('debug_list:', debug_list)
   print('Iterations:' , iterations)
   print('Largest palindrome:', max(palindromes_list))
   print('Runtime:', time.time()-start_time)
   print('---------End Run--------')
   #110 giây, 55 giây

#Hàm tìm palindrome theo thứ tự từ cao xuống thấp - cách tối ưu hơn
def palindrome_back():
   start_time = time.time()
   palindromes_list=[]
   debug_list=[]
   low_val =500
   high_val = 2000
   iterations = 0
   low_num2_val =500
   
   #vòng lặp từ cao xuống thấp để tìm palindrome lớn nhất trước
   for num1 in range(high_val,low_val,-1):
       if num1 < low_val: #điều kiện dừng khi đã tìm thấy palindrome lớn nhất
           break
       for num2 in range(high_val,low_num2_val,-1):
           iterations += 1
           #print(num1,num2)
           if is_palindrome(num1*num2):
               palindromes_list.append(num1*num2)
               #cập nhật các giới hạn dựa trên palindrome đã tìm thấy
               low_val = max((num1*num2)/high_val,low_val)
               low_num2_val = num2
               debug_list.append([num1,num2,(num1*num2)/high_val,low_val])
           if num1 == num2:
               break
               
   #In kết quả
   print('print of palindromes:',palindromes_list, num1, num2)
   print('debug_list:', debug_list)
   print('Iterations:' , iterations)
   print('Largest palindrome:', max(palindromes_list))
   print('Runtime:', time.time()-start_time)
   print('---------End Run--------')
   #110 giây, 55 giây

#Chạy cả hai hàm để so sánh    
palindrome()
palindrome_back()