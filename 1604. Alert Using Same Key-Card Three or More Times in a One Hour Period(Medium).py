from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict

        map = defaultdict(list)
        ans = []
        for name, time in zip(keyName, keyTime):
            tt = time.split(':')
            map[name].append((int(tt[0]) * 60 + int(tt[1])))

        for idx, val in map.items():
            val.sort()
            if len(val) >= 3:
                for i in range(2, len(val)):
                    if val[i] > val[i - 1] > val[i - 2] and val[i] - val[i - 2] <= 60:
                        ans.append(idx)
                        break
        return sorted(ans)


if __name__ == '__main__':
    print(Solution().alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                                ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
