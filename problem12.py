import math

def smallestfactor(n):
	m = int(math.sqrt(n))+1
	i = 1
	while (i <= m):
		i += 1
		if n%i == 0:
			return i
	return n # in this case n is prime
	
def numfactors(n):
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
	return len(r)
	
def test():
	j = 1
	maxd = 1
	while j <= 10000:
		n = j*(j+1)/2
		maxd = max(maxd, numfactors(n))	
		j += 1
		
	print(maxd)
	
def main():
	n = 2
	t = n*(n+1)/2
	while numfactors(t) <= 500:
		n += 1
		t += n
		
	print(n)
	print(t)
	print(numfactors(t))
	
if __name__ == "__main__":
	#test()
	main()
		
