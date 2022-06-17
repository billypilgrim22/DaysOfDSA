class Solution:
    '''
    1295. Find Numbers with Even Number of Digits: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
    
    Solution Approach: Go through each element in the list, divide the length of the element by 2,  and if remainder is zero (even number), increment the counter.
    '''
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in range(0,len(nums)):
            if(len(str(nums[i]))%2==0):
                c=c+1
        return c