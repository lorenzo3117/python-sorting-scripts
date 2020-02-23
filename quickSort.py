#https://stackoverflow.com/questions/18262306/quicksort-with-python
import time

comparisons = 0
swaps = 0

def quickSort(arr):
    start = time.time()
    sort(arr)
    end = time.time()
    print("QUICK SORT\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps))
    print("Time elapsed: ", str(end - start) + "\n")

def sort(array):
    """Sort the array by using quicksort."""
    global comparisons
    global swaps

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[len(array)-1]
        for x in array:
            if x < pivot:
                comparisons += 1
                less.append(x)
            elif x == pivot:
                comparisons += 1
                equal.append(x)
            elif x > pivot:
                comparisons += 1
                greater.append(x)
        # Don't forget to return something!
        swaps += 1
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array