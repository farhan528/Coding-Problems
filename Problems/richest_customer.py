# Problem link: https://leetcode.com/problems/richest-customer-wealth/


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            current_sum = 0
            for j in range(len(accounts[i])):
                current_sum+=accounts[i][j]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
