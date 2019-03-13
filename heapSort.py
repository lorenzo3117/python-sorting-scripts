# https://stackoverflow.com/questions/13979714/heap-sort-how-to-sort
swaps = 0


def swap(i, j):
    global swaps
    sqc[i], sqc[j] = sqc[j], sqc[i]
    swaps += 1

def heapify(end,i):
    l=2 * i + 1
    r=2 * (i + 1)
    max=i
    if l < end and sqc[i] < sqc[l]:
        max = l
    if r < end and sqc[max] < sqc[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)

def heap_sort():
    end = len(sqc)
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)

sqc = [0,4,2,1,6,8,3,9,5,7]

heap_sort()
print(sqc)
print("Swaps: ")
print(swaps)
