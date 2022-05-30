import os
import sys
import unittest
import json

sys.path.insert(os.path.join(os.getcwd(), '..'))
print(sys.path)

from general.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ENCODING
from general.utils import get_message, send_message


class TestSocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING) # Кодировка сообщения
        self.received_message = message_to_send # Отправляем в сокет

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 113.1131,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'very bad request'
    }

    def test_send_message_true(self):
        test_socket = TestSocket(self.test_dict_send) # Создание словаря (тест)
        send_message(test_socket, self.test_dict_send) # Вызов теста
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_with_error(self):
        test_socket = TestSocket(self.test_dict_send) # Тестовый словарь
        send_message(test_socket, self.test_dict_send) # Вызываем сам тест
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    def test_get_message(self):
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_error(self):
        test_sock_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
