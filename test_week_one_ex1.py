import unittest

import week_one_challenges


class Test_TestMultiplicationOrSum(unittest.TestCase):
    def test_fifty_times_fifty(self):
        self.assertEqual(week_one_challenges.multiplication_or_sum(50, 50), 100)

    def test_fifty_times_five(self):
        self.assertEqual(week_one_challenges.multiplication_or_sum(50, 5), 250)
    
    def test_fifty_times_five_hundred(self):
        self.assertEqual(week_one_challenges.multiplication_or_sum(50, 500), 550)
    
    def test_seven_times_five(self):
        self.assertEqual(week_one_challenges.multiplication_or_sum(7, 5), 35)


if __name__ == '__main__':
    unittest.main()