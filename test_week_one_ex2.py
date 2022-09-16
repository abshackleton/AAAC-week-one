import unittest

import week_one_challenges


class Test_TestReturnLastWord(unittest.TestCase):
    def test_mouse_vole_cat(self):
        self.assertEqual(week_one_challenges.return_last_word(["mouse", "vole", "cat"]), "vole")

    def test_cat(self):
        self.assertEqual(week_one_challenges.return_last_word(["cat"]), "cat")
    
    def test_cat_dog_mouse_moose(self):
        self.assertEqual(week_one_challenges.return_last_word(['cat', 'dog', 'mouse', 'moose']), "mouse")


if __name__ == '__main__':
    unittest.main()