class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import defaultdict
        x = 0
        y = 0
        map = defaultdict(set)
        guess = list(guess)
        for i, v in enumerate(secret):
            if guess[i] == v:
                x += 1
                guess[i] = 'F'
            else:
                map[v].add(i)
        for i, v in enumerate(guess):
            if v != 'F' and v in map:
                y += 1
                map[v].pop()
                if not map[v]:
                    del map[v]
        return str(x) + 'A' + str(y) + 'B'


if __name__ == '__main__':
    print(Solution().getHint( secret = "1807", guess = "7810"))
