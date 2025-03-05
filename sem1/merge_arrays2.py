import unittest

'''
Дано два отсортированных массива. Необходимо
написать функцию которая объединит эти два массива
в один отсортированный.
Первый массив имеет размер, равный
результирующиму массиву, значения в конце равны
нулям. Мы не должны создавать третий массив
'''

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    p1 = len(arr1) - len(arr2) - 1
    p2 = len(arr2) - 1
    p3 = len(arr1) - 1
    
    while p2 >= 0:
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p3] = arr1[p1]
            p1 -= 1
        else:
            arr1[p3] = arr2[p2]
            p2 -= 1
        p3 -= 1

    return arr1


class TestMergeFunction(unittest.TestCase):

    def test_case_1(self):
        arr1 = [1, 3, 5, 0, 0, 0]
        arr2 = [2, 4, 6]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_case_2(self):
        arr1 = [0, 0, 0]
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
        arr1 = [1, 1, 1, 0, 0, 0]
        arr2 = [1, 1, 1]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 1, 1, 1, 1, 1])

    def test_case_6(self):
        arr1 = [1, 2, 3, 0, 0, 0]
        arr2 = [4, 5, 6]
        result = merge(arr1, arr2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
