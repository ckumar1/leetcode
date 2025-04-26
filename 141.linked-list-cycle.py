#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def hasCycle(self, head: Optional[ListNode], next=None) -> bool: # type: ignore
        if not head or not head.next:
            return False

        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
        
# @lc code=end
