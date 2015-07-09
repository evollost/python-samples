def sumup(n):
    m = sum([int(i) ** 2 for i in str(n)])
    return m

def isHappy(n):
    slow = fast =n
    while True:
        slow = sumup(slow)
        #print slow
        fast = sumup(sumup(fast))
        #print '   ', fast
        if slow == fast:
            break
    if slow == 1:
        return True
    else:
        return False

def isHappy2(n):
    m = n
    mem = set()
    while m not in mem:
        mem.add(m)
        m = sumup(m)
        #print m
        if m == 1:
            return True
    return False


#for x in xrange(100000):
print isHappy(123456789)

#for x in xrange(100000):
print isHappy2(123456789)
