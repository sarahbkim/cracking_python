import unittest

def string_permute(str):
    if len(str) <= 1:
        return [str]

    last_char = str[-1:]
    rest = str[:-1]

    permut_all_but_last = string_permute(rest)
    permutations = []
    possible_positions = range(len(rest)+1)

    for permut in permut_all_but_last:
        for pos in possible_positions:
            permutation = permut[:pos] + last_char + permut[pos:]
            permutations.append(permutation)

    return list(set(permutations))


class StringPermutTest(unittest.TestCase):
    def testSmallestCase(self):
        str = "ab"
        answer = string_permute(str)
        expected = ["ba", "ab"]
        self.assertEqual(answer, expected)

    def testLargerCase(self):
        str = "hello"
        answer = string_permute(str)
        self.assertEqual("[]", answer)


if __name__=='__main__':
    unittest.main()