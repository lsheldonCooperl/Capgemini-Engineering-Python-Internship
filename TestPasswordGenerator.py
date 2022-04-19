import unittest

from PasswordGenerator import *
class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_LowerUpperChecker(self):
        self.assertTrue(push('qQr','4') in ['4qQr','q4Qr','qQ4r','qQr4'])

if __name__=="__main__":
    unittest.main()
