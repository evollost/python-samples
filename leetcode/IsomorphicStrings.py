def isIsomorphic(self, s, t):
#    S = [0] * 128
#    T = [0] * 128
#    for i in range(len(s)):
#        if S[ord(s[i])] == 0 and T[ord(t[i])] ==0:
#            S[s[i]] = t[i]
#            T[t[i]] = s[i]
#        elif S[ord(s[i])] != t[i] or T[ord(t[i])] != s[i]:
#            return False
#    return True
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))
