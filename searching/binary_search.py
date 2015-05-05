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


def binary_search(arr, item):
    n = len(arr)
    if n < 1:
        return -1
    else:
        mid = n/2
        if arr[mid] == item:
            return mid
        else:
            return binary_search(arr[0: mid], item)
            return binary_search(arr[mid+1, n-1], item)


class binary_search_test(unittest.TestCase):
    def test(self):
        arr = [2, 3, 1, 4, 5]
        self.assertEquals(binary_search(arr, 1), 2)

        arr2 = [1]
        self.assertEquals(binary_search(arr2, 1), 0)

        arr3 = [2, 4, 10, -30, 8, 7]
        self.assertEquals(binary_search(arr3, -30), 3)

        self.assertEquals(binary_search(arr2, 10), -1)
        self.assertEquals(binary_search(arr3, 1), -1)


if __name__ == '__main__':
    unittest.main()