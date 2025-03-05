import unittest

'''
В школе прошел экзамен по математике.
Несколько человек списали решения и были
замечены. Этим школьникам поставил 0
баллов. Задача: есть массив с оценками,
среди которых есть 0. Необходимо все
оценки, равные нулю перенести в конец
массива, чтобы все такие школьники
оказались в конце списка.
'''

def solve(arr: list[int]):
    ind = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[ind] = arr[ind], arr[i]
            ind += 1


class TestSolve(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 0, 3, 0, 5, 0, 7]
        solve(arr)
        self.assertEqual(arr, [1, 3, 5, 7, 0, 0, 0])

    def test_case_2(self):
        arr = [0, 0, 0, 0]
        solve(arr)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        solve(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_case_4(self):
        arr = [0, 1, 2, 3, 4]
        solve(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 0])

    def test_case_5(self):
        arr = [1, 2, 3, 4, 0]
        solve(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 0])

if __name__ == "__main__":
    unittest.main()
