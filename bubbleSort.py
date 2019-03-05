# Python3 Optimized implementation of Bubble sort
# This code is contributed by Shreyanshi Arun
# https://www.geeksforgeeks.org/bubble-sort/
# https://pastecode.xyz/view/44912854#L17
import timeit


### Function ###
def bubbleSort(arr):
    n = len(arr)
    checks = 0

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                checks += 1

        # If no two elements were swapped by inner loop, then break
        if swapped == False:
            break

    print(checks)


# Array
arr =


# Sort array
print(timeit.timeit('bubbleSort(arr)', 'from __main__ import bubbleSort, arr', number=1))
