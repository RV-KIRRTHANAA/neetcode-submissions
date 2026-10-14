class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for nums in num_set:
            if nums-1 not in num_set:
                current = nums
                length = 1
                while current+1 in num_set:
                    current+=1
                    length+=1
                longest = max(longest, length)
        return longest