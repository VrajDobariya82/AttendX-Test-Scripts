import unittest

def login(username, password):
    return username == "student01" and password == "test123"

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        self.assertTrue(login("student01", "test123"))

    def test_invalid_password(self):
        self.assertFalse(login("student01", "wrong123"))

    def test_invalid_username(self):
        self.assertFalse(login("wronguser", "test123"))

if __name__ == "__main__":
    unittest.main()