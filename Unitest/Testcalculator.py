import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(4, 3)
        self.assertEqual(answer, 7)

    def test_deduction(self):
        answer = self.calc.diduction(4, 3)
        self.assertEqual(answer, 1)

    def test_multiplication(self):
        answer = self.calc.multiplication(4, 3)
        self.assertEqual(answer, 12)

    def test_division(self):
        answer = self.calc.division(12, 3)
        self.assertEqual(answer, 4)

    if __name__ == "__main__":
        unittest.main()
