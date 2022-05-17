# Задание №1.4

def decode_encode_data(data):
    encode_data = data.encode('utf-8')
    decode_data = encode_data.decode('utf-8')
    return f'{data} --> {encode_data} --> {decode_data}'


list_data = ['разработка', 'администрирование', 'protocol', 'standard']
for i in list_data:
    print(decode_encode_data(i))
