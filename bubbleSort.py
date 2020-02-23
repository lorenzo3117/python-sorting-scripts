# Python3 Optimized implementation of Bubble sort
# This code is contributed by Shreyanshi Arun
# https://www.geeksforgeeks.org/bubble-sort/

### Function ###
def bubbleSort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if swapped == False:
            break

    return "\nBubble Sort:\nComparisons: " + str(comparisons) + "\nSwaps: " + str(swaps)