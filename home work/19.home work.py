import string
def is_palindrome(text):
    clean_text = ''.join(i for i in text.lower() if i not in string.punctuation).replace(" ", "")
    revers_text = clean_text[::-1]
    if clean_text == revers_text:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")


