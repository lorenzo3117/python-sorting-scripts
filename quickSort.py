# https://www.youtube.com/watch?v=RFyLsF9y83c&list=WL&index=86&t=0s
# https://pastecode.xyz/view/44912854#L17
from random import randint
import time

def quickSort(arr):

    if len(arr) <= 1: return arr
    smaller, equal, larger = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for x in arr:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)

    return quickSort(smaller) + equal + quickSort(larger)


# Array
arr = 

# Sort array
start = time.time()
sortedArr = quickSort(arr)
end = time.time()

print("Unsorted: ", arr)
print("Sorted: ", sortedArr)
print("Time: ", end - start)
