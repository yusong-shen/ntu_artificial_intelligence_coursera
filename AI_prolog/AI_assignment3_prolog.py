"""
AI assignment 3

prolog

2014.12.17
"""

def pre(A, B):
	"""
	determine whether A is the prefix of list B
	if A is None, then output all the possible prefix
	of B
	"""
	result = []
	if A == None:
		for i in range(len(B)):
			result.append(B[:i])
		return result
	else:
		if len(A) > len(B):
			return False
		for i in range(len(A)):
			if A[i] != B[i]:
				return False
		return True


def rev(A, B):
	"""
	determine whether list A and B are reversed lists
	if yes, return True
	"""
	if len(A) != len(B):
		return False
	else:
		for i in range(len(A)):
			# print A[i],B[len(A)-1-i]
			if A[i] != B[len(A)-1-i]:
				return False
		return True

def maxsum(A):
	"""
	computer a subarray that has maximum sum in all the subarray
	return its sum
	by using dynamic programming
	"""
	max_ending_here = max_so_far = A[0]
	for x in A[1:]:
		max_ending_here = max(x, max_ending_here + x)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far	



def test():
	"""
	"""
	B1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	B2 = [3, 4, 5]
	A1 = [-2, 1, -3]
	A2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 100]
	A3 = [3, 1, 2]
	A4 = None 
	A5 = [5, 4, 3]
	assert maxsum(B1) == 6
	assert pre(A1, B1) == True
	assert pre(A2, B1) == False
	assert pre(A3, B1) == False
	print pre(A4, B1)
	assert rev(A1, B2) == False
	# rev(A5, B2)
	assert rev(A5, B2) == True
test()



 