'''
* 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
 *
 * 说明：
 *
 * 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
 *
 * 示例 1:
 *
 * 输入: [2,2,1]
 * 输出: 1
 *
 * 解法：
 *
 * 题目描述了时间复杂度必须是 O(n)，并且空间复杂度为 O(1)的条件，因此首先想到的Map解法是不能用的
 *
 * 我们可以利用二进制异或的性质来完成，将所有数字异或即得到唯一出现的数字。
 *
 * 关键点
 * 异或的性质：两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。如果同一位的数字相同则为 0，不同则为 1
 *
 * 异或的规律
 *
 * 任何数和本身异或则为0
 *
 * 任何数和 0 异或是本身
'''
from _ast import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= nums[i]
        return res