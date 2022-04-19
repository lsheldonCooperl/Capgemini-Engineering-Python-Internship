import unittest

from PasswordChecker import *
class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_LowerUpperChecker(self):
        self.assertEqual(LowerUpperChecker('qQ'),1)

    def test_DigitChecker(self):
        self.assertEqual(DigitChecker('qq'),0)

    def test_PunctuationCharChecker(self):
        self.assertEqual(PunctuationCharChecker('qQ'),0)

    def test_LengthChecker(self):
        self.assertEqual(LengthChecker('q12ec21eCC///11Q'),1)

if __name__=="__main__":
    unittest.main()
