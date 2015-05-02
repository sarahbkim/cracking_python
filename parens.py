import unittest

def parens(sentence, pos):
    arr = list(sentence)
    stack = []

    for i, x in enumerate(arr):
        if x == '(':
            stack.append(i)
        if x == ')':
            l = stack.pop()
            if l == pos:
                return i

    raise Exception("No closing parenthesis :(")


class ParensTest(unittest.TestCase):
    def test(self):
        sent = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
        self.assertEqual(parens(sent, 10), 79)

    def test2(self):
        sent2 = "Hello (I love (it when))"
        self.assertEqual(parens(sent2, 6), 23)
        self.assertEqual(parens(sent2, 14), 22)


if __name__ == '__main__':
  unittest.main()