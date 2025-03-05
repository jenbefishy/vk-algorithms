import unittest

'''
Дан массив, содержащий только 0 и 1. Напишите функцию,
которая сортирует его так, чтобы все нули оказались в
начале, а все единички - в конце. Решение должно быть
in-place.
'''

def sort_binary_array(arr: list[int]) -> list[int]:
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1

    return arr

class TestSortBinaryArray(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 0, 1, 0, 1, 0]
        sort_binary_array(arr)
        self.assertEqual(arr, [0, 0, 0, 1, 1, 1])

    def test_case_2(self):
        arr = [0, 0, 0, 0]
        sort_binary_array(arr)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_case_3(self):
        arr = [1, 1, 1, 1]
        sort_binary_array(arr)
        self.assertEqual(arr, [1, 1, 1, 1])

    def test_case_4(self):
        arr = [1, 0, 0, 1, 0, 1]
        sort_binary_array(arr)
        self.assertEqual(arr, [0, 0, 0, 1, 1, 1])

    def test_case_5(self):
        arr = [0, 1]
        sort_binary_array(arr)
        self.assertEqual(arr, [0, 1])

    def test_case_6(self):
        arr = [1, 0]
        sort_binary_array(arr)
        self.assertEqual(arr, [0, 1])

    def test_case_7(self):
        arr = []
        sort_binary_array(arr)
        self.assertEqual(arr, [])

if __name__ == "__main__":
    unittest.main()
