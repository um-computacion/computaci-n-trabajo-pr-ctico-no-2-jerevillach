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
    def test_frases_no_palindromes(self):
        self.assertFalse(is_palindrome("El sol brilla"))
        self.assertFalse(is_palindrome("Python es genial"))
        self.assertFalse(is_palindrome("Hoy es un buen día"))
if __name__ == "__main__":
    unittest.main()      
