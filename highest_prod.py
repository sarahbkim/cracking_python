arr = [2, 5, 10, 33, -100]

def highest_prod(arr):

# breakdown 

# brute force -> 3 loops. This is O(n^3) time 

# better: greedy approach 
# start with the product of first 3 elements
# keep highest and lowest numbers (min, max)
# keep highest sum of 2 numbers and lowest sum of 2 numbers 
