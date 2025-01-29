
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))
# Từ danh sách trên, điền vào một danh sách (friends_list) một cách phù hợp
# với tên của tất cả bạn bè. Mỗi người một "vị trí"
# bạn có thể cần chạy cùng một lệnh nhiều lần
# sử dụng lệnh print() để thực hiện từng bước trong bài tập này

