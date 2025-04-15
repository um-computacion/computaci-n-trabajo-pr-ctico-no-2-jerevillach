import unittest
#from src.pañindrome import is_palindrome, clean_text
class Testapalindrome(unittest.TestCase):
    def test_palindromes_simple(self):
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("como"))
        self.assertFalse(is_palindrome("arbol"))
    def test_frases_palindromes(self):
        self.assertTrue(is_palindrome("La ruta natural"))
        self.assertTrue(is_palindrome("Amo la pacífica paloma"))
        self.assertTrue(is_palindrome("Anita lava la tina"))

if __name__ == "__main__":
    unittest.main()      
