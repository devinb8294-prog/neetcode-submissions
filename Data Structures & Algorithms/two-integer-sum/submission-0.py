class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            right = len(nums)-1
            while right > i:
                if nums[i] + nums[right] == target:
                    return [i,right]
                right -= 1
            

