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
print prefix_sums(arr)


