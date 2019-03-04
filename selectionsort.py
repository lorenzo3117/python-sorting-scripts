# Python program for implementation of Selection sort
# https://www.geeksforgeeks.org/selection-sort/
# https://pastecode.xyz/view/44912854#L17
import sys
import timeit


### Function ###
def selectionSort(arr):
    checks = 0

    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        checks += 1

    print(checks)


# Array
arr =

# Sort array
print(timeit.timeit('selectionSort(arr)', 'from __main__ import selectionSort, arr', number=1))
