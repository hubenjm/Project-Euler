import numpy as np

def sumevenfib(N):
	"""
	N is a positive number
	This function will add up all even fibonacci numbers that do not exceed N
	We use the convention that F_0 = 0, F_1 = 1,...,F_3 = 2
	Note that F_3k is the subsequence of even Fibonacci numbers
	"""
	
	F1 = 1
	F0 = 0
	S = 0
	while F0 <= N:
		S += F0
		F3 = 2*F1 + F0
		F1 = F3 + F1 + F0
		F0 = F3
	return S
	
def main():
	N = 4000000
	print(sumevenfib(N))

	
if __name__ == "__main__":
	main()
