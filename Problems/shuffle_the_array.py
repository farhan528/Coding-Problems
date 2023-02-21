# Problem link: https://leetcode.com/problems/shuffle-the-array/description/


class Solution(object):
    def shuffle(self, nums, n):
       arr1 = nums[0:n]
       arr2 = nums[n:]
       arr3 = []
       for i in range(n):
           arr3.append(arr1[i])
           arr3.append(arr2[i])
       return arr3

