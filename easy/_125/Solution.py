'''
* 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * <p>
 * 说明：本题中，我们将空字符串定义为有效的回文串。
 * <p>
 * 示例 1:
 * <p>
 * 输入: "A man, a plan, a canal: Panama"
 * 输出: true
 * <p>
 * 解法：
 * 双指针法
 * 分别判断首尾指针指向的字符是不是字母和数字字符，如果不是的话，例如是空格，标点符号之类的，那分别指向下一个
 * 如果当前指向的字符是符合要求的，那需要判断是否相等，如果不相等就直接返回false
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        while begin < end:
            while begin < end and not s[begin].isalnum():
                begin += 1
            while begin < end and not s[end].isalnum():
                end -= 1
            if s[begin].lower() != s[end].lower():
                return False
            begin += 1
            end -= 1
        return True
