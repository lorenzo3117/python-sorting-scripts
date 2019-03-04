# Python program for implementation of Insertion Sort
# This code is contributed by Mohit Kumra
# https://www.geeksforgeeks.org/insertion-sort/
# https://pastecode.xyz/view/44912854#L17
import timeit


### Function ###
def insertionSort(arr):
    checks = 0

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        checks += 1

    print(checks)


# Array
arr =


# Sort array
print(timeit.timeit('insertionSort(arr)', 'from __main__ import insertionSort, arr', number=1))
