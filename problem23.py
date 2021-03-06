import time
import math

N = 28124 # We know a priori that any number N or larger can be written as the sum of 2 abundant integers

def proper_divisors(n):
	"""
	Compute all proper divisors of a positive integer n and return them as a list (not sorted)
	"""
	a, r = 1, [1]
	while a * a < n:
		a += 1
		if n % a: continue
		b, f = 1, []
		while n % a == 0:
			n //= a
			b *= a
			f += [i * b for i in r]
		r += f
	if n > 1: r += [i * n for i in r]
	return r[:-1]

def find_abundant(n):
	"""
	return the set of all positive integers that are abundant and < n
	"""
	s = set([])
	for j in range(12,n,1):
		if sum(proper_divisors(j)) > j:
			s = s.union([j])		
	return s

def abundant_sums(n):
	a = find_abundant(n)
	s = set([i + j for i in a for j in a if i + j < n])
	return s
	
def non_abundant_sums():
	"""
	Computes the pairwise sums of all pairs of distinct abundant numbers less than N
	"""
	s = abundant_sums(N)
	#return (N-1)*N/2 - sum(s)
	t = set([i for i in range(1,N,1) if i not in s]) #doesn't add much extra compute time to return the set of all such non abundant sums instead of the sum of them
	return t
		
def test():
	print(len(find_abundant(30000)))
	print(len(abundant_sums(30000)))
	
def main():
	start = time.time()
	t = non_abundant_sums()
	print(sum(t))
	print(len(t))
	end = time.time()
	print(end-start)
	
if __name__ == "__main__":
	#test()
	main()
