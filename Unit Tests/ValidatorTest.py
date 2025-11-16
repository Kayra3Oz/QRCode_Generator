import unittest
import Validator

class ValidatorTest(unittest.TestCase):
    def test_validate_valid_url_1(self):
        res = Validator.validate("https://google.com")
        self.assertTrue(res)

    def test_validate_valid_url_2(self):
        res = Validator.validate("http://google.de")
        self.assertTrue(res)

    def test_validate_valid_url_3(self):
        res = Validator.validate("https://www.google.com")
        self.assertTrue(res)

    def test_validate_invalid_url_1(self):
        res = Validator.validate("https://google.")
        self.assertFalse(res)

    def test_validate_invalid_url_2(self):
        res = Validator.validate("https:/google.com")
        self.assertFalse(res)

    def test_validate_invalid_url_3(self):
        res = Validator.validate("https//google.com")
        self.assertFalse(res)

    def test_validate_invalid_url_4(self):
        res = Validator.validate("htts://google.com")
        self.assertFalse(res)

if __name__ == '__main__':
        unittest.main()