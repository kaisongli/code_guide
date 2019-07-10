'''
* 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 *
 * 你可以假设数组是非空的，并且给定的数组总是存在众数。
 *
 * 示例 1:
 *
 * 输入: [3,2,3]
 * 输出: 3
 *
 * 解法1：
 * 使用哈希表来存储每个元素，然后用一个循环在线性时间内遍历 nums ，然后我们只需要返回有最大值的键。
 * 复杂度分析
 *
 * 时间复杂度：O(n)
 * 我们将 nums 迭代一次，哈希表的插入是常数时间的。所以总时间复杂度为 O(n)时间的。
 * 空间复杂度：O(n)
 *
 * 解法2：
 * 先将 nums 数组排序，然后返回上面所说的数字。无论众数是多少，返回 n/2下标对应的值都是正确的。
 * 时间复杂度：O(nlgn)
 * 空间复杂度：O(1) 或者 O(n)
'''
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort();
        return nums[len(nums) // 2];

    def majorityElemen2(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)