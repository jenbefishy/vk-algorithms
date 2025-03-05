import unittest

'''
Дан не отсортированный массив целых чисел. Необходимо перенести в начало
массива все четные числа, сохраняя их очередность. То есть если 8 стояла после 2,
то после переноса в начало, он по-прежнему должна стоять после 2
'''

def evenFirst(arr:list[int]) -> list[int]:
    ind = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[ind] = arr[ind], arr[i]
            ind += 1
    return arr

class TestEvenFirst(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5]
        evenFirst(arr)
        self.assertEqual(arr, [2, 4, 3, 1, 5])

    def test_case_2(self):
        arr = [2, 4, 6, 8]
        evenFirst(arr)
        self.assertEqual(arr, [2, 4, 6, 8])

    def test_case_3(self):
        arr = [1, 3, 5, 7]
        evenFirst(arr)
        self.assertEqual(arr, [1, 3, 5, 7])

    def test_case_4(self):
        arr = [3, 1, 4, 2, 5]
        evenFirst(arr)
        self.assertEqual(arr, [4, 2, 3, 1, 5])

    def test_case_5(self):
        arr = []
        evenFirst(arr)
        self.assertEqual(arr, [])

if __name__ == "__main__":
    unittest.main()
