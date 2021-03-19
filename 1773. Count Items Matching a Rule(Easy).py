from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum((1 for x, y, z in items if
                    (ruleKey == 'type' and x == ruleValue) or (ruleKey == 'color' and y == ruleValue) or (
                            ruleKey == 'name' and z == ruleValue)))


if __name__ == '__main__':
    print(Solution().countMatches(
        [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], ruleKey="type",
        ruleValue="phone"))
