import unittest

'''
Дан массив целых чисел.
Необходимо повернуть (сдвинуть) справа налево часть массива, которая
указана вторым параметром.
Сделать это надо за линейное время без дополнительных аллокаций
'''

def reverseArray(arr:list[int], left:int, right:int):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def solve(arr:list[int], k:int) -> list[int]:
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, k % n - 1)
    reverseArray(arr, k % n, n - 1)


class TestArrayRotation(unittest.TestCase):
    
    def test_case_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solve(arr, k)
        self.assertEqual(arr, [5, 6, 7, 1, 2, 3, 4])

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5]
        k = 5
        solve(arr, k)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        k = 8
        solve(arr, k)
        self.assertEqual(arr, [3, 4, 5, 1, 2])

    def test_case_4(self):
        arr = [1, 2, 3, 4, 5]
        k = 0
        solve(arr, k)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_case_5(self):
        arr = [1]
        k = 0
        solve(arr, k)
        self.assertEqual(arr, [1])

    def test_case_6(self):
        arr = [1, 2]
        k = 1
        solve(arr, k)
        self.assertEqual(arr, [2, 1])

if __name__ == "__main__":
    unittest.main()
