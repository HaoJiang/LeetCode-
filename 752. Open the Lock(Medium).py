# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
#
#
# Example 1:
#
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:
#
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#
# Example 3:
#
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
# Example 4:
#
# Input: deadends = ["0000"], target = "8888"
# Output: -1

from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        from collections import deque
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0

        deadends = set(deadends)
        dq = deque()
        dq.append(('0000', 0))
        deadends.add('0000')
        while dq:
            lock, step = dq.popleft()
            for i in range(len(lock)):
                for nei in (1, -1):
                    k = int(lock[i]) + nei
                    if k < 0:
                        new_lock = lock[:i] + '9' + lock[i+1:]
                    elif k > 9:
                        new_lock = lock[:i] + '0' + lock[i+1:]
                    else:
                        new_lock = lock[:i] + str(k) + lock[i+1:]
                    # ck = ''.join([str(i) for i in new_lock])
                    print(new_lock)

                    if new_lock == target:
                        return step + 1
                    if new_lock not in deadends:
                        deadends.add(new_lock)
                        dq.append((new_lock, step + 1))
        return -1


if __name__ == "__main__":
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(Solution().openLock(deadends, target))