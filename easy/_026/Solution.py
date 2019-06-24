'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

解法：
使用快慢指针来记录遍历的坐标。

开始时这两个指针都指向第一个数字

如果两个指针指的数字相同，则快指针向前走一步

如果不同，慢指针的下一个值为快指针的值，且两个指针都向前走一步

当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数

复杂度分析

时间复杂度：O(n)，假设数组的长度是 n，那么 i 和 j 分别最多遍历 n 步。

空间复杂度：O(1)。

'''


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        low, fast = 0, 0
        while (fast < len(nums)):
            if nums[low] == nums[fast]:
                fast += 1
            else:
                nums[low + 1] = nums[fast]
                low += 1
                fast += 1
        return low + 1
