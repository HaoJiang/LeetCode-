class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        from collections import defaultdict

        cache = defaultdict(int)
        cache[0] = 1

        def dfs(root, path_sum):
            if not root:
                return 0
            # ADD THE CURRENT NODE'S VALUE TO THE PATH SUM
            path_sum += root.val

            # GET THE NUMBER OF PATHS WITH SUM = PATH_SUM - TARGET
            count = cache[path_sum - s]

            # RECORD THE PATH SUM IN SEEN
            cache[path_sum] += 1

            # RECURSE ON LEFT AND RIGHT SUBTREES
            count += dfs(root.left, path_sum)
            count += dfs(root.right, path_sum)

            # REMOVE THE PATH SUM IN SEEN
            cache[path_sum] -= 1
            return count

        return dfs(root, 0)


if __name__ == '__main__':
    print(Solution().pathSum())
