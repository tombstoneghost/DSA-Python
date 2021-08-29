def partition(array, low, high):
    i = low  - 1
    pivot = array[high]
    
    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return(i + 1)

def quicksort(array, low, high):
    
    if len(array) == 1:
        return array
    else:
        if low < high:
            pi = partition(array, low, high)
            
            quicksort(array, low, pi - 1)
            quicksort(array, pi + 1, high)
            
            return array