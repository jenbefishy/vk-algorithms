import unittest

'''
Дано два отсортированных массива. Необходимо
написать функцию которая объединит эти два массива
в один отсортированный
'''

def merge(arr1:list[int], arr2:list[int]) -> list[int]:
    merged_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    # Last elements
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr

class TestMergeFunction(unittest.TestCase):

    def test_case_1(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_case_2(self):
        arr1 = []
        arr2 = [1, 2, 3]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 2, 3])

    def test_case_3(self):
        arr1 = [1, 2, 3]
        arr2 = []
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 2, 3])

    def test_case_4(self):
        arr1 = []
        arr2 = []
        result = merge(arr1, arr2)
        self.assertEqual(result, [])

    def test_case_5(self):
        arr1 = [1, 1, 1]
        arr2 = [1, 1, 1]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 1, 1, 1, 1, 1])

    def test_case_6(self):
        arr1 = [3, 1, 2]
        arr2 = [6, 4, 5]
        result = merge(sorted(arr1), sorted(arr2))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
