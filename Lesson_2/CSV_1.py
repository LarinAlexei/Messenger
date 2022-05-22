# Задание №1

from chardet import detect
import re
import csv

file_name_list = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt',
]

get_file = [
    'Изготовитель системы',
    'Название OC',
    'Код продукта',
    'Тип системы',
]


def get_data():
    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file_names in file_name_list:
        with open(file_names, 'rb') as f:
            encoding = detect(f.read())['encoding']
            f.seek(0)
            content = f.read().decode(encoding=encoding)

        def values_field(field_names):
            field_names = re.escape(field_names)
            pattern = rf'{field_names}:(?:\W+)(.*?)\r'
            result = re.search(pattern, content, re.IGNORECASE)
            return result.groups()[0].strip() if result else None

        os_prod_list.append(values_field('Название OC'))
        os_name_list.append(values_field('Изготовитель системы'))
        os_code_list.append(values_field('Код продукта'))
        os_type_list.append(values_field('Тип системы'))
        main_data = [get_file, *zip(os_prod_list, os_name_list, os_code_list, os_type_list)]
    return main_data if main_data else None


def write_to_csv(fpath):
    data = get_data()
    if not data:
        return 'Данные не получены'
    with open(fpath, 'w', encoding='utf-8', newline='') as f:
        files_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        files_writer.writerows(data)


write_to_csv('task_1_write.csv')
