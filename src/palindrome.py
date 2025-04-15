import string
def is_palindrome(text):
    text = text.lower()
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    cleaned_text = cleaned_text.replace(" ", "")
    return cleaned_text== cleaned_text[::-1]

