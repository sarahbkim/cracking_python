import unittest

## SELECTION SORT
# loop through the list, find the min and swap with current until
# at end of list
# you can actually just loop from 0..n-2


## PSEUDOCODE
# def selectionSort(arr):
#     for i to n-2:
#         min_i = i
#         for j = i + 1 to n-1:
#             if arr[j] < a[min_i]:
#                 min_i = j
#
#         temp = arr[i]
#         arr[i] = arr[min_i]
#         arr[min_i] = temp
#


## ALGORITHM
# Running time: O(n^2)
def selectionSort(arr):
    i = 0
    while i < len(arr)-1:
        min_i = i  # set min idx to 0 at start
        j = i + 1 # j is one after i
        while j < len(arr):
            if arr[j] < arr[min_i]: # compare values at j and min_i
                min_i = j
            j += 1
        arr[i], arr[min_i] = arr[min_i], arr[i] #swap
        i += 1
    return arr


## TEST
class selectionSortTest(unittest.TestCase):
    def test(self):
        arr = [4, 1, 5, 10, 3, 2]
        self.assertEqual(selectionSort(arr), [1, 2, 3, 4, 5, 10])

    def test2(self):
        arr = [100, 2, 4]
        self.assertEqual(selectionSort(arr), [2, 4, 100])

if __name__=='__main__':
    unittest.main()