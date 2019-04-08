class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev_count = 1
        count = 1
        if len(nums) < 1:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:                
                if nums[i] - nums[i-1] == 1:
                    count = count+1
                    print(count)
                else:
                    prev_count = max(prev_count,count)
                    count = 1

        return max(count,prev_count)
                
      