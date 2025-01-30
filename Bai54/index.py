# Tạo một trò chơi đặt cược bi:

# rút một viên bi từ túi (giả sử là ngẫu nhiên)
# một túi có 10 viên bi: 6 viên xanh lá và 4 viên đỏ
# nếu bạn rút được viên bi xanh lá, bạn thắng số tiền bằng số tiền đặt cược, nếu bạn rút được viên bi đỏ, bạn thua số tiền đặt cược.
# các viên bi được đặt lại vào túi sau mỗi vòng
# trước khi rút, quyết định số tiền bạn sẽ đặt cược và nhập vào
# bạn bắt đầu trò chơi với 1,000 đồng vàng hoặc $,£,€
# số lượng vòng/lần rút phải là biến
# nếu bạn thua một nửa số tiền của mình thì trò chơi kết thúc
# in/hiện thị dữ liệu khi bạn chơi
#Bonus:
# thay thế hai viên bi: 1 viên xanh lá bằng viên bi đen thắng 10X, 1 viên đỏ bằng viên bi xám thua 5X

import random 
#tạo túi với 10 viên bi
bag = ('green','green','green','green','green','black','red','red','red','white')

#số tiền ban đầu
start_purse = 1000

#số tiền hiện tại
purse = start_purse

#kết quả của vòng cuối
result = 0

#số lượng vòng
rounds = 3

#viên bi cuối cùng
marble = 'none'

#chào mừng người chơi vào trò chơi 
print(f'You start the game with {start_purse} gold pieces')

#vòng lặp rút bi
for draw in range(1,rounds+1):
   #đặt cược bao nhiêu
   bet = int(input(f'Current Purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: '))
   
   #rút bi
   marble = random.choice(bag)
   
   #thắng hay thua
   if marble == 'green':
       result = bet
   elif marble == 'black':
       result = 10 * bet
   elif marble == 'white':
       result = -5 * bet
   else:
       result = -bet
       
   #tính thắng thua/ kết quả và số tiền mới
   purse += result
   
   #thua cuộc nếu mất một nửa số tiền
   if purse < 0.5 * start_purse:
       print(f'Game over! You lost to much gold!!!')
       break
       
   #in kết quả
   print(f'purse: {purse}, last result: ({marble}): {result}')
   print('')

#in kết quả cuối cùng
print('starting/ ending purse: ', start_purse, '/',purse)
print('gain/loss: ', ((purse-start_purse)/start_purse *100),'%')