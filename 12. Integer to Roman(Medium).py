class Solution:
    def intToRoman(self, num: int) -> str:
        map = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        map = {val: idx for idx, val in map.items()}
        first = 5
        sec = 10
        st = ''
        time = 1
        while num:
            k = num % 10
            num //= 10
            if k not in map:
                if k < first:
                    st = (first - k) * map[time] + map[first * time] + st
                elif k < sec:
                    st = (sec - k) * map[time] +  map[sec * time] + st
            else:
                st = map[k * time] + st
            time *= 10
        return st

    # stack = []
    # for i in num:
    #     if stack and stack[-1] < map[i]:
    #         num = stack.pop()
    #         stack.append(map[i] - num)
    #     else:
    #         stack.append(map[i])
    #
    # return sum(stack)


if __name__ == '__main__':
    print(Solution().intToRoman(58))
