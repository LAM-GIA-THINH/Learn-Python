# Tách chuỗi và ghép chuỗi trong Python - Ví dụ
#=============================================

# 1. Tách chuỗi (split):
# Tách theo khoảng trắng (mặc định)
text = "Hello World Python Programming"
words = text.split()  # ['Hello', 'World', 'Python', 'Programming']
print(words)

# Tách theo dấu phẩy
text = "apple,banana,orange,grape"
fruits = text.split(',')  # ['apple', 'banana', 'orange', 'grape'] 
print(fruits)

# Tách với khoảng trắng thừa
text = "  Hello   World  "
words = text.split()  # ['Hello', 'World']
print(words)

# Tách theo ký tự cụ thể với khoảng trắng
text = "a , b ,c,  d"
items = text.split(',')  # ['a ', ' b ', 'c', '  d']
print(items)

# 2. Ghép chuỗi (join):
# Ghép bằng dấu gạch ngang
words = ['Hello', 'World', 'Python']
text = '-'.join(words)  # 'Hello-World-Python'
print(text)

# Ghép nhiều lần
words = ['a', 'b', 'c']
text = '--'.join(words)  # 'a--b--c'
print(text)

# Ghép với chuỗi rỗng
words = ['H', 'e', 'l', 'l', 'o']
text = ''.join(words)  # 'Hello'
print(text)

# 3. Ứng dụng:
# Xử lý khoảng trắng thừa bằng split() và join()
text = "  Hello     World  Python  "
clean_text = ' '.join(text.split())  # 'Hello World Python'
print(clean_text)

# Xử lý khoảng trắng thừa bằng replace()
text = "  Hello     World  Python  "
clean_text = text.replace(" ", "")  # 'HelloWorldPython'
print(clean_text)