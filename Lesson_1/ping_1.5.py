# Задание №1.5

import chardet
import subprocess
import platform


def ping(url, num_ping=5):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, str(num_ping), url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for meaning in process.stdout:
        result = chardet.detect(meaning)
        meaning = meaning.decode(result['encoding']).encode('utf-8')
        print(meaning.decode('utf-8'), end='')


ping('yandex.ru', 5)
ping('youtube.com', 5)
