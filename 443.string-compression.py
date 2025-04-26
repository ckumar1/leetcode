#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        char = chars[0]
        count = 1

        def write_char(char: str, write: int, count: int):
            # we always write the char
            chars[write] = char
            write += 1
            if count > 1:
                # write the count if > 1
                s_count = str(count)
                for d in s_count:
                    chars[write] = d
                    write += 1
            return write

        for read in range(1, len(chars)):
            #  at the end write the final segment char and count 
            if chars[read] != char:
                write = write_char(char, write, count)
                # clear count to 1 and set char to chars[read]
                char = chars[read]
                count = 1
            else:
                count += 1

        write = write_char(char, write, count)

        return write
            


            
            
# @lc code=end
