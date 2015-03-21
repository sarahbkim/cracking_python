s = 'hello'
s1 = 'x'
s2 = 'critan'

def unique_string(s):
    # return True if it's just a single char
    if len(s)==1: 
        return True
    
    # otherwise loop
    for i, x in enumerate(s):
        start = s[i]
        if(i<len(s)-1):
            if (start==s[i+1]):
                return False
    return True

unique_string(s)
unique_string(s1)
unique_string(s2)

def unique_arr(arr):
    uniques = []
    # returns a new array of just uniques
    for x in arr:
        if x not in uniques:
            uniques.append(x)
    return uniques

arr = [1, 3, 10, 4, 3, 1]
unique_arr(arr) # runs in linear time O(n)
