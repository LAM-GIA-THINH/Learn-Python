def enigma_light(): 
    # tạo chuỗi keys
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # tự động tạo chuỗi values bằng cách dịch chuyển chuỗi gốc
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
    # tạo hai từ điển
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    # HOẶC tạo 1 từ điển rồi đảo ngược nó
    #dict_e = dict(zip(keys,values))
    #dict_d = {value:key for key, value in dict_e.items()}
    # nhập 'thông điệp' và chế độ từ người dùng
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
    # chạy mã hóa hoặc giải mã
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()
# trả về kết quả
# làm sạch và làm đẹp mã

print(enigma_light())