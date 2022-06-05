import unittest

from C4_PC_1 import *


class TestPlace(unittest.TestCase):
    def setUp(self) -> None:
        print("test setup")

    def tearDown(self) -> None:
        print("tear down")

    def test0(self):
        self.assertEqual(main_func("2 12 13 23 31 34 41"), 25)

    def test1(self):
        self.assertEqual(main_func("1 12 23 34 11 21 32 45 53 95 43 99 29 91"), 5)

    def test2(self):
        self.assertEqual(main_func("3 12 23 34 41 31 52 45 61 14 21 33 55 13 54 32 56 36"), 49)

    def test3(self):
        self.assertEqual(main_func("1 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78"), 10)

    def test4(self):
        self.assertEqual(main_func("2 12 11 33 34 43 55 52 41 31 25 88 79 98 45 13 42 87 35 51 21 14 78"), 50)

    def test5(self):
        self.assertEqual(main_func("1 12 31 41 42 43 45 51 63 64 56 16"), 0)

    def test6(self):
        self.assertEqual(main_func("2 12 13 22 23 24 34 42 98 71 87 17 96 67"), 42)

    def test7(self):
        self.assertEqual(main_func("3 12 14 21 24 25 32 41 43 59 65 91 87 76 95"), 24)

    def test8(self):
        self.assertEqual(main_func("2 11 12 14 15 23 25 31 43 45 51 52 68 79 87 89"), 52)

    def test9(self):
        self.assertEqual(main_func("3 55 77 45 54"), 6)


if __name__ == '__main__':
    unittest.main()
