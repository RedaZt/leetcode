class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            try: 
                return [i, i+1+nums[i+1:].index(target - nums[i])]
            except: 
                pass