class solution:
    def addTwoNumbers(self, l1, l2):
        ## Time O(max(n,m)) || Space O(max(n,m)) [at max it will be max(n,m)+1]
        ## n: l1 first list m: l2 second list

        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return None

        res = ListNode(0)
        node = res

        carry = 0
        l1_val = l1.val
        l2_val = l2.val
        while l1 or l2:

            currSum = l1_val + l2_val + carry

            quotient = currSum % 10
            node.next = ListNode(quotient)
            carry = currSum // 10

            node = node.next

            if not l1.next and not l2.next:
                break

            if l1.next:
                l1 = l1.next
                l1_val = l1.val
            else:
                l1_val = 0

            if l2.next:
                l2 = l2.next
                l2_val = l2.val
            else:
                l2_val = 0

        if carry:
            node.next = ListNode(carry)
            node = node.next

        return res.next