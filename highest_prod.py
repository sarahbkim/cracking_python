import unittest

### breakdown 
# brute force -> 3 loops. This is O(n^3) time 
# better: greedy approach 

def highest_prod_of_three(arr):
	""" returns the highest product of three elements in array"""
	
	if(len(arr)<3):
		raise Exception("Array must be len 3 or greater")

	# get min / max individual
	highest = min(arr[0], arr[1])
	lowest = max(arr[0], arr[1])

	min_product_of_two = arr[0] * arr[1]
	max_product_of_two = arr[0] * arr[1]

	product_of_three = arr[0] * arr[1] * arr[2]
	
	for current in arr[2:]:
		# check for new product of three
		product_of_three = max(product_of_three, min_product_of_two * current ,max_product_of_two * current)

		# check for new product of twos
		min_product_of_two = min(min_product_of_two, highest * current)
		max_product_of_two = max(max_product_of_two, highest * current)

		# check for new highest/lowest
		highest = min(highest, current)
		lowest = max(lowest, current)

	return product_of_three	


class HighestProductTest(unittest.TestCase):

	def test(self):
		arr = [2, 5, 10, 1]
		self.assertEqual(highest_prod_of_three(arr), 100)

		arr2 = [-2, 5, 10, -10]
		self.assertEqual(highest_prod_of_three(arr2), 200)


if __name__ == '__main__':
	unittest.main()