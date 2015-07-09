def getRow(self, rowIndex):
    result = []
    value = 1
    if rowIndex >= 0:
        result.append(value)
        for i in range(1,rowIndex+1):
            value = value * (rowIndex+1-i) / i
            result.append(value)
    return result
