# Imports
import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort

# Main
print()
print("PYTHON SORTING SCRIPTS")
print("----------------------\n")

# Input
ans = True
while(ans):
    n = int(input("How many numbers (between 2 and 50.000; could take a minute or two) do you want in the array? "))
    if n > 50000 or n < 2: print("Can't use that number bro try again")
    else: ans = False
array = random.sample(range(1, n+1), n)

# Sortings
start = time.time()
print(bubbleSort(array.copy()))
print("Time elapsed: ", str(time.time() - start) + "\n")

start = time.time()
print(selectionSort(array.copy()))
print("Time elapsed: ", str(time.time() - start) + "\n")

start = time.time()
print(insertionSort(array.copy()))
print("Time elapsed: ", str(time.time() - start) + "\n")

start = time.time()
print(heapSort(array.copy()))
print("Time elapsed: ", str(time.time() - start) + "\n")

quickSort(array.copy())

# End
input("Press any key to quit...")