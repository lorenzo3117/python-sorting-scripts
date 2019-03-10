# Python program for implementation of Insertion Sort
# This code is contributed by Mohit Kumra
# https://www.geeksforgeeks.org/insertion-sort/
# https://pastecode.xyz/view/44912854#L17
import timeit


### Function ###
def insertionSort(arr):
    comparisons = 0
    swaps = 0

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        position = i-1

        while key < arr[position] and position >= 0:
            arr[position + 1] = arr[position]
            position -= 1
            swaps += 1

        arr[position+1] = key


    print("Comparisons = swaps: ")
    print(swaps)


# Array
arr = 

# Sort array
print(timeit.timeit('insertionSort(arr)', 'from __main__ import insertionSort, arr', number=1))
