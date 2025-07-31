"""_Question_
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""

from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            merged_string.append(word1[i])
            i += 1

        while j < len(word2):
            merged_string.append(word2[j])
            j += 1

        return "".join(merged_string)


"""
Given an integer array nums of size n, return the number with the closest value to 0 in nums. If there are multiple answers, return the number with the largest value.
"""


class Solution:
    def closestToZero(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest


"""_Roman Numbers to Integers_
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
                total += roman_map[s[i+1]] - roman_map[s[i]]
                i += 2
            else:
                total += roman_map[s[i]]
                i += 1
        return total


"""Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if S > T:
            return False
        if s == "":
            return True

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:
                    return True
                j += 1
        return False


"""
You are given an array of prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 0
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit