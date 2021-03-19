# Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
#
#
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
#
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
# Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# Output: [1,4,2,5,3,8,6,9,7,10,11]
#
#
# Input: nums = [[1,2,3,4,5,6]]
# Output: [1,2,3,4,5,6]
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.


# same idea on 498
#
# we create hashtable store the point total in hash   because  the diagonal point total is same (01 10) (02 11 20)
# and the extend list is ordered   so when store all the number we just trversal the dt and reversed list save to the res
# then return
