import unittest

'''
Напишите функцию, которая принимает на вход строку и возвращает true, если она является палиндромом*. В противном случае верните false.

*слово или текст, одинаково читающиеся в обоих направлениях.
'''

def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


class TestIsPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isPalindrome("abccba"))
    
    def test_case_2(self):
        self.assertTrue(isPalindrome("racecar"))
    
    def test_case_3(self):
        self.assertFalse(isPalindrome("hello"))
    
    def test_case_4(self):
        self.assertTrue(isPalindrome("a"))
    
    def test_case_5(self):
        self.assertTrue(isPalindrome(""))
    
    def test_case_6(self):
        self.assertTrue(isPalindrome("12321"))
    
    def test_case_7(self):
        self.assertFalse(isPalindrome("12345"))
    
if __name__ == "__main__":
    unittest.main()
