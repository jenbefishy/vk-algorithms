import unittest

'''
Дан массив целых чисел.
Необходимо развернуть его.
Сделать это надо за линейное время без
дополнительных аллокаций памяти
'''

def reverseArray(nums:list[int]):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

class TestReverseArray(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4, 5]
        reverseArray(nums)
        self.assertEqual(nums, [5, 4, 3, 2, 1])
    
    def test_case_2(self):
        nums = [1, 2, 2, 3]
        reverseArray(nums)
        self.assertEqual(nums, [3, 2, 2, 1])
    
    def test_case_3(self):
        nums = [7]
        reverseArray(nums)
        self.assertEqual(nums, [7])
    
    def test_case_4(self):
        nums = []
        reverseArray(nums)
        self.assertEqual(nums, [])
    
    def test_case_5(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        reverseArray(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == "__main__":
    unittest.main()

