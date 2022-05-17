# Задание №1.3

def get_bites(data):
    try:
        data_bites = eval(f'b"{data}"')
        return data_bites
    except SyntaxError:
        return 'не могу записать в виде байтов'


data_for_bites = ['attribute', 'класс', 'функция', 'type']
for data in data_for_bites:
    print(f'{data} - {get_bites(data)}')
