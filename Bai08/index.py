# **Python 101: Bài tập chuỗi 1**

# 1. Từ chuỗi “Welcome to Python 101: Strings”, trích xuất văn bản và tạo/in ra một chuỗi mới có nội dung:  
#    - “1 Welcome Ring To Tyler”  
#    - Mỗi chữ cái đầu trong từ phải viết hoa (dạng `title format`).  

# 2. In chuỗi vừa rồi theo thứ tự ngược lại.  
#    Gợi ý: Google sẽ là bạn của bạn...
msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title())