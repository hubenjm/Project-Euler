import time
import math

def proper_divisors(n):
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

def find_abundant(N):
	"""
	return the set of all positive integers that are abundant and < N
	"""
	s = set([])
	for j in range(12,N,1):
		if sum(proper_divisors(j)) > j:
			s = s.union([j])		
	return s

def abundant_sums(N):
	a = find_abundant(N)
	s = set([i + j for i in a for j in a if i + j < N])
	return s
	
def old_non_abundant_sums():
	N = 28124
	s = abundant_sums(N)
	t = []
	for j in range(1,N,1):
		if j not in s:
			t += [j]
	return t
	
def non_abundant_sums():
	N = 28124
	s = abundant_sums(N)
	#return (N-1)*N/2 - sum(s)
	t = set([i for i in range(1,N,1) if i not in s])
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
