# Наш сервак


import sys
import json
import socket
from general.variables import *
from general.utils import get_message, send_message


def client_message(mess):
    instructions = ACTION in mess and mess[ACTION] == PRESENCE and TIME in mess and USER in mess and mess[USER][
        ACCOUNT_NAME] == 'Larin'
    if instructions:
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad request',
    }


def ans():
    try:
        if '-p' in sys.argv:
            listening_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listening_port = DEFAULT_PORT
        if listening_port < 1024 or listening_port > 65535:
            raise ValueError
    except IndexError:
        print('Не указан номер порта после параметра: - \'\'!')

    try:
        if '-a' in sys.argv:
            listening_ip = sys.argv[sys.argv.index('-a') +1]
        else:
            listening_ip = ''
    except IndexError:
        print('Необходимо указать адрес после параметра -a, который сервер будет слушать')

    endure = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endure.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    endure.bind((listening_ip, listening_port))
    endure.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = endure.accept()
        try:
            message_client = get_message(client)
            print(message_client)
            response = client_message(message_client)
            send_message(client, response)
            client.close() # обязательно закрываем!
        except (ValueError, json.JSONDecodeError):
            print('Некорректное сообщение')
            client.close()

if __name__ == '__main__':
    ans()
