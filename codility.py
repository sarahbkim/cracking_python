# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
# how to run this in constant time.. 
''' 
X is starting
Y is ending
D is steps
'''
def solution1(X, Y, D):
    times = (Y - X) / D
    passed = X + (D * times)
    
    while passed < Y:
        times = times + 1
        passed = passed + D
    return times

X = 10
Y = 85 
D = 30
# solution2(X, Y, D)


# you can use print for debugging purposes, e.g.
# print "this is a debug message"
# [2, 3, 1, 5]

# possible: 
# sort the array
# find the missing elem. 
# this takes O(2 n log n) time

def solution2(A):
    # write your code in Python 2.7
    if len(A) > 1:
        A.sort()
        for i, x in enumerate(A):
            if len(A)-1 > i:
                if A[i+1] - A[i] > 1:
                    return A[i+1] - 1
    else:
        raise ValueError('A must be an array greater than length 1')


'''
Task description
A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
def solution(A)
that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
Assume that:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:
expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
'''

matrix = [[5, 4, 4],
            [4, 3, 4],
            [3, 2, 4]]

matrix2 = [[4, 4, 4],
            [0, 3, 4]]
# country  = 6


def matrixIterate(A):
    countries = []

    for i, x in enumerate(A):
        for j, y in enumerate(A[i]):
            if type(A[i][j]) != None:
                country = checkNeighbors(A, i, j) 
                if country not in countries:
                    countries.append(country)
                A[i][j] = None
    return len(countries)-1
    
def checkNeighbors(A, x, y):
    startVal = A[x][y]
    neighbors = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

    for neighbor in neighbors:
        if neighbor[0] >= 0 and neighbor[0] <= len(A)-1 and neighbor[1] >= 0 and neighbor[1] <= len(A[x])-1:
            if A[neighbor[0]][neighbor[1]] != None and startVal == A[neighbor[0]][neighbor[1]]: # check if same country
                checkNeighbors(A, neighbor[0], neighbor[1])
                A[neighbor[0]][neighbor[1]] = None # to signify checked
            return countries



'''
Task description
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
'''
def findMissingElement(A):
    if len(A) == 0:
        return 1
    else:
        n = len(A) + 1
        expected_sum = n * (n + 1) / 2

        sum = reduce(lambda x, y: x + y, A)
        return expected_sum - sum


# A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1]and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7 
# P = 2, difference = |4 − 9| = 5 
# P = 3, difference = |6 − 7| = 1 
# P = 4, difference = |10 − 3| = 7 

def findMinCombination(A):
    # write your code in Python 2.7
    P = 1
    smallest = float("inf")
    
    while P < len(A)-1:
        first_split_end = A[P-1]
        second_split_end = A[len(A)-1]
        first_sum = reduce(lambda x, y: x + y, A[0:P])
        second_sum = reduce(lambda x, y: x + y, A[P:len(A)])
        smallest = min(smallest, abs(first_sum - second_sum))
        P = P + 1
    return smallest

# this is O(N*N) complexity... 

def findMinCombination2(A):
    start = 1
    left_sum = A[start-1]
    right_sum = reduce(lambda x, y: x + y, A[start:len(A)])
    smallest = float("inf")

    # need to test if the array is just a 2 element arr... 
    if len(A) < 3:
        return abs(left_sum-right_sum)
    else:
        while start < len(A)-1:
            left_sum = left_sum + A[start]
            right_sum = right_sum - A[start]
            smallest = min(smallest, abs(left_sum - right_sum))
            start = start + 1

        return smallest


# that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer that does not occur in A.

# For example, given:
#   A[0] = 1
#   A[1] = 3
#   A[2] = 6
#   A[3] = 4
#   A[4] = 1
#   A[5] = 2
# the function should return 5.

# O(n) time and O(1) space 
# segregate pos and neg numbers  so all non-pos to left side of arr
# ignore non-positive elements for now & traverse through the arr 
    # mark presence of element x, change sign val at index x to neg 
    # traverse arr again and print first idx with pos val 

# the below soluation doesn't work ... 
def segregate(A):
    # return idx for pos start
    j = 0
    for idx, x in enumerate(A):
        if x <= 0:
            A[j], A[idx] = x, A[j]
            j = j + 1
    return j


def find_missing_positive(A):
    if len(A)<=1:
        try:
            return A[0]
        except:
            return 0
    
    target_arr = [None] * (len(A) + 1)
    minIdx = min(A)
    for i in A:
        target_arr[i-minIdx] = i
    for idx, t in enumerate(target_arr):
        if t == None:
            next_min = target_arr[idx-1]
            return next_min + 1


def find_missing_neg_in_arr(A):
    start = segregate(A)
    return find_missing_positive(A[start:])



class CodilityTests(unittest.TestCase):
    def test(self):
        # test normal case
        arr = [3, 1, 2, 4, 3]
        self.assertEqual(findMinCombination2(arr), 1)

        # test two element array
        arr2 = [1, 3]
        self.assertEqual(findMinCombination2(arr2), 2)

    def segregate_test(self):
        arr = [3, -10, 4, -1, 2]
        self.assertEqual(segregate(arr), 2)
        
        arr3 = [-30, 0, 4]
        self.assertEqual(segregate(arr3), 2)
        
        arr2 = [3, -1]
        self.assertEqual(segregate(arr2), 1)

        arr4 = [0, -1]
        self.assertEqual(segregate(arr4), 2)

    def find_missing_positive_test(self):
        arr = [1, 3, 6, 4, 1, 2]
        self.assertEqual(find_missing_positive(arr), 5)

        arr2 = []
        self.assertEqual(find_missing_positive(arr2), [])
        
        arr4 = [30, 28, 31, 27, 26]
        self.assertEqual(find_missing_positive(arr4), 29)

    def find_missing_neg_in_arr_test(self):
        arr = [-30, -28, 0, -31, -27, 3, -26, 1]
        self.assertEqual(find_missing_neg_in_arr(arr), 2)

        arr2 = [-30, 0, 4, -6, 2, 4]
        self.assertEqual(find_missing_neg_in_arr(arr2), 3)


if __name__ == '__main__':
    unittest.main()
