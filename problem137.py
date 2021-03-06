import math
import time
import gmpy

#recycles some factorization code from problem3.py
def smallest_factor(n):
	m = int(math.sqrt(n))
	i = 1
	while (i <= m):
		i += 1
		if n%i == 0:
			return i
	return n # in this case n is prime

def largest_prime_factor(n):
	p = smallest_factor(n)
	while(p < n):
		n = n/p
		p = smallest_factor(n)
	return n
###

def get_factors(n):
	f = {}
	while n > 1:
		#p = largest_prime_factor(n)
		p = smallest_factor(n)
		count = 0
		f[p] = 0
		while n % p == 0:
			n /= p
			count += 1
		f[p] += count
	return f

def is_square(n):
	"""
	Tests whether a given positive integer n is a perfect square
	"""
	x = n // 2
	seen = set([x])
	while x*x != n:
		x = (x + (n // x))//2
		if x in seen: return False
		seen.add(x)
	return True

def rational_golden_nugget(N):
#	assert N > 10, "N should be an integer larger than 10"
#	k = 74049691

#(k, 5*k^2 + 2*k + 1)
#(2, 25)
#(15, 1156)
#(104, 54289)
#(714, 2550409)
#(4895, 119814916)
#(33552, 5628750625)
#(229970, 264431464441)
#(1576239, 12422650078084)
#(10803704, 583600122205489)
#(74049690, 27416783093579881)
#(507544127, 1288005205276048900)

	#s = [2,15,104,714,4895,33552,229970,1576239,10803704,74049690,507544127]
	
	index = 8
	k = 10803704
	kold = k
	d = 5*k**2 + 2*k + 1
	while index < N:
		if gmpy.is_square(d):
			index += 1
			print(index, k, d)
			kold = k
			k = int(6.8541*k)
			d = 5*k**2 + 2*k + 1
		d += 10*k + 7
		k += 1
	return kold
	
def test():
	print(smallest_factor(8))
	print(smallest_factor(27))
	print(largest_prime_factor(27))
	print(is_square(9))
	print(is_square(144))
	print(get_factors(14256376))

	start = time.time()
	print(is_square(544523231234123521123412341324**2))
	end = time.time()
	print(end-start)
	
def main():
	N = 25
	print(rational_golden_nugget(N))	

if __name__ == "__main__":
	#test()
	main()
	
	
			
			
	
	
