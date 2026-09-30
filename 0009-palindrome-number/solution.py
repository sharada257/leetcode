# @leetsync-header
# Problem: 9. Palindrome Number (Easy)
# Language: Python3
# Runtime: 8 ms (Beats 53.96%)
# Memory: 19.3 MB (Beats 55.58%)
# Submission: https://leetcode.com/problems/palindrome-number/submissions/2157918857/
# Submitted: 2026-09-30T07:24:57.532Z

class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False

        temp=x
        rnum=0
        
        while temp!=0:
                digit = temp%10
                rnum=rnum*10+digit
                temp=temp//10
        return x==rnum
