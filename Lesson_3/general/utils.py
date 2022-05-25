# Утилиты нашего приложения

import json
from variables import MAX_PACKAGE_LENGTH, ENCODING

def get_message(client):
    # Принимаем сообщение в байтах
    encoded_response = client.rev(MAX_PACKAGE_LENGTH)
    # Делаем валидацию, если все корректно тогда возвращаем словарь
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        if isinstance(json_response, str):
            response = json.loads(json_response) # тут мы из получаем словарь из строки
            if isinstance(response, dict):
                return response # тут наоборот возвращаем словарь
            raise ValueError
        raise ValueError
    raise ValueError


def send_message(sock, message):
    if not isinstance(message, dict):
        raise TypeError
    message_js = json.dumps(message)
    encoded_message = message_js.encode(ENCODING)
    sock.send(encoded_message)
