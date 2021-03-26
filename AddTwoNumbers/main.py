# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        aux = result
        carry = 0
        prev = None
        while l1 or l2 or carry > 0:
            sum = 0
            if l1 and l2:
                sum = (l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = (l1.val + carry)
                l1 = l1.next
            elif l2:
                sum = (l2.val + carry)
                l2 = l2.next
            else:
                sum = carry
            aux.val = sum % 10
            carry = sum//10
            prev = aux
            aux.next = ListNode()
            aux = aux.next
        if(aux.val == 0):
            prev.next = None
        return result

    def to_list(self, node: ListNode):
        l = []
        aux = node
        while aux != None:
            l.append(aux.val)
            aux = aux.next
        return l


if __name__ == "__main__":
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)


    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    sol = Solution()
    print(sol.to_list(sol.addTwoNumbers(l1, l2)))
