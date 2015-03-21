import unittest

# Here's a formal algorithm:

# If the end time of the first meeting is equal to or greater than the start time of the second meeting,
	# we merge the two meetings into one time range. 
	# The resulting time range's start time is the first meeting's start, and its end time is the later of the two meetings' end times.
# Else, we leave them separate.

# for faster, sort the array 
# O(nlog(n)) time 

def overlapped_times(arr):
	""" takes an array of tuples and outputs an array of tuples with times merged """
	# sort the array of tuples
	arr.sort()
	new_arr = []
	i = 0

	while i < len(arr)-1:
		start_time = arr[i][0]
		end_time = arr[i][1]

		if(arr[i][1]>=arr[i+1][0]): # if prev end time is after or same as next start time
			end_time = max(arr[i+1][1], arr[i][1])
			start_time = min(arr[i][0], arr[i+1][0])
			i+=1

		new_arr.append((start_time, end_time))
		i += 1

	print new_arr
	return new_arr


class MeetingsTest(unittest.TestCase):

	def test(self):
		meetings = [(1, 3), (2, 4)]
		print "works when first meeting ends after second meeting begins"
		self.assertEqual(overlapped_times(meetings), [(1, 4)])

		meetings2 = [(1, 2), (2, 4)]
		print "works when they end and start at the same time"
		self.assertEqual(overlapped_times(meetings2), [(1, 4)])

		meetings3 = [(1, 5), (2, 3)]
		print "works when first mtg ends before 2nd meeting begins"
		self.assertEqual(overlapped_times(meetings3), [(1, 5)])
		
		meetings4 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
		print "works for a long array of tuples"
		self.assertEqual(overlapped_times(meetings4), [(0, 1), (3, 8), (9, 12)])


if __name__ == '__main__':
	unittest.main()