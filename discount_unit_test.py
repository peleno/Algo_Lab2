import random
import unittest
from discount import count_min_sum

class MyTestCase(unittest.TestCase):
    def test_input1(self):
        prices = [50, 20, 30, 17, 100]
        discount = 10
        self.assertEqual(count_min_sum(prices, discount), 207.00)

    def test_input2(self):
        prices = [1, 2, 3, 4, 5, 6, 7]
        discount = 100
        self.assertEqual(count_min_sum(prices, discount), 15.00)

    def test_input3(self):
        prices = [1, 1, 1]
        discount = 33
        self.assertEqual(count_min_sum(prices, discount), 2.67)

    def test_any(self):
        goods_count = random.randint(1, 1000)
        prices = random.sample(range(1000000000), goods_count)
        discount_counts = len(prices) // 3
        discount = random.randint(0, 100)
        sorted_prices = sorted(prices, reverse=True)
        min_sum_brute = (sum(sorted_prices[:discount_counts]) * (100 - discount) / 100
                        + sum(sorted_prices[discount_counts:]))
        self.assertEqual(count_min_sum(prices, discount), min_sum_brute)

if __name__ == '__main__':
    unittest.main()
