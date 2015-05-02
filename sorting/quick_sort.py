import unittest

### QUICK SORT
# Divide & Conquer algorithm. Break down the array into sublists until you just get an arr with 1 elem,
# which is always sorted.

## Time: O(n log(n)) average, O(n^2) worst
# worst case scenario avoided with randomized Quick sort
# an efficient sorting algo

# in-place algorithm

## PSEUDOCODE
# partition the list from a pivot (i.e. last element in the list
# then split the list to L and R and partition again


## quick sort
def quick_sort(arr, start, end):
    if start < end:
        idx = partition(arr, start, end)
        quick_sort(arr, start, idx - 1)
        quick_sort(arr, idx + 1, end)
    return arr

## partition
# select pivot and move elems less than pivot to left, others towards the right
# returns pivot idx to the quick sort
# params: arr, start, end
def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    i = start
    while i < end:
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
        i += 1

    arr[p_index], arr[end] = arr[end], arr[p_index]

    return p_index



class QuickSortTest(unittest.TestCase):
    def test(self):
        arr = [5, 10, 3, 4, 1]
        self.assertEquals(quick_sort(arr, 0, len(arr)-1), [1, 3, 4, 5, 10])

if __name__ == '__main__':
    unittest.main()