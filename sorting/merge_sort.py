import unittest

## MERGE SORT
# Divide & Conquer algorithm. Break down the array into sublists until you just get an arr with 1 elem,
# which is always sorted.
# Compare the left and right arr (len(1)) and merge them in the right order, replacing them into the correct idx
# of the original list

## Time: O(n log(n))
### Space: Theta(n log(n))

# for python, slice the array instead of passing indexes
def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.

    >>> lst = [4, 5, 1, 6, 3]
    >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right, lst)


def merge(left, right, lst):
    len_l, len_r= len(left), len(right)
    i, j, k = 0, 0, 0
    while i < len_l and j < len_r:
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len_l:
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len_r:
        lst[k] = right[j]
        j += 1
        k += 1

    return lst

# def merge(L, R):
    # if not L:
    #     return R
    # if not R:
    #     return L
    # if L[0] < R[0]:
    #     return [L[0]] + merge(L[1:], R)
    # return [R[0]] + merge(L, R[1:])


class MergeSortTest(unittest.TestCase):
    def test(self):
        helper = []
        arr = [5, 10, 3, 4, 9, 2]
        self.assertEqual(merge_sort(arr), [2, 3, 4, 5, 9, 10])


if __name__=='__main__':
    unittest.main()
