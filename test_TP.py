
import os
import unittest
import unittest.mock as mock
import TP

class TestTP(unittest.TestCase):
    def test_grab(self):
        with mock.patch('builtins.input', side_effect=['<user_token>', '<channel_id>']):
            TP.grab()
            self.assertTrue(os.path.exists("output.csv"), "output.csv does not exist")
            os.remove("output.csv")
    def test_analyze(self):
        with mock.patch('builtins.input', side_effect=['<user_token>', '<channel_id']):
            TP.grab()
            TP.analyze()
            self.assertRaises(IndexError)
            self.assertRaises(FileNotFoundError)
            os.remove("output.csv")
            

if __name__ == '__main__':
    unittest.main() 