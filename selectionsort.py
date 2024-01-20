def findSmallest(arr)-> int:
    """ Find index of the smallest element in array"""
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallestIndex = i
            smallest = arr[i]
    return smallestIndex

def selectionSort(arr)->list:
    """ sorting array by selection sort"""
    sortedarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedarr.append(arr.pop(smallest))
    return sortedarr

l = [2, 4, 1, 3, 6, 5]
print(selectionSort(l))