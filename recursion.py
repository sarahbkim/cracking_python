# -*- coding: utf-8 -*-
#!/usr/bin/python
import unittest
import math, re, string

def combos(arr):
    c = []
    if len(arr)<=1:
        c.append(arr)
        return c
    else:
        start = 0
        for i in xrange(len(arr)):
            c.append(arr[start:i+1])
        return c + combos(arr[1:])


def setCombos(arr):
    subsets = []
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr)+1:
            subset = arr[i:j]
            subsets.append(subset)
            j+=1
        i+= 1

    return subsets


def setComboRecursive(arr):
    subsets = []
    if len(arr)>=1:
        j = 1
        while j < len(arr)+1:
            subset = arr[0:j]
            subsets.append(subset)
            j += 1
        subsets += setComboRecursive(arr[1:])
    return subsets

setComboRecursive([1, 2, 3])

# generate nth Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)
'''
Imagine a robot sitting on the upper left hand corner of an NxN grid 
The robot can only move in two directions: right and down 
How many possible paths are there for the robot?
'''
def robot_moves(x, y):
    # at each move, either go down or go left
    if x == 1 or y == 1:
        return 1
    else:
        return robot_moves(x-1, y) + robot_moves(y, x-1)

def robot_moves_math(x, y):
    return math.factorial(x-1 + y-1)/(math.factorial(x-1) * math.factorial(y-1))


'''
Write a method to compute all permutations of a string
'''
def permute_strings(s):
    if len(s) == 0:
        return ['']
    else:
        rest_strings = permute_strings(s[1:])
        next_list = []
        for i in xrange(len(rest_strings)):
            for j in xrange(len(s)):
                new_string = rest_strings[i][0:j] + s[0] + rest_strings[i][j:len(s)-1]
                if new_string not in next_list:
                    next_list.append(new_string)
        return next_list

'''
Implement an algorithm to print all valid (e g , properly opened and closed) 
combi- nations of n-pairs of parentheses

>>> parens_combo(3)
()()(), ()(()), (())(), ((()))

'''
def balanced_parens(n):
    return helper(0, n)
    
def helper(unmatched, to_match):
    if to_match == 0:
        return [""]
    
    res = []
    if unmatched < to_match:
        tails = helper(unmatched + 1, to_match)

        res.extend("(" + tail for tail in tails)
    if unmatched > 0:
        tails = helper(unmatched - 1, to_match - 1)
        res.extend(")" + tail for tail in tails)
    return res

def combo_n_cents(n):
    coinsOptions = [1, 5, 10, 25]
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # return sum([combo_n_cents(n-coin) for coin in coinsOptions])
        return combo_n_cents(n-25) + combo_n_cents(n-10) + combo_n_cents(n-5) + combo_n_cents(n-1)

'''
8 queens on chess board. can't share col, row, or diagnols 
chess board is an 8 by 8 array of arrays
'''
def queens():
    board = [[None] * 8] * 8
    first_move = (0,0)

'''
makes the move, marks out now impossible moves, and returns range of legal moves
'''
def make_move(move):
    x = move[0]
    y = move[1]
    # set queen at move
    if board[x][y] == None:
        board[x][y] = 'Q'


def isPal(s):
    s = removeSpaces(s)
    for i in xrange((len(s)-1)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def removeSpaces(s):
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in s if ch not in exclude)
    arr = s.lower().split(' ')
    cleaned = []
    for i in arr:
        if re.match(r"([A-Za-z])", i):
            cleaned.append(i)
    return ''.join(cleaned)

class recursionTests(unittest.TestCase):
    def test_removeSpaces(self):
        self.assertEquals(removeSpaces('hi my , name'), 'himyname')

    def test_pal(self):
        self.assertEquals(isPal('kayak'), True)
        self.assertEquals(isPal("kayak"), True)
        self.assertEquals(isPal("aibohphobia"), True)
        self.assertEquals(isPal("Live not on evil"), True)
        self.assertEquals(isPal("Reviled did I live, said I, as evil I did deliver"), True)
        self.assertEquals(isPal("Able was I ere I saw Elba"), True)
        self.assertEquals(isPal("Kanakanak"), True)
        self.assertEquals(isPal("Wassamassaw"), True)

    def test_cents(self):
        self.assertEquals(combo_n_cents(5), 2)

    def test_parens_combo(self):
        self.assertEquals(balanced_parens(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])

    def test_permutations(self):
        self.assertEquals(permute_strings('cat'), ['cat', 'act', 'atc', 'cta', 'tca', 'tac'])

    def test_fib(self):
        self.assertEquals(fib(3), 2)
        self.assertEquals(fib(19), 4181)

    def test_robot_moves(self):
        self.assertEquals(robot_moves(3, 3), 6)
        self.assertEquals(robot_moves(1, 1), 1)

    def test_robot_moves_math(self):
        self.assertEquals(robot_moves_math(3, 3), 6)
        self.assertEquals(robot_moves_math(1, 1), 1)


if __name__ == '__main__':
    unittest.main()