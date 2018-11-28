# Use binary search to find the key in the list
"""
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return low - 1 # Now high < low, key not found
"""

def recursiveBinSearch(list, key):
    low = 0
    high = len(list) - 1
    return recursiveBinSearchHelper(list, key, low, high)

def recursiveBinSearchHelper(list, key, low, high):
    if low > high: #exhausted without a match
        return -low - 1
    mid = (low + high) // 2
    if key < list[mid]:
        return recursiveBinSearchHelper(list, key, low, mid - 1)
    elif key == list[mid]:
        return mid
    else:
        return recursiveBinSearchHelper(list, key, mid + 1, high)

def main():
    list = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursiveBinSearch(list, 3))
    print(recursiveBinSearch(list, 4))

main()