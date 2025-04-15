import unittest
#from src.pañindrome import is_palindrome, clean_text
class Testapalindrome(unittest.TestCase):
    def test_palindromes_simple(self):
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("como"))
        self.assertFalse(is_palindrome("arbol"))
    def test_textcleaner(self):
        self.assertEqual(clean_text("A man, a plan, a canal, Panama!"), "amanaplanacanalpanama")
        self.assertEqual(clean_text("No 'x' in Nixon."), "noxinnixon")
        self.assertTrue(clean_text("como estas?"), "comoestas")

if __name__ == '__main__':
    unittest.main()       