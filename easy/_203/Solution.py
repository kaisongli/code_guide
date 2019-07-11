'''
* 删除链表中等于给定值 val 的所有节点。
 * <p>
 * 示例:
 * <p>
 * 输入: 1->2->6->3->4->5->6, val = 6
 * 输出: 1->2->3->4->5
 *
 * 解法：
 * 链表的基本操作，不过需要注意边界值
 * 如果头节点就是需要删除的节点的情况 --->采用虚拟节点
 * 如果连续两个节点都是要删除的节点的情况
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dumpyNode = ListNode(-1)
        dumpyNode.next = head
        curNode = dumpyNode
        while curNode.next != None:
            if curNode.next.val == val:
               curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return dumpyNode.next