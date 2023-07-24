class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True) #Sorts decending
        for i in range(len(nums) - 2):
            print(i)
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
        #the sum of two sides must be greater than one of the sides, a + b > c

print(Solution().largestPerimeter([3,2,3,4]))