import unittest

'''
Дан отсортированный по возрастанию
массив целых чисел и некоторое число target
Необходимо найти два числа в массиве,
которые в сумме дают заданное значение
target, и вернуть их индексы.
'''

def twoSum(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if target == s:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return []


class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
    
    def test_case_2(self):
        self.assertEqual(twoSum([2, 3, 4], 6), [0, 2])
    
    def test_case_3(self):
        self.assertEqual(twoSum([3, 3], 6), [0, 1])
    
    def test_case_4(self):
        self.assertEqual(twoSum([-5, -4, -3, 6, 9], 2), [1, 3])
    
    def test_case_5(self):
        self.assertEqual(twoSum([1, 2, 3, 4, 5, 6], 10), [3, 5])
    
    def test_case_6(self):
        self.assertEqual(twoSum([1, 2, 8, 4, 9, 6], 7), [0, 5])
    
    def test_case_7(self):
        self.assertEqual(twoSum([1, 2, 3, 4, 5, 6], 12), [])
    
    def test_case_8(self):
        self.assertEqual(twoSum([-3, 0, 3, 7, 9], 7), [1, 3])
    
    def test_case_9(self):
        self.assertEqual(twoSum([0, 0, 3, 4], 0), [0, 1])

if __name__ == "__main__":
    unittest.main()

