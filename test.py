from unittest import TestCase
from main import auth_with_login_email
from test_dataset import dataset
from check_phone import check_phone_number


class TestYandex(TestCase):

    def test_ya_login(self):
        for item in dataset:
            expected = check_phone_number(item['phone'])
            result = auth_with_login_email(item['user'], item['pass'])
            self.assert_(result, expected)

