def trailingZeroes(self, n):
    #return 0 if n < 5 else n // 5 + self.trailingZeroes(n//5)
    k = count = 0
    while True:
        if 5**k >= n:
            break
        k += 1
        count += n // 5**k
    return count
