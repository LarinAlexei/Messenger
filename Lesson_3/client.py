# Наш клиент


import socket
import sys
import json
import time
from general.variables import *
from general.utils import send_message, get_message


def create(account='Larin'):
    out_data = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account
        }
    }
    return out_data

def ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: yes'
        return f'500: {message[ERROR]}'
    raise ValueError


def important():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_address
        server_port = DEFAULT_PORT
    except ValueError:
        print('Порт указывается от 1024 до 65535')
        sys.exit(1)

    endure = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    endure.connect((server_address, server_port))
    mess_server = create()
    send_message(endure, mess_server)

    try:
        answer = ans(get_message(endure))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Сооббщение не декодировано')


if __name__ == '__main__':
    important()
