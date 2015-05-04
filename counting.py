'''
counts how many #s there are in an array
runs in O(n + m ) time 
'''
def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in xrange(n):
        count[A[k]] += 1
    return count

'''
check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap
'''
def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
    d //= 2
    count = counting(A, m)
    for i in xrange(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False

# fast_solution([1, 2, 3], [3, 2, 1], 1)

'''
prefix sums
input numbers 1   2   3   4   5   6  ...
prefix sums   1   3   6  10  15  21  ...
''' 
def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for i in xrange(1, n+1):
        P[i] = P[i-1] + A[i-1]
    return P

arr = [1, 2, 3, 4, 5, 6]
prefix_sums(arr)

'''
get totals of an array faster by using prefix sums
'''
def get_total(A):
    prefixed = prefix_sums(A)
    n = len(A)
    return prefixed[n]

print get_total(arr)

def get_total_slice(A, x, y):
    prefixed = prefix_sums(A)
    print prefixed[y+1], prefixed[x], prefixed
    return prefixed[y+1] - prefixed[x]

print get_total_slice(arr, 1, 3)


'''
A non-empty zero-indexed array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
Array A contains only 0s and/or 1s:
0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
Write a function:

'''

# brute force, O(n^2) solution...
def solution(A):
    cars, start = 0, 0
    
    while start < len(A):
        
        rest = A[start+1:]
        i = 0
        while i < len(rest):
            
            if A[start] == 0 and rest[i] == 1:
                cars = cars + 1
            i = i + 1
        start = start + 1
    
    return cars

def solution(A):
    east = [0] * len(A)

    start = 1
    while start < len(A):
        if A[start-1] == 0:
            east[start] = east[start-1] + 1
        else:
            east[start] = east[start-1]
        start = start + 1
       
    cars = 0
    i = 1
    while i < len(A):
        if A[i] == 1:
            cars = cars + (east[i] * 1)
            if cars > 1000000000:
                return -1
        i = i + 1
    return cars