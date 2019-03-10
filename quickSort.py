# Python program for implementation of Quicksort Sort
# This code is contributed by Mohit Kumra
# https://www.geeksforgeeks.org/quick-sort/
# https://pastecode.xyz/view/44912854#L17
import time


swaps = 0

# This function takes last element as pivot, places the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot
def partition(arr,low,high):
    global swaps
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # Increment index of smaller element
            i = i+1
            #swaps += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick Sort
def quickSort(arr,low,high):
    global swaps

    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr,low,high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

        swaps += 1




# Array
arr = [14,9,5,7,18,12,15,6,10,8,13,2,4,16,1,3,0,17,18,11]

# Sort array
n = len(arr)
start = time.time()
quickSort(arr,0,n-1)
end = time.time()
print(end - start)

print("Swaps: ")
print(swaps)
