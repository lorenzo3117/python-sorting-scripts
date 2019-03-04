# Python3 Optimized implementation of Bubble sort
# This code is contributed by Shreyanshi Arun 
# https://www.geeksforgeeks.org/bubble-sort/
from random import shuffle

# Function
def bubbleSort(arr): 
    n = len(arr) 
    swaps = 0
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
   
            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
                swaps = swaps + 1
  
        # If no two elements were swapped by inner loop, then break 
        if swapped == False: 
            break
    
    print ("\n Gesorteerde array:")
    print(arr)
    print("\n Hoeveelheid swaps:")
    print(swaps)

# Loop
while True:       
    # Ask how many numbers
    x = int(input("Hoeveel getallen? "))

    # Make array with x numbers in a random order
    arr = [t for t in range(x)]
    shuffle(arr)
    print("\n Originele array:")
    print(arr)

    # Sort the array
    bubbleSort(arr) 