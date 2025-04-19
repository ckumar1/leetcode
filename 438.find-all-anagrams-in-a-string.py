#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

from collections import Counter
from typing import List, Dict

# @lc code=start
class Solution:
    def removeLetter(self, counter: Counter, letter):
        if letter in counter[letter]:
            counter[letter] -= 1 

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        ans = []
        # store anagram string p into a counter hash table by letter
        anagram_counter = Counter(p)
        anagram_letter_count = len(p)
        # decrement counter for each letter when it is part of the current substring
        for i in range(len(p)):
            letter = s[i]
            if letter in anagram_counter:
                anagram_counter[letter] -= 1
                if anagram_counter[letter] >= 0:
                    anagram_letter_count -= 1
        if anagram_letter_count == 0:
            ans.append(0)

        # iterate through each letter of s
        for right in range(len(p), len(s)):
            left = right - len(p)
            left_letter, right_letter = s[left], s[right]
            # add 1 to counter if letter at left exists in anagram_counter
            if left_letter in  anagram_counter:
                anagram_counter[left_letter] += 1
                if anagram_counter[left_letter] > 0:  # Also important!
                    anagram_letter_count += 1
            # subtract 1 from counter if right letter exists in anagram_counter
            if right_letter in anagram_counter:
                anagram_counter[right_letter] -= 1
                if anagram_counter[right_letter] >= 0:  # Also important!
                    anagram_letter_count -= 1
                    

            if anagram_letter_count == 0:
                ans.append(left+1)

        return ans 
            
            # do an anagram check starting at each letter
            # store anagram string p into a counter hash table
            # an anagram check can be done by iterating forward len(p) substring and checking if the counters are set to zero
            # or we can do an anagram check using a sliding window
# @lc code=end
