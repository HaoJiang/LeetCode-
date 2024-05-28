from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

        map = {}

        for i in cpdomains:
            temp = i.split(' ')
            times = int(temp[0])
            cdomain = temp[1].split('.')
            for j in range(len(cdomain)):
                curr = '.'.join(cdomain[j:])
                if curr in map:
                    map[curr] += times
                else:
                    map[curr] = times
        return [str(v) + ' ' + i for i, v in map.items()]


if __name__ == '__main__':
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
