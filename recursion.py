

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