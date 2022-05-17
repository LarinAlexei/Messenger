# Задание №1.1

def get_info(data):
    for i in data:
        print(f'Тип: {type(i)} Значение: {i}')


# Наши исходные данные
data_str = ['разработка', 'сокет', 'декоратор']

# Используем конвертер https://calcsbox.com/post/konverter-teksta-v-unikod.html
unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                '\u0441\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

# Вывод
print('Результат значений:')
get_info(data_str)

print('Результат в unicode:')
get_info(unicode)
