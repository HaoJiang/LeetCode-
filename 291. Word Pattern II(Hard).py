class Solution:
    def wordPattern2(self, pattern, str):
        if not pattern:
            return False

        mp = {}
        used = set()

        def dfs(idx, st, used):
            if idx == len(pattern):
                return not st
            word = pattern[idx]

            if word in mp:
                if not st.startswith(mp[word]):
                    return False

                return dfs(idx + 1, st[len(mp[word]):], used)

            for i in range( len(st)):
                ch = st[:i + 1]
                if ch in used:
                    continue
                mp[word] = st[:i + 1]
                used.add(st[:i + 1])
                if dfs(idx + 1, st[i + 1:], used):
                    return True
                used.discard(st[:i + 1])
                del mp[word]
            return False

        return dfs(0, str, used)


if __name__ == "__main__":

    print(Solution().wordPattern2(pattern = "aaaa",str = "dogdogdogdog"))
