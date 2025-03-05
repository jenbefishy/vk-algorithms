import queue
import unittest

'''
В исходную строку добавили некоторое количество символов. Необходимо выявить, была ли строка a исходной для строки b.
'''

def isSubsequence(a: str, b: str) -> bool:
    i, j = 0, 0
    lenA = len(a)
    lenB = len(b)

    while i < lenA and j < lenB:
        if a[i] == b[j]:
            i += 1
        j += 1

    return i == lenA


class TestIsSubsequence(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isSubsequence("abc", "aebdc"))
    
    def test_case_2(self):
        self.assertFalse(isSubsequence("axc", "ahbgdc"))
    
    def test_case_3(self):
        self.assertTrue(isSubsequence("", "abc"))
    
    def test_case_4(self):
        self.assertFalse(isSubsequence("abc", ""))
    
    def test_case_5(self):
        self.assertTrue(isSubsequence("abc", "abc"))
    
    def test_case_6(self):
        self.assertTrue(isSubsequence("abc", "aabbcc"))
    
    def test_case_7(self):
        self.assertFalse(isSubsequence("abc", "cba"))
    
if __name__ == "__main__":
    unittest.main()
