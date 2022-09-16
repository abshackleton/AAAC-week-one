import unittest

import week_one_challenges


class Test_TestEggDecoder(unittest.TestCase):
    def test_UK_organic(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("1UK5432A"), ["Organic", "United Kingdom", "5432A"])

    def test_NL_organic(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("1NL5432A"), ["Organic", "Netherlands", "5432A"])
    
    def test_BE_organic(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("1BE5432A"), ["Organic", "Belgium", "5432A"])
    
    def test_DE_organic(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("1DE5432A"), ["Organic", "Germany", "5432A"])
    

    def test_UK_free_range(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("2UK5432A"), ["Free range", "United Kingdom", "5432A"])
    
    def test_NL_free_range(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("2NL5432A"), ["Free range", "Netherlands", "5432A"])
    
    def test_BE_free_range(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("2BE5432A"), ["Free range", "Belgium", "5432A"])
    
    def test_DE_free_range(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("2DE5432A"), ["Free range", "Germany", "5432A"])
    

    def test_UK_barn(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("3UK5432A"), ["Barn", "United Kingdom", "5432A"])
    
    def test_NL_barn(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("3NL5432A"), ["Barn", "Netherlands", "5432A"])
    
    def test_BE_barn(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("3BE5432A"), ["Barn", "Belgium", "5432A"])
    
    def test_DE_barn(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("3DE5432A"), ["Barn", "Germany", "5432A"])
    

    def test_UK_cage(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4UK5432A"), ["Cage", "United Kingdom", "5432A"])
    
    def test_NL_cage(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4NL5432A"), ["Cage", "Netherlands", "5432A"])
    
    def test_BE_cage(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4BE5432A"), ["Cage", "Belgium", "5432A"])
    
    def test_DE_cage(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4DE5432A"), ["Cage", "Germany", "5432A"])

    
    def test_invalid_method(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("5UK5432A"), 0)
    
    def test_invalid_country(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4US5432A"), 0)
    
    def test_too_long(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4BE56432A"), 0)
    
    def test_too_short(self):
        self.assertEqual(week_one_challenges.egg_stamp_decoder("4DE542A"), 0)


if __name__ == '__main__':
    unittest.main()