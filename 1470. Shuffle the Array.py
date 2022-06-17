class Solution:
    '''
    1470. Shuffle the Array: https://leetcode.com/problems/shuffle-the-array/
    
    Solution Approach: Since the array contains 2n elements, if xi is an element, then xi + n will be yn.

    '''
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans