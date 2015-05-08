#!/usr/bin/python
import unittest

def calculateWaterAmt(l, r, arr):
    filled_amt = 0
    for i in arr[l+1:r]:
        filled_amt += i

    totalArea = min(arr[l], arr[r]) * (abs(l - r) - 1)
    return totalArea - filled_amt

def getWaterFill(arr):
    amt = 0
    if len(arr) <= 2:
        return amt

    curr = 1
    l = curr - 1
    r = curr + 1
    # continue until r is the last element of the list
    while r < len(arr):
        # is R the last elemnet on the list? 
        if r == len(arr)-1:
            # is elem at r and l greater than curr? 
            if arr[r] > arr[curr] and arr[l] >= arr[curr]:
                amt += calculateWaterAmt(l, r, arr)
                return amt
            else:
                return amt
        else:
            # is elem at l greater than curr? 
            if arr[l] > arr[curr]:
                # is eleem at r greater than curr and r + 1 ? 
                if arr[r] > arr[curr] and arr[r] > arr[r+1]:
                    # calculate amt
                    amt += calculateWaterAmt(l, r, arr)
                    # shift l, curr, and r
                    l = r
                    curr = l + 1
                    r = l + 2
                else:
                    # shift curr and r 
                    curr = curr + 1
                    r = r + 1
            else:
                # shift l, curr, and r
                l = curr
                curr = l + 1
                r = curr + 1
        
    return amt


def find_odd_occurence(arr):
    return reduce(lambda x,y: x^y, arr)

def find_sqrt(num):
    for i in xrange(0, num/2):
        if i*i == num:
            return i 
        elif i*i > num:
            return i-1
def find_missing(arr1, arr2):
    result = 0
    for i in arr1 + arr2:
        result ^= i
    return result

def isBalanced(expr):
    if len(expr) % 2 != 0:
        return False
    opening = set('([{')
    stack = []
    match=set([ ('(',')'), ('[',']'), ('{','}') ])
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            lastOpen = stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack) == 0

def reverse_words(string):
    arr = string.split(' ')
    stack = []
    for i in arr:
        stack.append(i)
    reversed_str = ""
    
    while stack:
        reversed_str += stack.pop() + " "

    return reversed_str.strip()

'''
>>> str = "hi this is great"
>>> arr = str.split(' ')
>>> arr
['hi', 'this', 'is', 'great']
>>> [for x in arr]
  File "<stdin>", line 1
    [for x in arr]
       ^
SyntaxError: invalid syntax
>>> [x for x in arr]
['hi', 'this', 'is', 'great']
>>> [x for x in arr[::-1]]
['great', 'is', 'this', 'hi']
'''
def reversed_words_2(string):
    arr = string.split(' ')
    return ' '.join([x for x in arr[::-1]])


'''
search for an elem in a sorted array of unknown length
'''

def find(arr, item):
    idx = 0
    exp = 0

    # find the index 
    while True:
        try:
            if arr[idx] == item:
                return idx
            elif arr[idx] < item:
                # increment the idx more then!
                idx = exp**2
                exp += 1
            else:
                # the arr[idx] is larger than item, so we have our cut off
                break
        except IndexError:
            break

    return b_search(arr, 0, idx-1, item)


def b_search(arr, start, end, item):
    if end < start:
        return -1
    else:
        # need to calculate the mid point correctly!!! 
        mid = start + (end-start)/ 2
        if arr[mid] > item:
            return b_search(arr, 0, mid-1, item)
        elif arr[mid] < item:
            return b_search(arr, mid+1, end, item)
        else:
            return mid

def rain_fall(arr):
    leftMax = 0
    rightMax = len(arr)-1
    i = 1
    while i < len(arr)/2:
        if arr[leftMax] < arr[i]:
            leftMax = i
        if arr[len(arr)-1-i] >= arr[rightMax]:
            rightMax = len(arr)-1-i
        i += 1

    if leftMax < rightMax:
        localMax = min(arr[leftMax], arr[rightMax])
        filled_area = reduce(lambda x, y: x + y, arr[leftMax+1:rightMax])
        return (localMax * (rightMax-leftMax-1)) - filled_area

def remove_duplicates_str(str):
    result = []
    seen = set()

    for i in str:
        if i not in seen:
            seen.add(i)
            result.append(i)
    
    return ''.join(result)

def get_next_largest(num):
    strNum = str(num)
    length = len(strNum)
    for i in xrange(length-2, -1, -1):
        current = strNum[i]
        right = strNum[i+1]
        if current < right:
            # i is our pivot
            temp = sorted(strNum[i:])
            nextNum = temp[temp.index(current)+1]
            temp.remove(next)
            temp = ' '.join(temp)
            return int(strNum[:i]+nextNum+temp)
    return num

def find_word_positions(text):
    # prepopulate the dictionary
    dictionary = {}
    for i, t in enumerate(text):
        # should clean up t here before appending to dict 
        
        if t not in dictionary.keys():
            dictionary[t] = [i]
        else:
            dictionary[t].append(i)
    
    # find the text    
    try:
        return dictionary[key]
    except KeyError:
        return "Text not in dictionary"

def get_permute_str(word):
    if len(word) == 0:
        return ['']
    permutes = get_permute_str(word[1:])
    answers = []

    for i in xrange(len(permutes)):
        for j in xrange(len(word)):
            newWord = permutes[i][0:j] + word[0] + permutes[i][j:len(word)-1]
            answers.append(newWord)
    return answers



class ArgoTests(unittest.TestCase):
    def test_get_permute_str(self):
        self.assertEqual(get_permute_str("cat"), ['cat', 'act', 'atc', 'cta', 'tca', 'tac'])

    def test_remove_duplicate_str(self):
        self.assertEqual(remove_duplicates_str("tree traversal"), "tre avsl")

        
    def test_rain_fall(self):
        self.assertEqual(rain_fall([2, 5, 1, 3, 1, 2, 1, 7, 7, 6]), 17)
    def test_find(self):
        self.assertEqual(find([1, 3, 5, 6, 8, 9, 10, 11, 34], 6), 3)

    def test_reverse_words(self):
        self.assertEqual(reverse_words("Hi this is great"), "great is this Hi")

    def test_isBalanced(self):
        self.assertEqual(isBalanced(['(', '{', '}', ')']), True)
        self.assertEqual(isBalanced(['(', '{', ')', '}']), False)
        self.assertEqual(isBalanced(['(', '{', ')', '}', ')']), False)


    def test_find_missing(self):
        self.assertEqual(find_missing([1, 2, 3], [2, 3]), 1)

    def test_find_sqrt(self):
        self.assertEqual(find_sqrt(8), 2)
        self.assertEqual(find_sqrt(9), 3)

    def test(self):
        arr = [0,1,2,1,0]
        self.assertEqual(getWaterFill(arr), 0)
        arr2 = [0,3,1,2,3,0]
        self.assertEqual(getWaterFill(arr2), 3)
        arr3 = [0,2,1,2,1,2,0]
        self.assertEqual(getWaterFill(arr3), 2)
        arr4 = [0,3,1,2,1,4,0,3,0] 
        self.assertEqual(getWaterFill(arr4), 5)


if __name__ == '__main__':
    unittest.main()