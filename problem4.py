import numpy as np

def ispalindrome(n):
	"""
	checks whether the integer n is a palindrome
	"""
	s = str(n)
	return s == s[::-1]
	
def largestpalindrome(N):
	"""
	finds the largest palindrome that is a product of N-digit positive integers
	"""	
	maxpalindrome = 0
	for j1 in range(10**(N-1),10**N):
		for j2 in range(10**(N-1),10**N):
			if ispalindrome(j1*j2):
				maxpalindrome = max(maxpalindrome, j1*j2)
	
	return maxpalindrome
				
def test():
	n1 = 1001
	n2 = 4052
	print(ispalindrome(n1))
	print(ispalindrome(n2))

def main():
	N = 4
	print(largestpalindrome(N))	
	
if __name__ == "__main__":
	#test()
	main()
