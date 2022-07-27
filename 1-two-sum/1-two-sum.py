class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            required= target-num
            temp= list(nums[nums.index(num)+1:])
            if required in temp:
                index1= nums.index(num)
                index2= temp.index(required)
                return [index1, index1+index2+1]