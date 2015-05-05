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


# ## quick sort



def quicksort(arr, start, end):
    if start < end:
        idx = partition(arr, start, end)
        quicksort(arr, start, idx-1)
        quicksort(arr, idx+1, end)
    return arr


# ## partition
# # select pivot and move elems less than pivot to left, others towards the right
# # returns pivot idx to the quick sort
# # params: arr, start, enddef partition2(arr, start, end):
def partition(arr, start, end):
    pivot = arr[end] # choose last element to be the pivot
    p_idx = start # have p_idx at start of arr

    i = start 
    while i < end:
        # if item is less than pivot, then swap the items
        if arr[i] <= pivot:
            arr[i], arr[p_idx] = arr[p_idx], arr[i]
            # increment p index
            p_idx += 1
        i += 1
    # swap the pivot item with current p_idx 
    arr[p_idx], arr[end] = arr[end], arr[p_idx]
    return p_idx


class QuickSortTest(unittest.TestCase):
    def test(self):
        arr = [5, 10, 3, 4, 1]
        self.assertEquals(quicksort(arr, 0, len(arr)-1), [1, 3, 4, 5, 10])

    def test2(self):
        arr = [6, 10, 3, 4, 1, 10, 3, 4, 1]
        self.assertEquals(quicksort(arr, 0, len(arr)-1), [1, 1, 3, 3, 4, 4, 6, 10, 10])

if __name__ == '__main__':
    unittest.main()