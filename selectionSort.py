# Python program for implementation of Selection sort
# https://www.geeksforgeeks.org/selection-sort/
# https://pastecode.xyz/view/44912854#L17
import timeit


### Function ###
def selectionSort(arr):
    comparisons = 0
    swaps = 0

    # Traverse through all array elements
    for i in range(0, len(arr) - 1):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    print("Comparisons: ")
    print(comparisons)
    print("Swaps: ")
    print(swaps)


# Array
arr =

# Sort array
print(timeit.timeit('selectionSort(arr)', 'from __main__ import selectionSort, arr', number=1))
