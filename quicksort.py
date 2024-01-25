def quicksort(array) -> list:
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

lst = [3, 2, 4, 1, 6, 7, 5, 9, 8]
print(quicksort(lst))