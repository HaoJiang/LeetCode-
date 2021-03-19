class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter, defaultdict
        C_word1 = Counter(word1)
        C_word2 = Counter(word2)

        m = len(word1)
        n = len(word2)
        if m != n:
            return False

        M_word1 = defaultdict(int)
        M_word2 = defaultdict(int)
        for i, v in C_word1.items():
            M_word1[v] += 1

        for i, v in C_word2.items():
            M_word2[v] += 1

        if len(set(C_word1) ^ set(C_word2)) > 0:
            return False

        for i in M_word1:
            if i not in M_word2:
                return False
            if M_word1[i] != M_word2[i]:
                return False
        return True


if __name__ =="__main__":

    print(Solution().closeStrings( word1 = "cabbba", word2 = "abbccc"))

