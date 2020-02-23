# https://stackoverflow.com/questions/56180411/how-to-count-the-amount-of-swaps-made-in-insertion-sort

def insertionSort(array):
    swapsmade = 0
    checksmade = 0

    for f in range(len(array)):
        value = array[f]
        valueindex = f
        checksmade += 1
        # moving the value
        while valueindex > 0 and value < array[valueindex-1]:
            array[valueindex] = array[valueindex-1]
            valueindex -= 1
            checksmade += 1
            swapsmade += 1 #  Move inside the while loop
        array[valueindex] = value
    
    return "INSERTION SORT:\nComparisons: " + str(checksmade) + "\nSwaps: " + str(swapsmade)