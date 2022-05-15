class Solution(object):
    def twoSum(self, nums, target):
        for i,v in enumerate(nums):
            b = target - v
            if b in nums and (v!=b or nums.count(v)>1):
                return [i, i+1+nums[i+1:].index(b)]