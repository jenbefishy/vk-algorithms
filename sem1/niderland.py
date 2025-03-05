import unittest

'''
Дан массив состоящий из нулей, единиц и двоек.
Необходимо его отсортировать за линейное время
'''

def sortColors(arr:list[int]) -> list[int]:
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

import unittest

class TestSortColors(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 0, 2, 1, 0, 2]
        sortColors(arr)
        self.assertEqual(arr, [0, 0, 1, 1, 2, 2])

    def test_case_2(self):
        arr = [0, 0, 0, 0]
        sortColors(arr)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_case_3(self):
        arr = [2, 2, 2, 2]
        sortColors(arr)
        self.assertEqual(arr, [2, 2, 2, 2])

    def test_case_4(self):
        arr = [1, 2, 0, 1, 2, 0]
        sortColors(arr)
        self.assertEqual(arr, [0, 0, 1, 1, 2, 2])

    def test_case_5(self):
        arr = [0, 1]
        sortColors(arr)
        self.assertEqual(arr, [0, 1])

    def test_case_6(self):
        arr = [1, 0]
        sortColors(arr)
        self.assertEqual(arr, [0, 1])

    def test_case_7(self):
        arr = []
        sortColors(arr)
        self.assertEqual(arr, [])

if __name__ == "__main__":
    unittest.main()
