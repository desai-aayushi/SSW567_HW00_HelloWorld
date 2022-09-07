import unittest

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(3,3,'three equals three')  # add assertion here

if __name__ == '__main__':
    unittest.main()
