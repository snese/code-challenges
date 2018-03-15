class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return False
        dict = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in dict:
                return [dict[value], index]
            else:
                dict[num] = index
        return False