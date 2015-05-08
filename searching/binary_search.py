#!/usr/bin/python
import unittest

# def binary_search(arr, item):
#     if len(arr)==0:
#         return -1
#     else:
#         mid = len(arr)/2
#         if item == arr[mid]:
#             return mid
#         else:
#             return binary_search(arr[0:mid-1], item)  # left side
#             return binary_search(arr[mid+1:-1], item)


# def binary_search(arr, item):
#     n = len(arr)
#     if n < 1:
#         return -1
#     else:
#         mid = n/2
#         if arr[mid] == item:
#             return mid
#         else:
#             return binary_search(arr[0: mid], item)
#             return binary_search(arr[mid+1, n-1], item)

def binary_search(arr, start, end, item):
    if end < start:
        return -1
    else:

        mid = start + (end-start)/2
        if arr[mid] > item:
            return binary_search(arr, 0, mid-1, item)
        elif arr[mid] < item:
            return binary_search(arr, mid+1, end, item)
        else:
            return mid

class binary_search_test(unittest.TestCase):
    def test(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEquals(binary_search(arr, 0, len(arr)-1, 4), 3)

        arr2 = [1]
        self.assertEquals(binary_search(arr2, 0, len(arr2)-1, 1), 0)
        self.assertEquals(binary_search(arr2, 0, len(arr2)-1, 10), -1)

        arr3 = [-30, 2, 4, 7, 8, 10]
        self.assertEquals(binary_search(arr3, 0, len(arr3)-1, -30), 0)
        self.assertEquals(binary_search(arr3, 0, len(arr3)-1, 1), -1)


if __name__ == '__main__':
    unittest.main()