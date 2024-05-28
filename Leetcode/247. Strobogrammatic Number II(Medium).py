# def strobogrammatic_num(n):
#     result = numdef(n, n)
#     return result
#
#
# # definition function
# def numdef(n, length):
#     if n == 0: return [""]
#     if n == 1: return ["1", "0", "8"]
#
#     middles = numdef(n - 2, length)
#     result = []
#
#     for middle in middles:
#         if n != length:
#             result.append("0" + middle + "0")
#
#         result.append("8" + middle + "8")
#         result.append("1" + middle + "1")
#         result.append("9" + middle + "6")
#         result.append("6" + middle + "9")
#     return result
#
#
# # Driver Code
# if __name__ == '__main__':
#     # Print all Strobogrammatic
#     # number for n = 3
#     print(strobogrammatic_num(3))


class Soultion(object):
    def strobogrammatic(self, n):
        def dfs(n, k):
            if k == 0:
                return ['']
            if k == 1:
                return ['1', '0', '8']

            mid = dfs(n, k - 2)

            res = []

            for i in mid:
                if n != k:
                    res.append('0' + i + '0')
                res.append('1' + i + '1')
                res.append('6' + i + '9')
                res.append('9' + i + '6')
                res.append('8' + i + '8')

            return res

        return dfs(n, n)


print(Soultion().Strobogrammatic(4))
