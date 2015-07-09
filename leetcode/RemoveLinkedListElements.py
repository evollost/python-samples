def removeElements(self, head, val):
    cur = head
    pre = None
    while cur:
        if cur.val == val:
            if not pre:
                head = cur.next
            else:
                pre.next = cur.next
            cur = cur.next
        else:
            pre = cur
            cur = cur.next
    return head
