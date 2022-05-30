import unittest
import os
import sys
sys.path.insert(os.path.join(os.getcwd(), '..'))
from client import create
from client import ans


from general.variables import ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR


class ClientTest(unittest.TestCase):
    def test_presence(self):
        test = create()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}})

    def test_no_action(self):
        test = create()
        test[TIME] = 1.1
        self.assertNotEqual(test, {ACTION: 'No action', TIME: 1.1, USER: {ACCOUNT_NAME: 'Larin'}})

    def test_presence_dict(self):
        # Проверка типа возвращаемых данных - должны быть словари
        test = create()
        self.assertIsInstance(test, dict)
        self.assertIsInstance(test[USER], dict)

    def test_account_name(self):
        # Проверка наличие ключа ACCOUNT_NAME
        test = create()
        self.assertTrue(test.get(USER).get(ACCOUNT_NAME))

    def test_with_acoount_name(self):
        # Проверка работоспособности функции с параметром
        user_name = 'test'
        test = create(account_name=user_name)
        self.assertEqual(test.get(USER).get(ACCOUNT_NAME), user_name)

    def test_time_type(self):
        # Проверка типа данные в TIME - должен быть float для time()
        test = create()
        self.assertIsInstance(test[TIME], float)

    def test_200_ans(self):
        self.assertEqual(ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        self.assertEqual(ans({RESPONSE: 400, ERROR: 'very bad request'}), '400 : very bad request')

    def test_no_response(self):
        self.assertRaises(ValueError, ans, {ERROR: 'very bad request'})


if __name__ == '__main__':
    unittest.main()
