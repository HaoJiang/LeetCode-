class solutions:
    def subsep(self, S):

        if not S:
            return []
        S = S.replace(",", "").replace("{", " ").replace("}", " ")

        S = [i for i in S.split(" ") if i]
        n = len(S)
        self.res = []
        print(S, n)

        def dfs(idx, path):
            if len(path) == n:
                self.res.append(path)
                return
            for i in S[idx]:
                dfs(idx + 1, path + i)

        dfs(0, '')

        return self.res


if __name__ == "__main__":
    print(solutions().subsep("{d,e}{a,b}c{d,e}f"))

