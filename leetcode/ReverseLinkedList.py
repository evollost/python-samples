def ReverselinkedList(self, head):
#def ReverselinkedList(self, node, prev=None):
#    if not node:
#        return prev
#    next = node.next
#    node.next = prev
#    return self.ReverseLinkedList(next, node)
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur
    return pre
        
