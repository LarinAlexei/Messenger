import sys
import os
import unittest
from Lesson_3.general.variables import ACTION, ACCOUNT_NAME, RESPONSE, ENCODING, PRESENCE, ERROR, TIME, USER
from Lesson_3.server import client_message

sys.path.insert(0, os.path.join(os.getcwd(), '..'))


# Тустируем сервер
class ServerTest(unittest.TestCase):
    ok_dict = {
        RESPONSE: 200,
    }

    err_dict = {
        RESPONSE: 400,
        ERROR: 'very bad request'
    }

# Проверяем корректность запроса
    def test_check(self):
        self.assertEqual(
            client_message(
                {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}}
            ), self.ok_dict
        )

    def test_no_action(self):
        self.assertEqual(
            client_message(
                {TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}}
            ), self.err_dict
        )

    def test_no_time(self):
        self.assertEqual(
            client_message(
                {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Larin'}}
            ), self.err_dict
        )

    def test_wrong_action(self):
        self.assertEqual(
            client_message(
                {ACTION: 'no action', TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}}
            ), self.err_dict
        )

# Проверяем имя пользователя
    def test_account_name(self):
        self.assertEqual(
            client_message(
                {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'wrong name'}}
            ), self.err_dict
        )

# Проверяем вернется ли словарь при 200 и 400
    def test_response_dict(self):
        self.assertIsInstance(
            client_message(
                {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}}
            ), dict
        )
        self.assertIsInstance(
            client_message(
                {ACTION: PRESENCE, }
            ), dict
        )

# Проверка если в функцию не передали параметр
    def test_response_empty_param(self):
        with self.assertRaises(TypeError):
            client_message()


if __name__ == '__main__':
    unittest.main()