# Задание №1.6

import chardet

def open_encoding(file_open):
    try:
        with open(file_open, 'rb') as f:
            meaning = f.readline()
        return chardet.detect(meaning)['encoding']
    except FileNotFoundError:
        print(f'Файл {file_open} не был найден')
        return None


def meaning_print(file_open):
    encoding = open_encoding(file_open)
    if encoding:
        print(f'Кодировка файла: {encoding}')
        with open(file_open, 'r', encoding=encoding) as f:
            for meaning in f:
                print(meaning, end='')


meaning_print('text_file.txt')
