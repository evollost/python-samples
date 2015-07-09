def isPalindrome(self, s):
#fast solution:
#    string = ''.join([c.lower() for c in s if c.isalnum()])
#    return string == string[::-1]
    start, end = 0, len(s)-1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            if s[start].lower() != s[end].lower():
                return False
            start, end = start+1, end-1
    return True
