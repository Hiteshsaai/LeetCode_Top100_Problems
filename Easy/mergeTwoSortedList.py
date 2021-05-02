class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        ## Time O(n+m) || Space O(n+m)
        if l1 and not l2:
            return l1

        if l2 and not l1:
            return l2

        if not l1 and not l2:
            return None

        res = ListNode(0)

        node = res

        while l1 and l2:

            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next

            elif l2.val < l1.val:
                node.next = ListNode(l2.val)
                l2 = l2.next

            node = node.next

        node.next = l2 if not l1 else l1

        return res.next
