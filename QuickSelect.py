#-*-coding:utf-8-*-
'''
输出n个整数中最小的k个值
'''
import random

def QuickSelect(list, k):
    list_small = []
    list_large = []
    pivot = random.choice(list)
    for element in list:
        if element < pivot:
            list_small.append(element)
        elif element > pivot:
            list_large.append(element)
    if k <= len(list_small):
        return QuickSelect(list_small, k)
    elif k > len(list)-len(list_large):
        return QuickSelect(list_large, k-(len(list)-len(list_large)))
    return pivot

def FindKSmallestNumbers(collection, k):
    result = []
    counter = 0
    kth_number = QuickSelect(collection, k)
    for value in collection:
        if value < kth_number:
            result.append(value)
            counter += 1
    for value in collection:
        if value == kth_number and counter < k:
            result.append(value)
            counter += 1
    return result
    
if __name__ == "__main__":
    collection = input("enter the numbers:")
    k = input("enter k:")
    result = FindKSmallestNumbers(collection, k)
    print result
