import numpy as np
import math

def isprime(n):
	if n == 1 or n%2 == 0 or n%3 == 0: return False
	elif n < 9: return True
	
	m = int(math.sqrt(n)) + 1
	i = 5
	while i <= m:
		if n%i == 0 or n%(i+2) == 0:
			return False
		i = i + 6
	return True
	
def nthprime(N):
	if N == 1: return 2
	p = 3
	i = 2
	while i < N:
		p += 2
		if isprime(p):
			i += 1
	return p
	
def main():
	print(nthprime(10001))
	
if __name__ == "__main__":
	main()
