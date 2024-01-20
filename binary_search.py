def binary_search(list : list, item):
    """Algorithm of classic realization of binary search
    input: list of items and item for search
    output: index of item or None if item does not exist"""

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



lst = [1, 2, 3, 4, 5, 6, 11]
print(binary_search(lst, 11))