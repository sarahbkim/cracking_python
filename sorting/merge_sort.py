import unittest

## MERGE SORT
# Divide & Conquer algorithm. Break down the array into sublists until you just get an arr with 1 elem,
# which is always sorted.
# Compare the left and right arr (len(1)) and merge them in the right order, replacing them into the correct idx
# of the original list

## Time: O(n log(n))
### Space: Theta(n log(n))

# # for python, slice the array instead of passing indexes

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
    # split the array if len(arr) is greater than 1
        # calculate mid point
        mid = len(arr)/2
        # get L and R sides
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # merge both sides
        return merge(left, right, arr)


def merge(left, right, arr): 
    len_l, len_r = len(left), len(right)
    i, j, k = 0, 0, 0

    while i < len_l and j < len_r:
        # if left item is smaller, update the original array
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len_l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


class MergeSortTest(unittest.TestCase):
    def test(self):
        helper = []
        arr = [5, 10, 3, 4, 9, 2]
        self.assertEqual(merge_sort(arr), [2, 3, 4, 5, 9, 10])


if __name__=='__main__':
    unittest.main()
