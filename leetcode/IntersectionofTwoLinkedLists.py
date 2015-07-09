def getIntersectionNode(self, headA, headB):
#    p1, p2 = headA, headB
#    if not p1 or not p2:
#        return None
#    while p1 != p2:
#        p1 = p1.next
#        p2 = p2.next
#        if p1 == p2:
#            return p1
#        if p1 == None:
#            p1 = headB
#        if p2 == None:
#            p2 = headA
#    return p1
    curA, curB = headA, headB
    lenA, lenB = 0, 0
    while curA:
        lenA += 1
        curA = curA.next
    while curB:
        lenB += 1
        curB = curB.next
    curA, curB = headA, headB

    if lenA > lenB:
        for i in range(lenA-lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB-lenA):
            curB = curB.next
    while curA != curB:
        curA = curA.next
        curB = curB.next
    return curA
