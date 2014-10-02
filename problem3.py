import numpy as np
import math

def smallestfactor(n):
	m = int(math.sqrt(n))+1
	i = 2
	while (i <= m):
		i += 1
		if n%i == 0:
			return i
	return n # in this case n is prime
	
def largestprimefactor(n):
	p = smallestfactor(n)
	while(p < n):
		n = n/p
		p = smallestfactor(n)
	return n

def main():
	n = 600851475143
	q = 7*3*5*29
	print(largestprimefactor(n))
	print(largestprimefactor(q))
	
	while (n > 1):
		d = largestprimefactor(n)
		n = n/d
		
	print(6857*1471*839*71)
	
	print(largestprimefactor(7**41))
	
if __name__ == "__main__":
	main()
