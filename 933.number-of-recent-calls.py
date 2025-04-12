#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

from collections import deque

# @lc code=start
class RecentCounter:

    def __init__(self):
        # need a queue of timestamps that are pushed into the queue on ping
        # Queue should be groomed after every ping so that it pops items < t-30000
        # count of recent calls is equal to number of items in the queue
        self.recent_calls = deque()

    def ping(self, t: int) -> int:
        # Add t to recent queue    
        self.recent_calls.append(t)
        # peek at each item at the beginnning of the q to ensure that its <t-3000
        while self.recent_calls[0] < t -3000:
            self.recent_calls.popleft()
        return len(self.recent_calls)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

