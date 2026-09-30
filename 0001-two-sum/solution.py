# @leetsync-header
# Problem: 1. Two Sum (Easy)
# Language: Python3
# Runtime: 7 ms (Beats 35.94%)
# Memory: 20.7 MB (Beats 7.63%)
# Submission: https://leetcode.com/problems/two-sum/submissions/2157909424/
# Submitted: 2026-09-30T07:12:04.074Z

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        nums=[(j,i) for i,j in enumerate(nums)]
        nums.sort()
        while(i<j):
            if nums[i][0]+nums[j][0]==target:
                return [nums[i][1],nums[j][1]]
            elif nums[i][0]+nums[j][0]<target:
                i+=1
            else:
                j-=1
