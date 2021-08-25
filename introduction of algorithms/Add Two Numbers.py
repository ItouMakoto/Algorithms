class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resList = ListNode()
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        bitSum = val1 + val2 + carry
        bit = bitSum % 10
        carry = bitSum // 10
        resList.val = bit
        l1next = l1.next if l1 else None
        l2next = l2.next if l2 else None
        if not l1next and not l2next and carry == 0:
            return resList
        resList.next = self.addTwoNumbers(l1next, l2next, carry)
        return resList


if __name__ == '__main__':
    l1 = [9, 9]
    l2 = [9]
    test = Solution()
    print(test.addTwoNumbers(l1, l2))
